#!/usr/bin/env bash
# Copy the registry-driven deploy workflow from pegasus-child's default branch (master or main) onto every site branch mapped in the registry.
# Run AFTER merging Visionquest-Development/pegasus-child#4.
#   ./apply-deploy-workflow-to-child-branches.sh            # dry run: shows what would change per branch
#   ./apply-deploy-workflow-to-child-branches.sh --push     # commit + push (each push triggers that site's deploy!)
#   ./apply-deploy-workflow-to-child-branches.sh --push mabellas_theme ulg_theme   # only these branches
# Never force-pushes, never touches the default branch. Uses a temp clone; your local working copies are untouched.
set -euo pipefail
PUSH=false; [ "${1:-}" = "--push" ] && { PUSH=true; shift; }
ONLY=("$@")
REPO=git@github.com:Visionquest-Development/pegasus-child.git
WF=.github/workflows/deploy-siteground.yml
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
git clone -q "$REPO" "$TMP/pc"; cd "$TMP/pc"
DEF=$(git symbolic-ref --short refs/remotes/origin/HEAD | sed "s@^origin/@@")   # master or main
echo "pegasus-child default branch: $DEF"
git show origin/$DEF:.github/deploy/sites.json >/dev/null 2>&1 || { echo ".github/deploy/sites.json not on $DEF yet - merge pegasus-child#4 first"; exit 1; }
git show origin/$DEF:$WF | grep -q "contents: read" || { echo "$DEF workflow is not the registry-driven one yet"; exit 1; }
mapfile -t BRANCHES < <(git show origin/$DEF:.github/deploy/sites.json | jq -r --arg def "$DEF" '.sites[].child_branch | select(. != "" and . != $def)' | sort -u)
[ ${#ONLY[@]} -gt 0 ] && BRANCHES=("${ONLY[@]}")
for b in "${BRANCHES[@]}"; do
  if ! git show-ref -q "refs/remotes/origin/$b"; then echo "MISSING  $b (no such branch on GitHub - fix registry or create branch)"; continue; fi
  git checkout -q -B "$b" "origin/$b"
  git checkout origin/$DEF -- "$WF"
  if git diff --cached --quiet; then echo "CURRENT  $b"; continue; fi
  git commit -q -m "Use registry-driven SiteGround deploy workflow (from $DEF)"
  if $PUSH; then git push -q origin "$b" && echo "PUSHED   $b $(git rev-parse --short HEAD)  -> deploy triggered"; else echo "WOULD    $b ($(git diff --stat HEAD~1 | tail -1))"; fi
done
$PUSH || echo "Dry run only. Re-run with --push to apply."
