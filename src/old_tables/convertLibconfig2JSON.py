
import pylibconfig2
import json
import sqlite3
import xml.etree.ElementTree as ET
import uuid
import sys


conn = sqlite3.connect('./CMIP6.sql3')
conn.isolation_level = None
c = conn.cursor()
c.execute("""drop table if exists CMORvar""")
c.execute("""drop table if exists axisEntry""")

print("Create Tables")

c.execute(""" create table CMORvar (
        deflate text,
        deflate_level text,
        description text,
        frequency text,
        label text,
        mipTable text,
        modeling_realm text,
        ok_max_mean_abs text,
        ok_min_mean_abs text,
        positive text,
        prov text,
        provNote text,
        rowIndex text,
        shuffle text,
        stid text,
        title text,
        type text,
        uid text,
        valid_max text,
        valid_min text,
        vid text)""")

c.execute(""" create table axisEntry (
    name text,
    axis text,
    climatology text,
    formula text,
    long_name text,
    must_have_bounds text,
    out_name text,
    positive text,
    requested text,
    requested_bounds text,
    standard_name text,
    stored_direction text,
    tolerance text,
    type text,
    units text,
    valid_max text,
    valid_min text,
    value text,
    z_bounds_factors text,
    z_factors text,
    bounds_values text,
    generic_level_name text,
    origin text)""")


# -----------------------------------
# Read in dreq.xml and set namespace
# -----------------------------------
print("----------------------")
print("reading file dreq.xml")
print("----------------------")

contentDoc = ET.parse("../../docs/dreq.xml")
root = contentDoc.getroot()
namespace = '{urn:w3id.org:cmip6.dreq.dreq:a}'

# *********************************************************************
# Create first shot of axes from Martin's table.  If axes are missing,
# they will be created by reading CMIP5 tables
# *********************************************************************
axes = root.findall('./{0}main/{0}grids'.format(namespace))[0]
print("Create Martin's dreq.xml axes")
c.execute("begin")
for child in axes.getchildren():
    name               = child.get('label') or ""
    if name in ['alevel', 'olevel', 'alevhalf', 'olevhalf' ]:
        continue
    caxis              = child.get('axis') or ""
    long_name          = child.get('title') or ""
    must_have_bounds   = child.get('bounds') or ""
    out_name           = child.get('altLabel') or ""
    positive           = child.get('positive') or ""

    if child.get('boundsRequested'):
        requested_bounds = str([str(x) for x in child.get('boundsRequested').split()] )
    else:
        requested_bounds = ""

    if child.get('requested'):
        try:
            requested  = str([str(x) for x in child.get('requested').split()])
        except:
            try:
                requested  = str([str(x) for x in child.get('requested').split()])
            except:
                sys.exit(1)
    else:
        requested  = ""

    if child.get('boundsValues'):
        bounds_values = str([float(x.replace(",","")) for x in child.get('boundsValues').split()] )
        # convert list into string of values
        # -----------------------------------
        bounds_values = " ".join(str(value) for value in eval(bounds_values))
    else:
        bounds_values = ""

    standard_name      = child.get('standardName') or ""
    stored_direction   = child.get('direction') or ""
    ctype              = child.get('type') or ""
    units              = child.get('units') or ""
    valid_max          = child.get('valid_max') or ""
    valid_min          = child.get('valid_min') or ""
    value              = child.get('value') or ""
    tolerance          = ""
    z_bounds_factors   = ""
    z_factors          = ""
    climatology        = ""
    generic_level_name = ""
    if (name == 'time2') or (name == 'time3'):
        climatology        = "yes"
    formula            = ""
                        
    cmd = """select name from axisEntry where name = '""" + str(name).strip() + "';"
    c.execute(cmd)
    results = c.fetchall()
    if not results:
        cmd = """insert into axisEntry values (""" + \
              "'" + str(name)              + "'" + """, """ \
              "'" + str(caxis)             + "'" + """, """ \
              "'" + str(climatology)       + "'" + """, """ \
              "'" + str(formula)           + "'" + """, """ \
              "'" + str(long_name)         + "'" + """, """ \
              "'" + str(must_have_bounds)  + "'" + """, """ \
              "'" + str(out_name)          + "'" + """, """ \
              "'" + str(positive)          + "'" + """, """ \
              "'" + str(requested).replace("'","\"")        + "'" + """, """ \
              "'" + str(requested_bounds).replace("'", "\"")  + "'" + """, """ \
              "'" + str(standard_name)     + "'" + """, """ \
              "'" + str(stored_direction)  + "'" + """, """ \
              "'" + str(tolerance)         + "'" + """, """ \
              "'" + str(ctype)             + "'" + """, """ \
              "'" + str(units)             + "'" + """, """ \
              "'" + str(valid_max)         + "'" + """, """ \
              "'" + str(valid_min)         + "'" + """, """ \
              "'" + str(value)             + "'" + """, """ \
              "'" + str(z_bounds_factors)  + "'" + """, """ \
              "'" + str(z_factors)         + "'" + """, """ \
              "'" + str(bounds_values)     + "'" + """, """ \
              "'" + str(generic_level_name)     + "'" + """, """ \
              "'" + "XML"                  + "'" + """) """
        c.execute(cmd)
