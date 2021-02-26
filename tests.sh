#!/bin/bash

export PYTHONPATH=$PYTHONPATH:../promptwithoptions

poetry run pytest -v tests "$@"
