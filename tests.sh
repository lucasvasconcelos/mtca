#!/bin/bash

rm -f ./pep8.report ./pylint.report ./pyflakes.report ./coverage.xml

python3.4 -m coverage run ./discover_tests.py

python3.4 -m coverage xml -o coverage.xml --include=mtca*

pep8 mtca > ./pep8.report || true
flake8 --select=F --format=pylint mtca > ./pyflakes.report || true
pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --reports=n mtca > ./pylint.report || true