axes=""
c.execute("commit")

# ----------------------------------
#  Insert CMORvar in the database
# ----------------------------------
CMORvar = root.findall('./{0}main/{0}CMORvar'.format(namespace))[0]

print("Create CMORvar")

for child in CMORvar.getchildren():
    defaultPriority = child.get('defaultPriority') or ""
    deflate         = child.get('deflate')         or ""
    deflate_level   = child.get('deflate_level')   or ""
    description     = child.get('description')     or ""
    frequency       = child.get('frequency')       or ""
    label           = child.get('label')           or ""
    mipTable        = child.get('mipTable')        or ""
    modeling_realm  = child.get('modeling_realm')  or ""
    ok_max_mean_abs = child.get('ok_max_mean_abs') or ""
    ok_min_mean_abs = child.get('ok_min_mean_abs') or ""
    positive        = child.get('positive')        or ""
    prov            = child.get('prov')            or ""
    provNote        = child.get('provNote')        or ""
    rowIndex        = child.get('rowIndex')        or ""
    shuffle         = child.get('shuffle')         or ""
    stid            = child.get('stid')            or ""
    title           = child.get('title')           or ""
    vtype           = child.get('type')            or ""
    uid             = child.get('uid').replace('\'','')             or ""
    valid_max       = child.get('valid_max')       or ""
    valid_min       = child.get('valid_min')       or ""
    vid             = child.get('vid').replace('\'','')             or ""

    defaultPriority = defaultPriority.replace('None', '')
    deflate         = deflate.replace('None', '')
    deflate_level   = deflate_level.replace('None', '')
    description     = description.replace('None', '')
    frequency       = frequency.replace('None', '')
    label           = label.replace('None', '')
    mipTable        = mipTable.replace('None', '')
    modeling_realm  = modeling_realm.replace('None', '')
    ok_max_mean_abs = ok_max_mean_abs.replace('None', '')
    ok_min_mean_abs = ok_min_mean_abs.replace('None', '')
    positive        = positive.replace('None', '')
    prov            = prov.replace('None', '')
    provNote        = provNote.replace('None', '')
    rowIndex        = rowIndex.replace('None', '')
    shuffle         = shuffle.replace('None', '')
    stid            = stid.replace('None', '')
    title           = title.replace('None', '')
    title           = title.replace('\'', '\'\'')
    vtype           = vtype.replace('None', '')
    uid             = uid.replace('None', '')
    valid_max       = valid_max.replace('None', '')
    valid_min       = valid_min.replace('None', '')
    vid             = vid.replace('None', '')
    print(label)

    cmd = """insert into CMORvar values (""" + \
         "'" + deflate         + "'" + """, """ + \
         "'" + deflate_level   + "'" + """, """ + \
         "'" + description.replace("'", "\"")     + "'" + """, """ + \
         "'" + frequency       + "'" + """, """ + \
         "'" + label           + "'" + """, """ + \
         "'" + mipTable        + "'" + """, """ + \
         "'" + modeling_realm  + "'" + """, """ + \
         "'" + ok_max_mean_abs + "'" + """, """ + \
         "'" + ok_min_mean_abs + "'" + """, """ + \
         "'" + positive        + "'" + """, """ + \
         "'" + prov            + "'" + """, """ + \
         "'" + provNote        + "'" + """, """ + \
         "'" + rowIndex        + "'" + """, """ + \
         "'" + shuffle         + "'" + """, """ + \
         "'" + stid            + "'" + """, """ + \
         "'" + title           + "'" + """, """ + \
         "'" + vtype           + "'" + """, """ + \
         "'" + uid.replace('\'','')             + "'" + """, """ + \
         "'" + valid_max       + "'" + """, """ + \
         "'" + valid_min       + "'" + """, """ + \
         "'" + vid.replace('\'','')            + "'" + """) """
    c.execute(cmd)
