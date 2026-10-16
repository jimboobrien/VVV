# Runs on the SiteGround server. All inputs arrive as env vars (validated in the plan job); nothing is templated in.
# Output is public (Actions log): one line per site, "<site>: DEPLOYED <sha> | SKIP <category> | FAIL <category>".
# No paths, hostnames, file names, commit subjects or raw git output are printed. Git's own output is discarded.
# SKIP (exit 0): not installed, no .git, detached HEAD, other branch checked out (incl. master/main after a rename:
# never switched here, see DEPLOY-SITEGROUND.md 'Moving to main'). Any git error -> FAIL (exit 1).
S="$DEPLOY_SITE"
skip() { echo "$S: SKIP $1"; exit 0; }
fail() { echo "$S: FAIL $1"; exit 1; }
BASE="${DEPLOY_WP_CONTENT}/${DEPLOY_KIND}s"
DIR=""
for f in $DEPLOY_FOLDERS; do
  if [ -d "$BASE/$f" ]; then DIR="$BASE/$f"; break; fi
done
[ -n "$DIR" ] || skip "not installed ($DEPLOY_KIND $DEPLOY_REPO)"
cd "$DIR" >/dev/null 2>&1 || fail "cannot enter install folder"
[ -e .git ] || skip "not a git checkout"
CUR="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)" || fail "git rev-parse error"
[ -n "$CUR" ] || fail "git rev-parse error"
[ "$CUR" != "HEAD" ] || skip "detached HEAD"
ST="$(git status --porcelain --untracked-files=no 2>/dev/null)" || fail "git status error"
if [ "$CUR" != "$DEPLOY_BRANCH" ]; then
  # Never switch branches on the server automatically (no checkout -B / branch -D here).
  case "$CUR:$DEPLOY_BRANCH" in
    master:main|main:master) skip "server on $CUR, default is $DEPLOY_BRANCH: run sync/migrate-default-branch-to-main.sh --servers or switch manually" ;;
    *) skip "wrong branch checked out (expected $DEPLOY_BRANCH)" ;;
  esac
fi
[ -z "$ST" ] || fail "dirty working tree ($(printf '%s\n' "$ST" | wc -l | tr -d ' ') files)"
git fetch -q --prune origin >/dev/null 2>&1 || fail "git fetch error"
git pull -q --ff-only origin "$DEPLOY_BRANCH" >/dev/null 2>&1 || fail "git pull --ff-only error (diverged or conflict)"
echo "$S: DEPLOYED $(git rev-parse --short HEAD 2>/dev/null)"
