#!/bin/bash
python-lambda-local -f lambda_handler -t 3 -e environment.json lambda_function.py ./event.json 