CMORvar = ""

formulaEntries = {}
axisEntries = {}

files = ["Amon_libconfig", 
         "CMIP5_Omon_CMOR3", 
         "CMIP5_formula_CMOR3"]
for file in files:
    cfg = pylibconfig2.Config()
    cfg.read_file(file)
    # Add formula variables
    #
    formulaVar = [key for key in cfg.variable_entry.keys()
                   if cfg.variable_entry.__dict__[key].long_name.find("formula") != -1]
    variables = [key for key in cfg.axis_entries.keys() if hasattr(cfg.axis_entries.__dict__[key], 'z_factors')]

    z_bnds     = {key for var in variables for key in
                  cfg.axis_entries.__dict__[var].z_bounds_factors.split(" ")
                  if key.find(':') == -1
                  if key in cfg.variable_entry.__dict__.keys()}
    z_factors  = {key for var in variables for key in
                  cfg.axis_entries.__dict__[var].z_factors.split(" ")
                  if key.find(':') == -1
                  if key in cfg.variable_entry.__dict__.keys()}

    z_factors.update(z_bnds)

    formulaVar = list(z_factors)
    print("Create formula variables")
    for var in formulaVar:
        name = var
        long_name = cfg.variable_entry.__dict__[var].long_name           \
                        if ('long_name' in
                            cfg.variable_entry.__dict__[var].keys()) else ""
        ctype     = cfg.variable_entry.__dict__[var].type                 \
                        if ('type' in
                            cfg.variable_entry.__dict__[var].keys()) else ""
        dimensions = " ".join(cfg.variable_entry.__dict__[var].dimensions[:])\
                        if ('dimensions' in
                            cfg.variable_entry.__dict__[var].keys()) else ""
        units     = cfg.variable_entry.__dict__[var].units                \
                        if ('units' in
                            cfg.variable_entry.__dict__[var].keys()) else ""
        out_name     = cfg.variable_entry.__dict__[var].out_name          \
                        if ('out_name' in
                            cfg.variable_entry.__dict__[var].keys()) else name

        print(out_name)
        if name not in formulaEntries.keys():
            formulaEntries[name] = dict(name=name,
                                        long_name=long_name,
                                        type=ctype,
                                        dimensions=dimensions,
                                        out_name=out_name,
                                        units=units)
        else:
            print("{} already in formulaVar".format(name))

files = ["CMIP5_Omon_CMOR3", 
         "CMIP6_OImon_CMOR3", 
         "CMIP6_LImon_CMOR3",
         "CMIP6_Lmon_CMOR3", 
         "CMIP5_3hr_CMOR3",
         "CMIP5_cfSites_CMOR3", 
         "CMIP5_cf3hr_CMOR3", 
         "CMIP5_cfMon_CMOR3"]
