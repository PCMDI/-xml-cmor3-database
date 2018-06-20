#!/usr/bin/env bash
ROOT_PATH="/git"
SQLITE3=${SQLITE3:-sqlite3}
CMIP6DB=${CMIP6DB:-CMIP6.sql3}

for realm in $(${SQLITE3} "${CMIP6DB}" \
                'select distinct mipTable from CMORvar'); do
    filename="CMIP6_${realm}.json"
    echo $filename
    cp /tmp/$filename .
    cp $filename ${ROOT_PATH}/cmor/Tables/
    cp $filename ${ROOT_PATH}/cmip6-cmor-tables/Tables
done
for filename in CMIP6_coordinate.json CMIP6_formula_terms.json; do 
    cmd="cp /tmp/$filename ."
    echo $cmd
    $cmd
    cmd="cp /tmp/$filename ${ROOT_PATH}/cmor/TestTables/"
    echo $cmd
    $cmd
    cmd="cp /tmp/$filename ${ROOT_PATH}/cmip6-cmor-tables/Tables"
    echo $cmd
    $cmd
done
exit 0
