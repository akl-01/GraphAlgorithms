#!/bin/bash

DATA_FOLDER=./data/coloring
FILES=(
    myciel3.col
    myciel7.col
    myciel.col
    school1.col
    school1_nsh.col
    anna.col
    miles1000.col
    miles1500.col
    le450_5a.col
    le450_15b.col
    queen11_11.col
)

CITE=https://mat.tepper.cmu.edu/COLOR02/INSTANCES/

mkdir -p ${DATA_FOLDER}
cd ${DATA_FOLDER}

for VARIABLE in ${FILES[@]}
do 
    wget ${CITE}${VARIABLE}
done