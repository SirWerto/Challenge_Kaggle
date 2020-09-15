#!/bin/bash


# DATA SCIENCE PROYECT TREE CREATOR
if [[ "$1" != "" ]]; then
    DIR="$1"
else
    echo "Need project name"
    exit
fi

mkdir -pv "${DIR}"
mkdir -v "${DIR}/raw_data"
mkdir -v "${DIR}/tables"
mkdir -v "${DIR}/tables/clean_scripts"
mkdir -v "${DIR}/tables/data_cleaned"
mkdir -v "${DIR}/models"
mkdir -v "${DIR}/simulations"
mkdir -v "${DIR}/pictures"


