#!/bin/bash

set -euo pipefail

VENV_PATH=${VENV_PATH:-./venv}

if [ ! -d $VENV_PATH ]; then
    python3 -m venv $VENV_PATH
    source $VENV_PATH/bin/activate
    pip install j2cli[yaml]
else
    source $VENV_PATH/bin/activate
fi

TEMPLATES="index about careers investors"

for template in $TEMPLATES; do
    j2 -f yaml ${template}.j2 input.yaml  > build/${template}.html
done

cp -r static/* build/