for file in files:
    cfg = pylibconfig2.Config()
    cfg.read_file(file)
    # Add formula variables
    #
    variables = [key for key in cfg.axis_entries.keys()
                 if hasattr(cfg.axis_entries.__dict__[key], 'z_factors')]

    z_bnds     = {key for var in variables for key in cfg.axis_entries.__dict__[var].z_bounds_factors.split(" ")
                  if key.find(':') == -1  if key in cfg.variable_entry.__dict__.keys()}
    z_factors  = {key for var in variables for key in cfg.axis_entries.__dict__[var].z_factors.split(" ") if key.find(':') == -1
                  if key in cfg.variable_entry.__dict__.keys()}

    half = { key for key in cfg.variable_entry.keys() if key.find("_half")>-1 }
    print("HALF:",half)
    z_factors.update(z_bnds)
    z_factors.update(half)

    formulaVar = list(z_factors)
    print("Create formula variables")
    for var in formulaVar:
        name = var
        long_name = cfg.variable_entry.__dict__[var].long_name           \
                        if ('long_name' in
                            cfg.variable_entry.__dict__[var].keys()) else ""
        ctype     = cfg.variable_entry.__dict__[var].type                 \
                        if ('type' in
                            cfg.variable_entry.__dict__[var].keys()) else ""
        dimensions = " ".join(cfg.variable_entry.__dict__[var].dimensions[:])\
                        if ('dimensions' in
                            cfg.variable_entry.__dict__[var].keys()) else ""
        units     = cfg.variable_entry.__dict__[var].units                \
                        if ('units' in
                            cfg.variable_entry.__dict__[var].keys()) else ""
        out_name     = cfg.variable_entry.__dict__[var].out_name          \
                        if ('out_name' in
                            cfg.variable_entry.__dict__[var].keys()) else name

        print(out_name)
        if name not in formulaEntries.keys():
            formulaEntries[name] = dict(name=name,
                                        long_name=long_name,
                                        type=ctype,
                                        dimensions=dimensions,
                                        out_name=out_name,
                                        units=units)
        else:
            print("{} already in formulaVar".format(name))

    print("Create axes")
    for axis in cfg.axis_entries.keys():
        #
        #    for item in cfg.axis_entries.__getattribute__(axis).keys():
        #        print item
        #
        name               = axis
        caxis              = cfg.axis_entries.__getattribute__(axis).__getattribute__('axis')             \
                               if ('axis'             in cfg.axis_entries.__getattribute__(axis).keys())     else ""
        climatology        = cfg.axis_entries.__getattribute__(axis).__getattribute__('climatology')      \
                               if ('climatology'      in cfg.axis_entries.__getattribute__(axis).keys())     else ""
        formula            = cfg.axis_entries.__getattribute__(axis).__getattribute__('formula')          \
                               if ('formula'          in cfg.axis_entries.__getattribute__(axis).keys())     else ""
        long_name          = cfg.axis_entries.__getattribute__(axis).__getattribute__('long_name')        \
                               if ('long_name'        in cfg.axis_entries.__getattribute__(axis).keys())     else ""
        must_have_bounds   = cfg.axis_entries.__getattribute__(axis).__getattribute__('must_have_bounds') \
                               if ('must_have_bounds' in cfg.axis_entries.__getattribute__(axis).keys())     else ""
        out_name           = cfg.axis_entries.__getattribute__(axis).__getattribute__('out_name')         \
                               if ('out_name'       in cfg.axis_entries.__getattribute__(axis).keys())       else ""
        positive           = cfg.axis_entries.__getattribute__(axis).__getattribute__('positive').strip()         \
                               if ('positive'       in cfg.axis_entries.__getattribute__(axis).keys())       else ""
        requested          = cfg.axis_entries.__getattribute__(axis).__getattribute__('requested')        \
                               if ('requested'      in cfg.axis_entries.__getattribute__(axis).keys())       else ""
        requested_bounds   = cfg.axis_entries.__getattribute__(axis).__getattribute__('requested_bounds')        \
                               if ('requested_bounds'  in cfg.axis_entries.__getattribute__(axis).keys())    else ""
        standard_name      = cfg.axis_entries.__getattribute__(axis).__getattribute__('standard_name')    \
                               if ('standard_name'  in cfg.axis_entries.__getattribute__(axis).keys())       else ""
        stored_direction   = cfg.axis_entries.__getattribute__(axis).__getattribute__('stored_direction') \
                               if ('stored_direction' in cfg.axis_entries.__getattribute__(axis).keys())     else ""
        tolerance          = cfg.axis_entries.__getattribute__(axis).__getattribute__('tolerance')        \
                               if ('tolerance' in cfg.axis_entries.__getattribute__(axis).keys())            else ""
        ctype              = cfg.axis_entries.__getattribute__(axis).__getattribute__('type')             \
                               if ('type'      in cfg.axis_entries.__getattribute__(axis).keys())            else ""
        units              = cfg.axis_entries.__getattribute__(axis).__getattribute__('units')            \
                               if ('units'     in cfg.axis_entries.__getattribute__(axis).keys())            else ""
        valid_max          = cfg.axis_entries.__getattribute__(axis).__getattribute__('valid_max')        \
                               if ('valid_max' in cfg.axis_entries.__getattribute__(axis).keys())            else ""
        valid_min          = cfg.axis_entries.__getattribute__(axis).__getattribute__('valid_min')        \
                               if ('valid_min' in cfg.axis_entries.__getattribute__(axis).keys())            else ""
        value              = cfg.axis_entries.__getattribute__(axis).__getattribute__('value')            \
                               if ('value'     in cfg.axis_entries.__getattribute__(axis).keys())            else ""
        z_bounds_factors   = cfg.axis_entries.__getattribute__(axis).__getattribute__('z_bounds_factors') \
                               if ('z_bounds_factors'    in cfg.axis_entries.__getattribute__(axis).keys())  else ""
        z_factors          = cfg.axis_entries.__getattribute__(axis).__getattribute__('z_factors')        \
                               if ('z_factors' in cfg.axis_entries.__getattribute__(axis).keys())            else ""
        bounds_values      = cfg.axis_entries.__getattribute__(axis).__getattribute__('bounds_values')    \
                               if ('bounds_values' in cfg.axis_entries.__getattribute__(axis).keys())        else ""
        generic_level_name = cfg.axis_entries.__getattribute__(axis).__getattribute__('generic_level_name')    \
                               if ('generic_level_name' in cfg.axis_entries.__getattribute__(axis).keys())        else "" 

        cmd = """select name from axisEntry where name = '""" + str(name).strip() + "';"
        c.execute(cmd)
        results = c.fetchall()
        if not results and name not in axisEntries.keys():
            origin = file.split("_")[1]
            axisEntries[name] = dict(name=name,       
                                     axis=caxis,
                                     climatology=climatology,
                                     formula=formula.replace("\n","\\n"),
                                     long_name=long_name,
                                     must_have_bounds=must_have_bounds,
                                     out_name=out_name,
                                     positive=positive,
                                     requested=requested,
                                     requested_bounds=requested_bounds,
                                     standard_name=standard_name,
                                     stored_direction=stored_direction,
                                     tolerance=str(tolerance),
                                     type=ctype,
                                     units=units,
                                     valid_max=str(valid_max),
                                     valid_min=str(valid_min),
                                     value=str(value),
                                     z_bounds_factors=z_bounds_factors,
                                     z_factors=z_factors,
                                     bounds_values=bounds_values,
                                     generic_level_name=generic_level_name,
                                     origin=origin)
            print("Added axis {}".format(name))
        else:
            print("{} already in axisEntry".format(name))
            
