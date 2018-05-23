#!/usr/bin/env bash
#ARRAY=(Amon LImon Lmon emMon  Omon Oclim Oday Oyr SIday SImon grids aero 3hr 6hrLev 6hrPlev cf3hr cfDay cfMon cfsites day fx)
#ARRAY=(3hr 6hrLev 6hrPlev 6hrPlevpt aerannual aerdaily aerfixed aerhourly aermonthly aero Amon AmonAdj cf3hr cfDay cfMon cfOff cfsites CORDEX_day day em em1hr em1hrclimmon em3hr em3hrpt emDay emDaypt emDayZ emFx emMon emMonclim emMonpt emMonZ emSubhr emYr fx LImon Lmon Oclim Oday Ofx Omon Oyr SIday SImon)

if [ `uname` = "Darwin" ]; then
    export DIFF_VIEW="/Applications/Visual Studio Code.app/Contents/MacOS/Electron"
else
    export DIFF_VIEW="code"
fi
SQLITE3=${SQLITE3:-sqlite3}
CMIP6DB=${CMIP6DB:-CMIP6.sql3}
for realm in $(${SQLITE3} "${CMIP6DB}" \
          'select distinct mipTable from CMORvar'); do                                                                                   
    filename="CMIP6_${realm}.json"                                                                                                             
    echo $filename
    "${DIFF_VIEW}" --diff /tmp/$filename $filename
done
"${DIFF_VIEW}" --diff /tmp/CMIP6_coordinate.json CMIP6_coordinate.json
"${DIFF_VIEW}" --diff /tmp/CMIP6_formula_terms.json CMIP6_formula_terms.json

exit 0
