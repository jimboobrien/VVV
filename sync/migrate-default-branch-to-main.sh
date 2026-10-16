#!/usr/bin/env bash
# Rename the default branch master -> main and move checkouts over safely.
#   ./migrate-default-branch-to-main.sh                        # dry run (default): GitHub rename + local VVV copies
#   ./migrate-default-branch-to-main.sh --apply                # rename on GitHub (needs `gh`) + switch clean local VVV copies
#   ./migrate-default-branch-to-main.sh --apply --local-only   # skip the GitHub rename (already done)
#   ./migrate-default-branch-to-main.sh --servers [--apply]    # switch SiteGround server copies over SSH (uses deploy-registry.json)
#   ./migrate-default-branch-to-main.sh [...] pegasus pegasus-wow   # limit to these repos
# pegasus-child is skipped unless named explicitly (its site branches are never renamed).
# Every switch (local or server) is the same safe sequence, never checkout -B / branch -D:
#   refuse if dirty; git fetch origin main:refs/remotes/origin/main;
#   refuse if `git rev-list origin/main..master` is non-empty (commits that would be stranded);
#   git checkout -b main --track origin/main (refuse if a local main exists and differs from origin/main);
#   git branch -d master (safe delete; failure is reported, not forced).
set -uo pipefail
OWNER=Visionquest-Development
APPLY=false; LOCAL_ONLY=false; SERVERS=false; REPOS=()
for a in "$@"; do case "$a" in --apply) APPLY=true;; --local-only) LOCAL_ONLY=true;; --servers) SERVERS=true;; -h|--help) sed -n 2,14p "$0"; exit 0;; *) REPOS+=("$a");; esac; done
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; WWW="$(dirname "$HERE")/www"; REG="$HERE/deploy-registry.json"
[ ${#REPOS[@]} -gt 0 ] || REPOS=(pegasus $(jq -r '.components | to_entries[] | select(.value.type=="plugin") | .key' "$REG"))

# Safe switch, run in a checkout dir. Args: DIR OLD NEW APPLY(true|false). Prints one status line per dir.
SWITCH_FN='
switch_branch() {
  local d="$1" old="$2" new="$3" apply="$4" cur
  cd "$d" 2>/dev/null || { echo "FAIL    $d (cannot cd)"; return; }
  cur=$(git rev-parse --abbrev-ref HEAD 2>/dev/null) || { echo "FAIL    $d (git error)"; return; }
  [ "$cur" = "$new" ] && { echo "OK      $d (already on $new)"; return; }
  [ "$cur" = "$old" ] || { echo "SKIP    $d (on $cur, not $old)"; return; }
  [ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "DIRTY   $d (uncommitted changes, not switched)"; return; }
  git fetch -q origin "$new:refs/remotes/origin/$new" 2>/dev/null || { if [ "$apply" = true ]; then echo "FAIL    $d (origin has no $new yet - rename on GitHub first)"; else echo "PENDING $d (clean, on $old; switches once origin has $new)"; fi; return; }
  local extra; extra=$(git rev-list "origin/$new..$old" 2>/dev/null | wc -l)
  [ "$extra" -eq 0 ] || { echo "SKIP    $d ($old has $extra commit(s) not in origin/$new - push/merge them first)"; return; }
  if git show-ref --verify --quiet "refs/heads/$new" && [ "$(git rev-parse "$new")" != "$(git rev-parse "origin/$new")" ]; then
    echo "SKIP    $d (local $new exists and differs from origin/$new)"; return; fi
  if [ "$apply" != true ]; then echo "WOULD   $d: fetch origin/$new, checkout -b $new --track origin/$new, branch -d $old"; return; fi
  if git show-ref --verify --quiet "refs/heads/$new"; then git checkout -q "$new" && git branch -q -u "origin/$new" "$new"
  else git checkout -q -b "$new" --track "origin/$new"; fi || { echo "FAIL    $d (checkout $new failed)"; return; }
  git remote set-head origin -a >/dev/null 2>&1 || true
  if git branch -d "$old" >/dev/null 2>&1; then echo "SWITCHED $d ($old -> $new, $old deleted)"
  else echo "SWITCHED $d ($old -> $new; WARNING: git branch -d $old refused, left in place)"; fi
}'
eval "$SWITCH_FN"

gh_default() { git ls-remote --symref "git@github.com:$OWNER/$1.git" HEAD 2>/dev/null | sed -n 's@^ref: refs/heads/\([^[:space:]]*\).*@\1@p'; }

for repo in "${REPOS[@]}"; do
  echo "== $repo"
  def=$(gh_default "$repo"); echo "  GitHub default: ${def:-unknown}"
  kind=$(jq -r --arg r "$repo" '.components[$r].type // "plugin"' "$REG")
  folders=$(jq -r --arg r "$repo" '(.components[$r].folders // [$r])[]' "$REG")
  if $SERVERS; then
    [ "$def" = main ] || { echo "  servers: GitHub default is not main yet - rename first"; continue; }
    jq -r --arg r "$repo" '.sites | to_entries[] | select(.value.enabled == true)
      | select($r == "pegasus" or .value.plugins == null or ((.value.plugins // []) | index($r) != null))
      | [.key, .value.ssh_user, .value.ssh_host, (.value.ssh_port // 18765 | tostring), .value.wp_content] | @tsv' "$REG" |
    while IFS=$'\t' read -r site user host port wpc; do
      for f in $folders; do
        dir="$wpc/${kind}s/$f"
        out=$(ssh -n -o BatchMode=yes -o ConnectTimeout=15 -p "$port" "$user@$host" \
              "$SWITCH_FN"$'\n'"[ -d '$dir/.git' ] && switch_branch '$dir' master main $APPLY || true" 2>&1) \
          || out="FAIL    ssh to $user@$host failed: ${out##*$'\n'}"
        [ -n "$out" ] && echo "  [$site] $out"
      done
    done
    continue
  fi
  if [ "$def" = master ] && ! $LOCAL_ONLY; then
    if $APPLY; then
      command -v gh >/dev/null || { echo "  ERROR: gh not installed; rename in GitHub settings and re-run with --local-only"; continue; }
      gh api -X POST "repos/$OWNER/$repo/branches/master/rename" -f new_name=main >/dev/null && echo "  renamed on GitHub" || { echo "  ERROR: GitHub rename failed"; continue; }
    else echo "  would run: gh api -X POST repos/$OWNER/$repo/branches/master/rename -f new_name=main"; fi
  fi
  for f in $folders; do
    for d in "$WWW"/*/public_html/wp-content/${kind}s/"$f"; do
      [ -d "$d/.git" ] || continue
      case "$(git -C "$d" config --get remote.origin.url)" in *"/$repo.git"|*"/$repo"|*":$OWNER/$repo.git") ;; *) echo "  SKIP    ${d#$WWW/} (different remote)"; continue;; esac
      echo "  $( (switch_branch "$d" master main $APPLY) | sed "s@$WWW/@@")"
    done
  done
done
$APPLY || echo "Dry run only. Add --apply to make changes."
