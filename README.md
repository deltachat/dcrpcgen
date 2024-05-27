# Delta Chat JSON-RPC Code Generator

[![Latest Release](https://img.shields.io/pypi/v/dcrpcgen.svg)](https://pypi.org/project/dcrpcgen)
[![CI](https://github.com/deltachat/dcrpcgen/actions/workflows/python-ci.yml/badge.svg)](https://github.com/deltachat/dcrpcgen/actions/workflows/python-ci.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Automatic code generation for the Delta Chat JSON-RPC API.

## Install

```sh
pip install git+https://github.com/deltachat/dcrpcgen
```

## Usage

To generate Java bindings given a local JSON-RPC schema file `./schema.json`
and save the generated code to `./src/` folder:

```
dcrpcgen java --schema schema.json --output src
```

Run `dcrpcgen --help` to see all available options.
