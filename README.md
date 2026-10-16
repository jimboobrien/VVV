# VVV

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/206b06167aaf48aab24422cd417e8afa)](https://www.codacy.com/gh/Varying-Vagrant-Vagrants/VVV?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Varying-Vagrant-Vagrants/VVV&amp;utm_campaign=Badge_Grade) [![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/varying-vagrant-vagrants/vvv.svg)](http://isitmaintained.com/project/varying-vagrant-vagrants/vvv "Average time to resolve an issue") [![Percentage of issues still open](http://isitmaintained.com/badge/open/varying-vagrant-vagrants/vvv.svg)](http://isitmaintained.com/project/varying-vagrant-vagrants/vvv "Percentage of issues still open")

VVV is a local developer environment, mainly aimed at [WordPress](https://wordpress.org) developers. It uses [Vagrant](https://www.vagrantup.com) and Docker/VirtualBox/Parallels/HyperV to create a linux server environment for building sites, and contributing to WordPress itself.

_VVV stands for Varying Vagrant Vagrants._

## How To Use

To use it, download and install [Vagrant](https://www.vagrantup.com) and a provider such as [VirtualBox](https://www.virtualbox.org/), Docker, or Parallels Pro. Then, clone this repository and run:

```shell
vagrant plugin install --local
vagrant up --provision
```

When it's done, visit [http://vvv.test](http://vvv.test).

The online documentation contains more detailed [installation instructions](https://varyingvagrantvagrants.org/docs/en-US/installation/).

* **Web**: [https://varyingvagrantvagrants.org/](https://varyingvagrantvagrants.org/)
* **Contributing**: Contributions are more than welcome. Please see our current [contributing guidelines](https://varyingvagrantvagrants.org/docs/en-US/contributing/). Thanks!

## Minimum System requirements

[For system requirements, please read the system requirements documentation here](https://varyingvagrantvagrants.org/docs/en-US/installation/software-requirements/)

## Software included

For a comprehensive list, please see the [list of installed packages](https://varyingvagrantvagrants.org/docs/en-US/installed-packages/).

## SiteGround auto-deploy (GitHub Actions)

Pushing to `pegasus` or a `pegasus-*` plugin (default branch), or to a pegasus-child site branch, runs `git pull --ff-only` on the matching SiteGround sites.
- Registry: `sync/sites.json` → `sync/pegasus.sh registry` → `sync/deploy-registry.json` → vendored as `.github/deploy/sites.json` in each repo (+ per-repo workflows via `sync/pegasus.sh workflow render|apply`)
- Roll the workflow out to site branches with `sync/pegasus.sh rollout-child [--push]`
- Secrets (org secrets limited to the 20 pegasus repos; no GitHub Environments), the per-server checklist, staging sites and how to add a site: see `DEPLOY-SITEGROUND.md`
