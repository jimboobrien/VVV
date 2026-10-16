#!/usr/bin/env bash
# Single entry point for the Pegasus / SiteGround tooling (deploys themselves run on GitHub Actions).
#   ./pegasus.sh registry [--child-branches "b1 b2"] [--offline] [--refresh-fingerprints [--known-hosts-only]]
#       Rebuild deploy-registry.json (+ sites.json/repos.json). --child-branches auto: list them from GitHub.
#       Fingerprint refresh keyscans SiteGround (5s apart, KEYSCAN_DELAY); add --known-hosts-only for no network.
#   ./pegasus.sh workflow render <repo>            Print that repo's rendered workflow (stdout only).
#   ./pegasus.sh workflow apply [--push] [repo..]  Dry run / push a chore/ branch per repo for a PR (never the default).
#   ./pegasus.sh rollout-child [--push] [branch..] Copy pegasus-child's default-branch workflow onto site branches (pushes deploy!).
#   ./pegasus.sh status [vvv]                      Rescan local pegasus copies -> /pegasus-status data; "vvv" = old git-status view.
#   ./pegasus.sh setup [args]                      Clone missing theme/plugin repos into VVV (lib/setup_repos.sh).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; LIB="$HERE/lib"
cmd="${1:-help}"; shift || true
case "$cmd" in
  registry)
    args=()
    while [ $# -gt 0 ]; do
      if [ "$1" = "--child-branches" ] && [ "${2:-}" = "auto" ]; then
        args+=(--child-branches "$(git ls-remote --heads git@github.com:Visionquest-Development/pegasus-child.git | sed 's@.*refs/heads/@@' | tr '\n' ' ')"); shift 2
      else args+=("$1"); shift; fi
    done
    exec python3 "$LIB/build_registry.py" "${args[@]}" ;;
  workflow)
    sub="${1:-}"; shift || true
    case "$sub" in
      render) [ $# -eq 1 ] || { echo "usage: $0 workflow render <repo>" >&2; exit 2; }; exec python3 "$LIB/build_registry.py" --render "$1" ;;
      apply)  exec python3 "$LIB/build_registry.py" --apply "$@" ;;
      *) echo "usage: $0 workflow render <repo> | apply [--push] [repo..]" >&2; exit 2 ;;
    esac ;;
  rollout-child) exec bash "$LIB/rollout_child.sh" "$@" ;;
  status)
    if [ "${1:-}" = "vvv" ]; then shift; exec bash "$LIB/git_status.sh" "$@"; fi
    exec python3 "$LIB/rescan_status.py" "$@" ;;
  setup) exec bash "$LIB/setup_repos.sh" "$@" ;;
  help|-h|--help) sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//' ;;
  *) echo "unknown command: $cmd" >&2; sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//' >&2; exit 2 ;;
esac
