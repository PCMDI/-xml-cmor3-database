# Create CMIP6 CMOR tables from the [CMIP6 Data Request](https://earthsystemcog.org/projects/wip/CMIP6DataRequest) XML document.

## Steps

1. Go into the `src` directory.
    ```
    cd src
    ```
2. Get latest changes from the [SVN repository](http://proj.badc.rl.ac.uk/svn/exarch/CMIP6dreq/tags/) for the data request, and copy the data request XML to the `docs` directory.
    ```
    bash cpyfromsvn.sh /path/to/svn/CMIP6dreq/tags/01.00.XX
    ```
3. Create a SQL database from the data request.
    ```
    python convertXML.py
    ```
4. Create tables with the database.  The tables will be stored in `/tmp/`.
    ```
    bash createAllTables.sh
    ```
    Optionally, see the differences between the old and new tables.
    ```
    bash diffAllTables.sh
    ```
5. Copy the tables from `/tmp/` into the `tables` directory, and into the table directories of your cmip6-cmor-tables and CMOR repos.
    ```
    bash copyAllTables.sh
    ```
