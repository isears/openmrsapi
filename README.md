# OpenMRS API Python Library

[![Build Status](https://travis-ci.org/isears/openmrsapi.svg?branch=master)](https://travis-ci.org/isears/openmrsapi)
[![Coverage Status](https://coveralls.io/repos/github/isears/openmrsapi/badge.svg?branch=master)](https://coveralls.io/github/isears/openmrsapi?branch=master)

A python library for interacting with OpenMRS API

## Install

```bash
git clone https://github.com/isears/openmrsapi
cd openmrsapi
pip3 install .
```

## Usage

Before using, setup the following environment variables based on your OpenMRS installation:

```bash
export OPENMRS_USERNAME=Admin
export OPENMRS_PASSWORD=Admin123
export OPENMRS_API_ENDPOINT=https://demo.openmrs.org/openmrs/ws/rest/v1/
```

Example:

```python
import openmrsapi

users = openmrsapi.get('user')

for user in users:
    print(user['display'])
```