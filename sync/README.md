# sync/ — Pegasus / SiteGround tooling

Deploys run on GitHub Actions (see `../DEPLOY-SITEGROUND.md`). This folder holds the registry and the tools that maintain it.
Everything goes through one entry point, `sync/pegasus.sh`.

| File | Purpose |
|------|---------|
| `pegasus.sh` | Entry point (subcommands below) |
| `sites.json` | **Source of truth**: sites, SSH host/user/path, host-key fingerprints, child branches |
| `repos.json` | Local VVV repo map (used by `status vvv`) |
| `deploy-registry.json` | Generated registry; vendored as `.github/deploy/sites.json` in each pegasus repo. Don't edit by hand |
| `deploy-siteground.template.yml` | Workflow template (`#BRANCHES#`, `#DEPLOY_SCRIPT#` placeholders) |
| `remote-deploy.sh` | Server-side script inlined into the workflow |
| `migrate-default-branch-to-main.sh` | One-off master→main rename helper (GitHub, local, `--servers`) |
| `lib/build_registry.py` | Registry builder + workflow render/apply |
| `lib/rescan_status.py` | Rescans local pegasus copies → `/pegasus-status` data |
| `lib/rollout_child.sh` | Copies pegasus-child's default-branch workflow onto site branches |
| `lib/git_status.sh`, `lib/setup_repos.sh` | Local VVV status view; clone missing repos |

## Commands

```bash
sync/pegasus.sh registry --child-branches auto                 # rebuild deploy-registry.json (+ sites.json, repos.json)
sync/pegasus.sh registry --child-branches auto --refresh-fingerprints   # keyscans SiteGround, 5s apart
sync/pegasus.sh registry --refresh-fingerprints --known-hosts-only       # no network; pins only hosts in ~/.ssh/known_hosts
sync/pegasus.sh workflow render pegasus-child                   # print a repo's workflow (stdout only)
sync/pegasus.sh workflow apply [repo..]                         # dry run: which repos need workflow/registry updates
sync/pegasus.sh workflow apply --push [repo..]                  # push chore/sync-deploy-workflow-<date> per repo; open the PRs yourself
sync/pegasus.sh rollout-child [--push] [branch..]               # site-branch rollout (each push deploys that site!)
sync/pegasus.sh status                                          # fetch + rescan local pegasus copies (/pegasus-status)
sync/pegasus.sh status vvv                                      # old git-status view of VVV repos
sync/pegasus.sh setup                                           # clone missing theme/plugin repos into VVV
```

Notes:
- `workflow apply` never pushes a default branch. `rollout-child` pushes site branches, and site branches auto-deploy.
- `--known-hosts-only` replaces stored pins with what's in your known_hosts and blanks hosts that aren't there. Review `git diff sync/deploy-registry.json` before committing.
- The old manual SSH deploy (`deploy.sh` + `.env`) is retired and lives in `../backups/sync/` (git-ignored) for emergencies.

## SiteGround auto-deploy (GitHub Actions)

Pushing to `pegasus` or a `pegasus-*` plugin (default branch), or to a pegasus-child site branch, runs `git pull --ff-only` on the matching SiteGround sites.
- Registry: `sync/sites.json` → `sync/pegasus.sh registry` → `sync/deploy-registry.json` → vendored as `.github/deploy/sites.json` in each repo (+ per-repo workflows via `sync/pegasus.sh workflow render|apply`)
- Roll the workflow out to site branches with `sync/pegasus.sh rollout-child [--push]`
- Secrets, the per-server checklist, staging sites and how to add a site: see `DEPLOY-SITEGROUND.md`
