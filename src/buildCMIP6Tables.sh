#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a data request version number."
    exit 0
fi

dreq_num=$1
dreq_path="svn/CMIP6dreq/tags/${dreq_num}"
dreq_repo="http://proj.badc.rl.ac.uk/svn/exarch/CMIP6dreq/tags/${dreq_num}"

#----------------------
# Checkout data request
#----------------------
if [ ! -d ${dreq_path} ]; then
    echo "checking out ${dreq_repo}"
    svn co ${dreq_repo} ${dreq_path}
else
    pushd ${dreq_path}
    svn info
    ERR=$?
    popd
    if [ $ERR -ne 0 ];then
        echo "checking out ${dreq_repo}"
        svn co ${dreq_repo} ${dreq_path}
    else
        pushd ${dreq_path}
        echo "getting updates from ${dreq_repo}"
        svn update
        popd
    fi
fi
cp ${dreq_path}/dreqPy/docs/dreq.xml ../docs
cp ${dreq_path}/dreqPy/docs/vocab.xml ../docs
cp ${dreq_path}/dreqPy/packageConfig.py .

#-----------------------------------------
# Build SQL database from data request XML
#-----------------------------------------
python convertXML.py

#-----------------------------
# Use database to build tables
#-----------------------------
for realm in $(sqlite3 "CMIP6.sql3" \
                'select distinct mipTable from CMORvar'); do
    filename="CMIP6_${realm}.json"
    echo "Creating: ${filename}"
    echo "python CMORCreateTable.py -r ${realm} -j  > ../tables/${filename}"
    echo "python CMORCreateTable.py -r ${realm} -j  > ../tables/${filename}" |bash
done
cmd="python CMORCreateTable.py -j  -A > ../tables/CMIP6_coordinate.json"
echo $cmd
echo $cmd | bash
cmd="python CMORCreateTable.py -j  -F > ../tables/CMIP6_formula_terms.json"
echo $cmd
echo $cmd | bash
