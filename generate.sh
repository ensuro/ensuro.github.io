#!/bin/bash

j2 -f yaml index.j2 input.yaml  > index.html
j2 -f yaml aboutus.j2 input.yaml  > aboutus.html
