#!/bin/bash


DATA_FOLDER=./data/clique
mkdir -p ${DATA_FOLDER}
pushd ${DATA_FOLDER}


CITE_1=https://www.dcs.gla.ac.uk/~pat/maxClique/distribution/DIMACS_cliques/
FILES_1=(
    brock200_1
    brock200_2
    brock200_3
    brock200_4
    brock400_1
    brock400_2
    brock400_3
    brock400_4
    hamming8-4
    johnson16-2-4
    johnson8-2-4
    keller4
    MANN_a27
    MANN_a9
    p_hat1000-1
    p_hat1000-2
    p_hat1500-1
    p_hat300-3
    p_hat500-3
    san1000
    sanr200_0.9
    sanr400_0.7
)

for VARIABLE in ${FILES_1[@]}; do
	wget -c ${CITE_1}${VARIABLE}.clq
done


CITE_2=https://mat.tepper.cmu.edu/COLOR02/INSTANCES/
FILES_2=(
    C125.9 
    gen200_p0.9_44
    gen200_p0.9_55
)

for VARIABLE in ${FILES_2[@]}; do
	wget -c ${CITE_2}${VARIABLE}.clq
done

popd