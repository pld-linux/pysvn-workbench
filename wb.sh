#!/bin/sh
export PYSVN_WORKBENCH_STDOUT_LOG=$(tty)

PYTHON=${PYTHON:-python}
exec ${PYTHON} /usr/share/pysvn-workbench/wb_main.pyc "$@"
