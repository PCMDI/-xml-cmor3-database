# ==================
# JSON Template
# ==================
HeaderJSON = """
{
    "Header":{
                    "data_specs_version": "<data_specs_version>",
                    "cmor_version":     "<cmorVersion>",
                    "table_id":         "Table <table>",
                    "realm":            "<modeling_realm>",
                    "table_date":       "<tableDate>",
                    "missing_value":    "<missingValue>",
                    "int_missing_value": "-999",
                    "product":          "model-output",
                    "approx_interval":  "<approxInterval>",
                    <DUMMYENTRY>
                    "generic_levels":   "<generic_levels>",
                    "mip_era":          "CMIP6",
                    "Conventions":      "CF-1.7 CMIP-6.2"
              },
"""

axisTemplateJSON = """
"<axis_entry>": {
                    "standard_name":    "<standard_name>",
                    "units":            "<units>",
                    "axis":             "<axis>",
                    "long_name":        "<long_name>",
                    "climatology":      "<climatology>",
                    "formula":          "<formula>",
                    "must_have_bounds": "<must_have_bounds>",
                    "out_name":         "<out_name>",
                    "positive":         "<positive>",
                    "requested":        <requested>,
                    "requested_bounds": <requested_bounds>,
                    "stored_direction":  "<stored_direction>",
                    "tolerance":        "<tolerance>",
                    "type":             "<type>",
                    "valid_max":        "<valid_max>",
                    "valid_min":        "<valid_min>",
                    "value":            "<value>",
                    "z_bounds_factors": "<z_bounds_factors>",
                    "z_factors":        "<z_factors>",
                    "bounds_values":    "<bounds_values>",
                    "generic_level_name": "<generic_level_name>"
                },
"""
FormulaVarTemplateJSON = """
"<variable_entry>": {
                        "long_name":   "<long_name>",
                        "units":       "<units>",
                        "dimensions":  "<dimensions>",
                        "out_name":    "<out_name>",
                        "standard_name":    "<standard_name>",
                        "type":        "<type>"
                    },
"""

VarTemplateJSON = """
"<variable_entry>": {
                        "frequency":         "<frequency>",
                        "modeling_realm":    "<modeling_realm>",
                        "standard_name":     "<standard_name>",
                        "units":             "<units>",
                        "cell_methods":      "<cell_methods>",
                        "cell_measures":     "<cell_measure>",
                        "long_name":         "<long_name>",
                        "comment":           "<comment>",
                        "dimensions":        "<dimensions>",
                        "out_name":          "<outname>",
                        "type":              "<type>",
                        "positive":          "<positive>",
                        "valid_min":         "<valid_min>",
                        "valid_max":         "<valid_max>",
                        "flag_values":       "<flag_values>",
                        "flag_meanings":     "<flag_meanings>",
                        "ok_min_mean_abs":   "<ok_min_mean_abs>",
                        "ok_max_mean_abs":   "<ok_max_mean_abs>"
},
"""


GridHeaderJSON = """
{
    "Header":{
                "data_specs_version": "<data_specs_version>",
                "table_id": "Table grids",
                "cmor_version":  "<cmorVersion>",
                "table_date":    "<tableDate>",
                "missing_value": "<missingValue>",
                "product": "output",
                "Conventions":      "CF-1.7 CMIP-6.2"
             },

    "mapping_entry": {
                "sample_user_mapping": {
                            "parameter1": "false_easting",
                            "parameter2": "false_northing",
                            "coordinates": "rlon rlat"
                                       }
             },
"""

GridVarTemplateJSON = """
"<grid_variable_entry>": {
                        "standard_name":     "<standard_name>",
                        "units":             "<units>",
                        "long_name":         "<long_name>",
                        "dimensions":        "<dimensions>",
                        "out_name":          "<out_name>",
                        "valid_min":         "<valid_min>",
                        "valid_max":         "<valid_max>",
                        "type":              "<type>"
                         },
"""
GridAxisTemplateJSON = """
"<grid_axis_entry>": {
                    "standard_name":    "<standard_name>",
                    "units":            "<units>",
                    "axis":             "<axis>",
                    "long_name":        "<long_name>",
                    "out_name":         "<out_name>",
                    "type":             "<type>"
                },
"""