with open('CMOR3_formula_terms.json','w') as f:
    json.dump(dict(formula_entry=formulaEntries), f, indent=4, sort_keys=True)

with open('CMOR3_axes.json','w') as f:
    json.dump(dict(axis_entry=axisEntries), f, indent=4, sort_keys=True)

gridVarEntries = {}
gridAxisEntries = {}

cfg = pylibconfig2.Config()
cfg.read_file("./CMIP5_grids_CMOR3")
print("Create axes for grids")
for axis in cfg.axis_entry.keys():
    print("FROM CMIP5_grids_CMOR3",axis)
    name               = axis
    caxis              = cfg.axis_entry.__getattribute__(axis).__getattribute__('axis')             \
                           if ('axis'             in cfg.axis_entry.__getattribute__(axis).keys())     else ""
    climatology        = cfg.axis_entry.__getattribute__(axis).__getattribute__('climatology')      \
                           if ('climatology'      in cfg.axis_entry.__getattribute__(axis).keys())     else ""
    formula            = cfg.axis_entry.__getattribute__(axis).__getattribute__('formula')          \
                           if ('formula'          in cfg.axis_entry.__getattribute__(axis).keys())     else ""
    long_name          = cfg.axis_entry.__getattribute__(axis).__getattribute__('long_name')        \
                           if ('long_name'        in cfg.axis_entry.__getattribute__(axis).keys())     else ""
    must_have_bounds   = cfg.axis_entry.__getattribute__(axis).__getattribute__('must_have_bounds') \
                           if ('must_have_bounds' in cfg.axis_entry.__getattribute__(axis).keys())     else ""
    out_name           = cfg.axis_entry.__getattribute__(axis).__getattribute__('out_name')         \
                           if ('out_name'       in cfg.axis_entry.__getattribute__(axis).keys())       else ""
    positive           = cfg.axis_entry.__getattribute__(axis).__getattribute__('positive').strip()         \
                           if ('positive'       in cfg.axis_entry.__getattribute__(axis).keys())       else ""
    requested          = cfg.axis_entry.__getattribute__(axis).__getattribute__('requested')        \
                           if ('requested'      in cfg.axis_entry.__getattribute__(axis).keys())       else ""
    requested_bounds   = cfg.axis_entry.__getattribute__(axis).__getattribute__('requested_bounds')        \
                           if ('requested_bounds'  in cfg.axis_entry.__getattribute__(axis).keys())  else ""
    standard_name      = cfg.axis_entry.__getattribute__(axis).__getattribute__('standard_name')    \
                           if ('standard_name'  in cfg.axis_entry.__getattribute__(axis).keys())       else ""
    stored_direction   = cfg.axis_entry.__getattribute__(axis).__getattribute__('stored_direction') \
                           if ('stored_direction' in cfg.axis_entry.__getattribute__(axis).keys())     else ""
    tolerance          = cfg.axis_entry.__getattribute__(axis).__getattribute__('tolerance')        \
                           if ('tolerance' in cfg.axis_entry.__getattribute__(axis).keys())            else ""
    ctype              = cfg.axis_entry.__getattribute__(axis).__getattribute__('type')             \
                           if ('type'      in cfg.axis_entry.__getattribute__(axis).keys())            else ""
    units              = cfg.axis_entry.__getattribute__(axis).__getattribute__('units')            \
                           if ('units'     in cfg.axis_entry.__getattribute__(axis).keys())            else ""
    valid_max          = cfg.axis_entry.__getattribute__(axis).__getattribute__('valid_max')        \
                           if ('valid_max' in cfg.axis_entry.__getattribute__(axis).keys())            else ""
    valid_min          = cfg.axis_entry.__getattribute__(axis).__getattribute__('valid_min')        \
                           if ('valid_min' in cfg.axis_entry.__getattribute__(axis).keys())            else ""
    value              = cfg.axis_entry.__getattribute__(axis).__getattribute__('value')            \
                           if ('value'     in cfg.axis_entry.__getattribute__(axis).keys())            else ""
    z_bounds_factors   = cfg.axis_entry.__getattribute__(axis).__getattribute__('z_bounds_factors') \
                           if ('z_bounds_factors'    in cfg.axis_entry.__getattribute__(axis).keys())  else ""
    z_factors          = cfg.axis_entry.__getattribute__(axis).__getattribute__('z_factors')        \
                           if ('z_factors' in cfg.axis_entry.__getattribute__(axis).keys())            else ""
    bounds_values      = cfg.axis_entry.__getattribute__(axis).__getattribute__('bounds_values')    \
                           if ('bounds_values' in cfg.axis_entry.__getattribute__(axis).keys())        else ""
    generic_level_name = ""
    origin="grid"

    cmd = """select name from axisEntry where name = '""" + str(name).strip() + "';"
    c.execute(cmd)
    results = c.fetchall()
    if not results:
        gridAxisEntries[name] = dict(name=name,       
                                     axis=caxis,
                                     climatology=climatology,
                                     formula=formula.replace("\n","\\n"),
                                     long_name=long_name,
                                     must_have_bounds=must_have_bounds,
                                     out_name=out_name,
                                     positive=positive,
                                     requested=requested,
                                     requested_bounds=requested_bounds,
                                     standard_name=standard_name,
                                     stored_direction=stored_direction,
                                     tolerance=str(tolerance),
                                     type=ctype,
                                     units=units,
                                     valid_max=str(valid_max),
                                     valid_min=str(valid_min),
                                     value=str(value),
                                     z_bounds_factors=z_bounds_factors,
                                     z_factors=z_factors,
                                     bounds_values=bounds_values,
                                     generic_level_name=generic_level_name,
                                     origin=origin)
    print("Added grid axis {}".format(name))

