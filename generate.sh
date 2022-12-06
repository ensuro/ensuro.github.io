#!/bin/bash

VENV_PATH=${VENV_PATH:-./venv}

if [ ! -d $VENV_PATH ]; then
    python3 -m venv $VENV_PATH
    source $VENV_PATH/bin/activate
    pip install j2cli[yaml]
else
    source $VENV_PATH/bin/activate
fi

j2 -f yaml index.j2 input.yaml  > build/index.html
j2 -f yaml aboutus.j2 input.yaml  > build/aboutus.html
j2 -f yaml careers.j2 input.yaml  > build/careers.html
cp -r static/* build/
