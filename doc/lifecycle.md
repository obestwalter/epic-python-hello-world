# Aspects of any (non trivial) project

# source control / backup / collaboration

One might argue that this approach is too optimistic, but in my opinion git in 
combination with Github (or occasionally Bitbucket, but I prefer Github) covers all those problems atm.

# Tests

## pytest + tox
    * minimal boilerplate
    * runner and framework together
    * killer feature: fixtures
    * Holger Krekels tools generally rock and play nicely together

# Documentation

* Sphinx


# The lifecycle of a python script

## create

* create a local git repository
* create virtualenv (same name)
* connect to gigthub



## develop

* build
* test

## publish

* build
    * tests
    * documentation
    * package
    
* push artefacts online


## (maybe) modify project

* rename complete project
    * repo (rename folder)
    * virtualenv (rename folder)
    * git repo (rename repo; git remote set-url origin new_url)
