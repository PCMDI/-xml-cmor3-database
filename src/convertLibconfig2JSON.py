
import pylibconfig2 as cfg
import json

formulaVars = {}
axisVars = {}

files = ["../tables/Amon_libconfig", "CMIP5_Omon_CMOR3", "CMIP5_formula_CMOR3", 
         "./CMIP5_Omon_CMOR3", "./CMIP6_OImon_CMOR3", "./CMIP6_LImon_CMOR3",
         "./CMIP6_Lmon_CMOR3", "./CMIP5_3hr_CMOR3",
         "./CMIP5_cfSites_CMOR3", "./CMIP5_cf3hr_CMOR3", "./CMIP5_cfMon_CMOR3"]
for file in files:
    cmor2 = cfg.Config()
    cmor2.read_file(file)
    # Add formula variables
    #
    formulaVar = [key for key in cmor2.variable_entry.keys()
                   if cmor2.variable_entry.__dict__[key].long_name.find("formula") != -1]
    variables = [key for key in cmor2.axis_entries.keys() if hasattr(cmor2.axis_entries.__dict__[key], 'z_factors')]

    z_bnds     = {key for var in variables for key in
                  cmor2.axis_entries.__dict__[var].z_bounds_factors.split(" ")
                  if key.find(':') == -1
                  if key in cmor2.variable_entry.__dict__.keys()}
    z_factors  = {key for var in variables for key in
                  cmor2.axis_entries.__dict__[var].z_factors.split(" ")
                  if key.find(':') == -1
                  if key in cmor2.variable_entry.__dict__.keys()}

    z_factors.update(z_bnds)

    formulaVar = list(z_factors)
    print("Create formula variables")
    for var in formulaVar:
        name = var
        long_name = cmor2.variable_entry.__dict__[var].long_name           \
                        if ('long_name' in
                            cmor2.variable_entry.__dict__[var].keys()) else ""
        ctype     = cmor2.variable_entry.__dict__[var].type                 \
                        if ('type' in
                            cmor2.variable_entry.__dict__[var].keys()) else ""
        dimension = " ".join(cmor2.variable_entry.__dict__[var].dimensions[:])\
                        if ('dimensions' in
                            cmor2.variable_entry.__dict__[var].keys()) else ""
        units     = cmor2.variable_entry.__dict__[var].units                \
                        if ('units' in
                            cmor2.variable_entry.__dict__[var].keys()) else ""
        out_name     = cmor2.variable_entry.__dict__[var].out_name          \
                        if ('out_name' in
                            cmor2.variable_entry.__dict__[var].keys()) else name

        print(out_name)
        if name not in formulaVars.keys():
            formulaVars[name] = dict(name=name,
                                     long_name=long_name,
                                     type=ctype,
                                     dimension=dimension,
                                     out_name=out_name,
                                     units=units)
        else:
            print("{} already in formulaVar".format(name))

    print("Create axes")
    for axis in cmor2.axis_entries.keys():
        #
        #    for item in cmor2.axis_entries.__getattribute__(axis).keys():
        #        print item
        #
        name               = axis
        caxis              = cmor2.axis_entries.__getattribute__(axis).__getattribute__('axis')             \
                               if ('axis'             in cmor2.axis_entries.__getattribute__(axis).keys())     else ""
        climatology        = cmor2.axis_entries.__getattribute__(axis).__getattribute__('climatology')      \
                               if ('climatology'      in cmor2.axis_entries.__getattribute__(axis).keys())     else ""
        formula            = cmor2.axis_entries.__getattribute__(axis).__getattribute__('formula')          \
                               if ('formula'          in cmor2.axis_entries.__getattribute__(axis).keys())     else ""
        long_name          = cmor2.axis_entries.__getattribute__(axis).__getattribute__('long_name')        \
                               if ('long_name'        in cmor2.axis_entries.__getattribute__(axis).keys())     else ""
        must_have_bounds   = cmor2.axis_entries.__getattribute__(axis).__getattribute__('must_have_bounds') \
                               if ('must_have_bounds' in cmor2.axis_entries.__getattribute__(axis).keys())     else ""
        out_name           = cmor2.axis_entries.__getattribute__(axis).__getattribute__('out_name')         \
                               if ('out_name'       in cmor2.axis_entries.__getattribute__(axis).keys())       else ""
        positive           = cmor2.axis_entries.__getattribute__(axis).__getattribute__('positive').strip()         \
                               if ('positive'       in cmor2.axis_entries.__getattribute__(axis).keys())       else ""
        requested          = cmor2.axis_entries.__getattribute__(axis).__getattribute__('requested')        \
                               if ('requested'      in cmor2.axis_entries.__getattribute__(axis).keys())       else ""
        requested_bounds   = cmor2.axis_entries.__getattribute__(axis).__getattribute__('requested_bounds')        \
                               if ('requested_bounds'  in cmor2.axis_entries.__getattribute__(axis).keys())    else ""
        standard_name      = cmor2.axis_entries.__getattribute__(axis).__getattribute__('standard_name')    \
                               if ('standard_name'  in cmor2.axis_entries.__getattribute__(axis).keys())       else ""
        stored_direction   = cmor2.axis_entries.__getattribute__(axis).__getattribute__('stored_direction') \
                               if ('stored_direction' in cmor2.axis_entries.__getattribute__(axis).keys())     else ""
        tolerance          = cmor2.axis_entries.__getattribute__(axis).__getattribute__('tolerance')        \
                               if ('tolerance' in cmor2.axis_entries.__getattribute__(axis).keys())            else ""
        ctype              = cmor2.axis_entries.__getattribute__(axis).__getattribute__('type')             \
                               if ('type'      in cmor2.axis_entries.__getattribute__(axis).keys())            else ""
        units              = cmor2.axis_entries.__getattribute__(axis).__getattribute__('units')            \
                               if ('units'     in cmor2.axis_entries.__getattribute__(axis).keys())            else ""
        valid_max          = cmor2.axis_entries.__getattribute__(axis).__getattribute__('valid_max')        \
                               if ('valid_max' in cmor2.axis_entries.__getattribute__(axis).keys())            else ""
        valid_min          = cmor2.axis_entries.__getattribute__(axis).__getattribute__('valid_min')        \
                               if ('valid_min' in cmor2.axis_entries.__getattribute__(axis).keys())            else ""
        value              = cmor2.axis_entries.__getattribute__(axis).__getattribute__('value')            \
                               if ('value'     in cmor2.axis_entries.__getattribute__(axis).keys())            else ""
        z_bounds_factors   = cmor2.axis_entries.__getattribute__(axis).__getattribute__('z_bounds_factors') \
                               if ('z_bounds_factors'    in cmor2.axis_entries.__getattribute__(axis).keys())  else ""
        z_factors          = cmor2.axis_entries.__getattribute__(axis).__getattribute__('z_factors')        \
                               if ('z_factors' in cmor2.axis_entries.__getattribute__(axis).keys())            else ""
        bounds_values      = cmor2.axis_entries.__getattribute__(axis).__getattribute__('bounds_values')    \
                               if ('bounds_values' in cmor2.axis_entries.__getattribute__(axis).keys())        else ""
        generic_level_name = cmor2.axis_entries.__getattribute__(axis).__getattribute__('generic_level_name')    \
                               if ('generic_level_name' in cmor2.axis_entries.__getattribute__(axis).keys())        else "" 

        if name not in axisVars.keys():
            origin = file.split("_")[1]
            axisVars[name] = dict(name=name,       
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
                                  tolerance=tolerance,
                                  type=ctype,
                                  units=units,
                                  valid_max=valid_max,
                                  valid_min=valid_min,
                                  value=value,
                                  z_bounds_factors=z_bounds_factors,
                                  z_factors=z_factors,
                                  bounds_values=bounds_values,
                                  generic_level_name=generic_level_name,
                                  origin=origin)
            print("Added axis {}".format(name))
        else:
            print("{} already in axisEntry".format(name))

