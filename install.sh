#!/bin/bash

if [ -d ".venv" ]
then
    source .venv/bin/activate
    pip install -r requirements.txt
else
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -U pip
    pip install -r requirements.txt
fi
