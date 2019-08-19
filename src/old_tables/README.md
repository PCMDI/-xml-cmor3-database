This directory contains the old CMIP5 & CMIP6 tables and Python script used make `CMOR3_axes.json`, `CMOR3_formula_terms.json`, and `CMOR3_grid.json`.  The previous version of `convertXML.py` used these tables for storing formula terms, axes, and grid variables that were not in the data request XML.  The Python script in this directory organizes these variables into more compact and easy to parse JSON files.

**This directory is only for archival reasons and shouldn't be used to edit the current CMOR3_axes.json, CMOR3_formula_terms.json, and CMOR3_grid.json in the `src` directory.  New additions and changes to the CMIP6 CMOR tables should be done by directly editing these JSON files, or via the data requests.**

The Python script requires pylibconfig2 and pyparsing.
```
pip install pylibconfig2 pyparsing
```

Run the script inside of this directory to generate the JSON files, and then copy them into the source directory.
```
cd src/old_tables
python convertLibconfig2JSON.py
cp CMOR3_*.json ..
```
