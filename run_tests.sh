#!/bin/bash
echo "Running test suite with coverage report at the end"
echo -e "( would require coverage python package to be installed )\n"

# comma separated list of directories to omit from report
OMIT="download_stats/tests/*"
# comma separeted list of packages to monitor when coverage is run
SOURCE="download_stats"

coverage run --source "$SOURCE" setup.py test
coverage report -m --omit "$OMIT"
