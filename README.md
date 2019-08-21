# Create CMIP6 CMOR tables from the [CMIP6 Data Request](https://earthsystemcog.org/projects/wip/CMIP6DataRequest) XML document.

## Steps

1. Go into the `src` directory.
    ```
    cd src
    ```
2. Run `bash buildCMIP6Tables.sh <DREQ-VERSION>` to get the latest changes from the [SVN repository](http://proj.badc.rl.ac.uk/svn/exarch/CMIP6dreq/tags/) for the provided data request version.  This script will then use the data request to form a database that will be used to create the CMIP6 CMOR tables.
    ```
    bash buildCMIP6Tables.sh 01.00.XX
    ```
3. Copy the CMIP6 tables from `tables` into the table directory of [cmip6-cmor-tables](https://github.com/PCMDI/cmip6-cmor-tables).
    ```
    cp ../tables/CMIP6_*.json ~/git/cmip6-cmor-tables/Tables
    ```