print("Create variable entries for grids")
for var in cfg.variable_entry.keys():
    print(cfg.variable_entry.__dict__[var].keys())
    long_name = cfg.variable_entry.__dict__[var].long_name                     \
                    if ('long_name' in cfg.variable_entry.__dict__[var].keys()) else ""
    standard_name = cfg.variable_entry.__dict__[var].standard_name                          \
                    if ('standard_name' in cfg.variable_entry.__dict__[var].keys())      else ""
    units     = cfg.variable_entry.__dict__[var].units                         \
                    if ('units' in cfg.variable_entry.__dict__[var].keys())     else ""
    dimensions = " ".join(cfg.variable_entry.__dict__[var].dimensions[:])                         \
                    if ('dimensions' in cfg.variable_entry.__dict__[var].keys())     else ""
    out_name  = cfg.variable_entry.__dict__[var].out_name                          \
                    if ('out_name' in cfg.variable_entry.__dict__[var].keys())      else ""
    valid_min = cfg.variable_entry.__dict__[var].valid_min                          \
                    if ('valid_min' in cfg.variable_entry.__dict__[var].keys())      else ""
    valid_max = cfg.variable_entry.__dict__[var].valid_max                          \
                    if ('valid_max' in cfg.variable_entry.__dict__[var].keys())      else ""
    vtype = cfg.variable_entry.__dict__[var].type                          \
                    if ('type' in cfg.variable_entry.__dict__[var].keys())      else ""


    cmd = """select label from CMORvar where label = '""" + str(name).strip() + "' and mipTable='grids';"
    c.execute(cmd)
    results = c.fetchall()
    if not results:
        gridVarEntries[var] = dict(long_name=long_name,
                                   standard_name=standard_name,
                                   units=units,
                                   dimensions=dimensions,
                                   out_name=out_name,
                                   valid_max=str(valid_max),
                                   valid_min=str(valid_min),
                                   type=vtype)
    print("Added grid variable {}".format(var))

with open('CMOR3_grid.json','w') as f:
    json.dump(dict(axis_entry=gridAxisEntries,variable_entry=gridVarEntries), f, indent=4, sort_keys=True)

c.close()