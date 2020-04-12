#!/bin/bash

pip freeze | grep -E "molecule|ansible|virtualenvwrapper|flake8|yamllint|vagrant" > requirements-dev.txt
