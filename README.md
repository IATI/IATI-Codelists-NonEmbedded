# IATI NonEmbedded Codelists

[![CI](https://github.com/IATI/IATI-Codelists-NonEmbedded/actions/workflows/CI.yml/badge.svg)](https://github.com/IATI/IATI-Codelists-NonEmbedded/actions/workflows/CI.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/IATI/IATI-Codelists-NonEmbedded/blob/master/LICENSE)

## Introduction

These are codelists used by the IATI Standard, but not "Embedded" within it, so not subject to the same change control progress. For more information see https://github.com/IATI/IATI-Codelists#embedded-vs-nonembedded-codelists

## Updates

Updates can come from a variety of sources, including [OCED DAC and CRS Codes](http://www.oecd.org/development/financing-sustainable-development/development-finance-standards/dacandcrscodelists.htm) and ISO updates (e.g. new currency [link](https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/amendments/dl_currency_iso_amendment_170.pdf))

## Process

1. Create a branch from `master` and commit the codelist changes
1. Create a Pull Request from the branch to `master`
1. Have Pull Request reviewed/approved
1. Merge Pull Request to update `master`

## Downstream Updates

### IATI Standard Website

- The [IATI/IATI-Reference-Generator](https://github.com/IATI/IATI-Reference-Generator) repo should be used to rebuild the SSOT documentation and upload to the website following that process. 
- This will ensure the updates to the codelists are reflected on the IATI Standard website.

### IATI Validator

- The [Validator](https://iativalidator.iatistandard.org) utilises a transformed version of the Codelists stored in [IATI/IATI-Validator-Codelists](https://github.com/IATI/IATI-Validator-Codelists). 
- When changes are pushed to this `master` branch, the `update-validator-codelists` job in `.github/workflows/CI.yml` triggers a GitHub action in [IATI/IATI-Validator-Codelists](https://github.com/IATI/IATI-Validator-Codelists). 
- Follow the [Update Process](https://github.com/IATI/IATI-Validator-Codelists#update-process) as documented in the IATI-Validator-Codelists repo

### IATI Datastore

- The [Datastore Search](https://datastore.iatistandard.org) utilises a transformed version of the Codelists stored in [IATI/dss-filters](https://github.com/IATI/dss-filters)
- See [IATI/dss-filters](https://github.com/IATI/dss-filters) for instructions on updating the Codelists used by Datastore Search.

## Information for developers

This tool supports Python 3.x. To use this script, we recommend the use of a virtual environment::

```bash
python3 -m venv pyenv
source pyenv/bin/activate
pip install -r requirements.txt
python convert.py
```