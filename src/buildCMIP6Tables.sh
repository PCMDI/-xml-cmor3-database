#!/bin/bash

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