cmor2 = cfg.Config()
cmor2.read_file("./CMIP5_grids_CMOR3")
print("Create axes for grids")
for axis in cmor2.axis_entry.keys():
    print("FROM CMIP5_grids_CMOR3",axis)
    name               = axis
    caxis              = cmor2.axis_entry.__getattribute__(axis).__getattribute__('axis')             \
                           if ('axis'             in cmor2.axis_entry.__getattribute__(axis).keys())     else ""
    climatology        = cmor2.axis_entry.__getattribute__(axis).__getattribute__('climatology')      \
                           if ('climatology'      in cmor2.axis_entry.__getattribute__(axis).keys())     else ""
    formula            = cmor2.axis_entry.__getattribute__(axis).__getattribute__('formula')          \
                           if ('formula'          in cmor2.axis_entry.__getattribute__(axis).keys())     else ""
    long_name          = cmor2.axis_entry.__getattribute__(axis).__getattribute__('long_name')        \
                           if ('long_name'        in cmor2.axis_entry.__getattribute__(axis).keys())     else ""
    must_have_bounds   = cmor2.axis_entry.__getattribute__(axis).__getattribute__('must_have_bounds') \
                           if ('must_have_bounds' in cmor2.axis_entry.__getattribute__(axis).keys())     else ""
    out_name           = cmor2.axis_entry.__getattribute__(axis).__getattribute__('out_name')         \
                           if ('out_name'       in cmor2.axis_entry.__getattribute__(axis).keys())       else ""
    positive           = cmor2.axis_entry.__getattribute__(axis).__getattribute__('positive').strip()         \
                           if ('positive'       in cmor2.axis_entry.__getattribute__(axis).keys())       else ""
    requested          = cmor2.axis_entry.__getattribute__(axis).__getattribute__('requested')        \
                           if ('requested'      in cmor2.axis_entry.__getattribute__(axis).keys())       else ""
    requested_bounds   = cmor2.axis_entry.__getattribute__(axis).__getattribute__('requested_bounds')        \
                           if ('requested_bounds'  in cmor2.axis_entry.__getattribute__(axis).keys())  else ""
    standard_name      = cmor2.axis_entry.__getattribute__(axis).__getattribute__('standard_name')    \
                           if ('standard_name'  in cmor2.axis_entry.__getattribute__(axis).keys())       else ""
    stored_direction   = cmor2.axis_entry.__getattribute__(axis).__getattribute__('stored_direction') \
                           if ('stored_direction' in cmor2.axis_entry.__getattribute__(axis).keys())     else ""
    tolerance          = cmor2.axis_entry.__getattribute__(axis).__getattribute__('tolerance')        \
                           if ('tolerance' in cmor2.axis_entry.__getattribute__(axis).keys())            else ""
    ctype              = cmor2.axis_entry.__getattribute__(axis).__getattribute__('type')             \
                           if ('type'      in cmor2.axis_entry.__getattribute__(axis).keys())            else ""
    units              = cmor2.axis_entry.__getattribute__(axis).__getattribute__('units')            \
                           if ('units'     in cmor2.axis_entry.__getattribute__(axis).keys())            else ""
    valid_max          = cmor2.axis_entry.__getattribute__(axis).__getattribute__('valid_max')        \
                           if ('valid_max' in cmor2.axis_entry.__getattribute__(axis).keys())            else ""
    valid_min          = cmor2.axis_entry.__getattribute__(axis).__getattribute__('valid_min')        \
                           if ('valid_min' in cmor2.axis_entry.__getattribute__(axis).keys())            else ""
    value              = cmor2.axis_entry.__getattribute__(axis).__getattribute__('value')            \
                           if ('value'     in cmor2.axis_entry.__getattribute__(axis).keys())            else ""
    z_bounds_factors   = cmor2.axis_entry.__getattribute__(axis).__getattribute__('z_bounds_factors') \
                           if ('z_bounds_factors'    in cmor2.axis_entry.__getattribute__(axis).keys())  else ""
    z_factors          = cmor2.axis_entry.__getattribute__(axis).__getattribute__('z_factors')        \
                           if ('z_factors' in cmor2.axis_entry.__getattribute__(axis).keys())            else ""
    bounds_values      = cmor2.axis_entry.__getattribute__(axis).__getattribute__('bounds_values')    \
                           if ('bounds_values' in cmor2.axis_entry.__getattribute__(axis).keys())        else ""
    generic_level_name = ""

    if name not in axisVars.keys():
        origin = 'grid'
        axisVars[name] = dict(name=name,       
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
                              tolerance=tolerance,
                              type=ctype,
                              units=units,
                              valid_max=valid_max,
                              valid_min=valid_min,
                              value=value,
                              z_bounds_factors=z_bounds_factors,
                              z_factors=z_factors,
                              bounds_values=bounds_values,
                              generic_level_name=generic_level_name,
                              origin=origin)
        print("Added axis {}".format(name))
    else:
        print("{} already in axisEntry".format(name))
            
with open('CMOR3_formula_terms.json','w') as f:
    json.dump(formulaVars, f, indent=4, sort_keys=True)

with open('CMOR3_axes.json','w') as f:
    json.dump(axisVars, f, indent=4, sort_keys=True)