FooterTemplateJSON="""
}
"""
# ==================
#  Header information
# ==================
tableDict = { "Amon": { "approxInterval" : "30.00000", 
                        "genericLevels"  : "alevel alevhalf"
                      },
            "AERmonZ": { "approxInterval" : "30.00000", 
                        "genericLevels"  : "alevel alevhalf"
                      },
            "AERmon": { "approxInterval" : "30.00000", 
                        "genericLevels"  : "alevel alevhalf"
                      },
            "AERday": { "approxInterval" : "1.0", 
                        "genericLevels"  : ""
                      },
            "AERhr": { "approxInterval" : "0.041667", 
                        "genericLevels"  : "alevel alevhalf"
                      },
              "Lmon": { "approxInterval" : "30.00000",
                        "genericLevels"  : ""
                      },
              "LImon": { "approxInterval" : "30.00000",
                        "genericLevels"  : ""
                      },
              "CFmon": { "approxInterval" : "30.00000",
                        "genericLevels"  : "alevel alevhalf"
                      },
              "Omon": { "approxInterval" : "30.00000",
                        "genericLevels"  : "olevel olevhalf"
                      },
              "SImon": { "approxInterval" : "30.00000",
                        "genericLevels"  : ""
                      },
              "Oclim": { "approxInterval" : "30.00000",
                        "genericLevels"  : "olevel olevhalf"
                      },
              "Oyr": { "approxInterval" : "365.00000",
                        "genericLevels"  : "olevel"
                      },
              "SIday":  { "approxInterval" : "1.00000",
                        "genericLevels"  : ""
                      },
              "Oday":  { "approxInterval" : "1.00000",
                        "genericLevels"  : "olevel"
                      },
             "CFday":  { "approxInterval" : "1.00000",
                        "genericLevels"  : "alevel alevhalf",
                      },
              "day":  { "approxInterval" : "1.00000",
                        "genericLevels"  : ""
                      },
            "E3hrPt":  { "approxInterval" : "0.125000",
                        "genericLevels"  : "alevel alevhalf",
                      },
       "E1hrClimMon":  { "approxInterval" : "0.041667",
                        "genericLevels"  : ""
                      },
             "E1hr":  { "approxInterval" : "0.041667",
                        "genericLevels"  : ""
                      },
             "E3hr":  { "approxInterval" : "0.125000",
                        "genericLevels"  : "alevel alevhalf"
                      },
            "CF3hr":  { "approxInterval" : "0.125000",
                        "genericLevels"  : "alevel alevhalf"
                      },
              "3hr":  { "approxInterval" : "0.125000",
                        "genericLevels"  : ""
                      },
            "E6hrZ":  { "approxInterval" : "0.250000",
                        "genericLevels"  : "alevel alevhalf"
                      },
           "6hrLev":  { "approxInterval" : "0.250000",
                        "genericLevels"  : "alevel alevhalf"
                      },
          "6hrPlev":  { "approxInterval" : "0.250000",
                        "genericLevels"  : ""
                      },
           "CFsubhr": { "approxInterval" : "0.017361",
                        "genericLevels"  : "alevel alevhalf",
                        "approxIntervalWarning" : "0.5",
                        "approxIntervalError" : "0.90"
                      },
            "Esubhr": { "approxInterval" : "0.017361",
                        "genericLevels"  : "alevel alevhalf",
                        "approxIntervalWarning" : "0.5",
                        "approxIntervalError" : "0.90"
                      },
             "IyrGre": { "approxInterval" : "365.00",
                            "genericLevels"  : ""
                      },
             "IyrAnt": { "approxInterval" : "365.00",
                            "genericLevels"  : ""
                      },
             "ImonGre": { "approxInterval" : "30.00",
                            "genericLevels"  : ""
                      },
             "ImonAnt": { "approxInterval" : "30.00",
                            "genericLevels"  : ""
                      },
             "Eyr": { "approxInterval" : "365",
                            "genericLevels"  : "alevel olevel"
                      },
             "Efx": { "approxInterval" : "0.00000",
                            "genericLevels"  : "alevhalf"
                      },
              "fx": { "approxInterval" : "0.00000",
                            "genericLevels"  : "alevel"
                      },
              "6hrPlevPt": { "approxInterval" : "0.250000",
                            "genericLevels"  : ""
                       },
             "EdayZ": { "approxInterval" : "1.00000",
                                    "genericLevels"  : ""
                       },
              "Eday": { "approxInterval" : "1.00000",
                                    "genericLevels"  : ""
                       },
           "EmonZ": { "approxInterval" : "30.00000",
                                    "genericLevels"  : "alevel olevel"
                       },
            "Emon": { "approxInterval" : "30.00000",
                                    "genericLevels"  : "alevel olevel"
                       },
            "Ofx": { "approxInterval" : "0.00000",
                                    "genericLevels"  : "olevel"
                       },
            "Odec": { "approxInterval" : "3650.00000",
                                    "genericLevels"  : "olevel"
                       }
             }

# ==================
#  Old CMOR2 format
# ==================
Header = """
table_id: "Table <table>"
modeling_realm: "<modeling_realm>"

frequency:  "<frequency>"

cmor_version: <cmorVersion>  # minimum version of CMOR that can read this table
cf_version:   <cfVersion>    # version of CF that output conforms to
activity_id:   "<activityID>"    # project id
table_date:   "<tableDate>"   # date this table was constructed

missing_value: <missingValue>    # value used to indicate a missing value
                                 #   in arrays output by netCDF as 32-bit IEEE
                                 #   floating-point numbers (float or real)

baseURL: "http://cmip-pcmdi.llnl.gov/CMIP6/dataLocation"
product: "output"

# space separated required global attribute

required_global_attributes: [ "creation_date","tracking_id","forcing","model_id","parent_experiment_id","parent_experiment_rip","branch_time","contact","institute_id" ]    

forcings:   "N/A Nat Ant GHG SD SI SA TO SO Oz LU Sl Vl SS Ds BC MD OC AA"

approx_interval:  <approxInterval> # approximate spacing between successive time
                          #   samples (in units of the output time
                          #   coordinate.select distinct mip,label,description from experiment order by mip;

generic_levels:   "<generic_levels>";
"""
# ==================
axisTemplate = """
!===============
axis_entry: <axis_entry>
!===============

!----------------------------------
! Axis attributes:
!----------------------------------
standard_name:    <standard_name>
units:            <units>
axis:             <axis>
long_name:        <long_name>
!----------------------------------
! Additional axis information:
!----------------------------------
climatology:      <climatology>
formula:          <formula>
must_have_bounds: <must_have_bounds>
out_name:         <out_name>
positive:         <positive>
requested:        <requested>
requested_bounds: <requested_bounds>
stored_direction: <stored_direction>
tolerance:        <tolerance>
type:             <type>
valid_max:        <valid_max>
valid_min:        <valid_min>
value:            <value>
z_bounds_factors: <z_bounds_factors>
z_factors:        <z_factors>
generic_level_name: <generic_level_name>
"""


FormulaVarTemplate = """
!===============
variable_entry: <variable_entry>
!===============

!----------------------------------
! Variable attributes:
!----------------------------------
long_name:   <long_name>
units:       <units>
!----------------------------------
! Additional variable information:
!----------------------------------
dimensions:  <dimensions>
type:        <type>
!----------------------------------
"""

VarTemplate = """
!===============
variable_entry:  <variable_entry>
!===============

modeling_realm:    <modeling_realm>
!----------------------------------
! Variable attributes:
!----------------------------------
standard_name:     <standard_name>
units:             <units>
cell_methods:      <cell_methods>
cell_measures:     <cell_measure>
long_name:         <long_name>
comment:           <comment>
!----------------------------------
! Additional variable information:
!----------------------------------
dimensions:        <dimensions>
out_name:          <outname>
type:              <type>
positive:          <positive>
valid_min:         <valid_min>
valid_max:         <valid_max>
ok_min_mean_abs:   <ok_min_mean_abs>
ok_max_mean_abs:   <ok_max_mean_abs>
"""


