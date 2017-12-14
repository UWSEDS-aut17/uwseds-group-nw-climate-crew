import futurefish.model.fishmod_utils as fishmod_utils
import pandas as pd

stream_temp_file = "sites_streamflow_stream_temperature.csv"
site_info_file = "full_site_test_dataset.csv"
path = "../data/"

data_wea = pd.read_csv(path + stream_temp_file)
data_latlon = pd.read_csv(path + site_info_file)
data_latlon = data_latlon.iloc[:, 0:4]

data_wea00 = data_wea.ix[:, ["Site ID",
                             "Stream Temperature Historical",
                             "Streamflow Historical"]]
data_wea40 = data_wea.ix[:, ["Site ID",
                             "Stream Temperature 2040s",
                             "Streamflow 2040s"]]
data_wea80 = data_wea.ix[:, ["Site ID",
                             "Stream Temperature 2080s",
                             "Streamflow 2080s"]]

data_wea00 = data_wea00.assign(Decade='1993-2005')
data_wea40 = data_wea40.assign(Decade='2030-2059')
data_wea80 = data_wea80.assign(Decade='2070-2099')

data_wea00.columns = ["Site ID", "Temperature", "Streamflow", "Decade"]
data_wea40.columns = ["Site ID", "Temperature", "Streamflow", "Decade"]
data_wea80.columns = ["Site ID", "Temperature", "Streamflow", "Decade"]

data_wea00 = pd.merge(data_latlon, data_wea00)
data_wea40 = pd.merge(data_latlon, data_wea40)
data_wea80 = pd.merge(data_latlon, data_wea80)

# Temperature Model
# Streamt temperature historical
temp = data_wea00["Temperature"]
temp_vulnerability00 = fishmod_utils.temp_mod(temp,
                                              r_max=4,
                                              t_max=30,
                                              t_min=-5,
                                              t_opt=17.6)
# Stream temperature 2040s
temp = data_wea40["Temperature"]
temp_vulnerability40 = fishmod_utils.temp_mod(temp,
                                              r_max=4,
                                              t_max=30,
                                              t_min=-5,
                                              t_opt=17.6)
# Stream temperature 2080s
temp = data_wea80["Temperature"]
temp_vulnerability80 = fishmod_utils.temp_mod(temp,
                                              r_max=4,
                                              t_max=30,
                                              t_min=-5,
                                              t_opt=17.6)

# Streamflow Model

# Historical
flow = data_wea00["Streamflow"]
flow_vulnerability00_chinook = fishmod_utils.stream_mod(flow,
                                                        fo=424,
                                                        a=12818,
                                                        b=424)    # Chinook
flow_vulnerability00_sockeye = fishmod_utils.stream_mod(flow,
                                                        fo=390,
                                                        a=946,
                                                        b=390)    # Sockeye
flow_vulnerability00_coho = fishmod_utils.stream_mod(flow,
                                                     fo=362,
                                                     a=12124,
                                                     b=362)       # Coho
flow_vulnerability00_pink = fishmod_utils.stream_mod_pink(flow,
                                                          a_max=1052,
                                                          f_max=1200,
                                                          f_min=0,
                                                          f_opt=420) # Pink

# Stream flow 2040s
flow = data_wea40["Streamflow"]
flow_vulnerability40_chinook = fishmod_utils.stream_mod(flow,
                                                        fo=424,
                                                        a=12818,
                                                        b=424)    # Chinook
flow_vulnerability40_sockeye = fishmod_utils.stream_mod(flow,
                                                        fo=390,
                                                        a=946,
                                                        b=390)    # Sockeye
flow_vulnerability40_coho = fishmod_utils.stream_mod(flow,
                                                     fo=362,
                                                     a=12124,
                                                     b=362)       # Coho
flow_vulnerability40_pink = fishmod_utils.stream_mod_pink(flow,
                                                          a_max=1052,
                                                          f_max=1200,
                                                          f_min=0,
                                                          f_opt=420) # Pink

# stream flow 2080s
flow = data_wea80["Streamflow"]
flow_vulnerability80_chinook = fishmod_utils.stream_mod(flow,
                                                        fo=424,
                                                        a=12818,
                                                        b=424)    # Chinook
flow_vulnerability80_sockeye = fishmod_utils.stream_mod(flow,
                                                        fo=390,
                                                        a=946,
                                                        b=390)    # Sockeye
flow_vulnerability80_coho = fishmod_utils.stream_mod(flow,
                                                     fo=362,
                                                     a=12124,
                                                     b=362)       # Coho
flow_vulnerability80_pink = fishmod_utils.stream_mod_pink(flow,
                                                          a_max=1052,
                                                          f_max=1200,
                                                          f_min=0,
                                                          f_opt=420) # Pink

# Combining temperature & streamflow vulnerability projections
# assigning equal weight to each output

# Historical
chinook_vuln00 = pd.DataFrame(round(temp_vulnerability00 * 0.5 +
                                    flow_vulnerability00_chinook * 0.5))
sockeye_vuln00 = pd.DataFrame(round(temp_vulnerability00 * 0.5 +
                                    flow_vulnerability00_sockeye * 0.5))
coho_vuln00 = pd.DataFrame(round(temp_vulnerability00 * 0.5 +
                                 flow_vulnerability00_coho * 0.5))
pink_vuln00 = pd.DataFrame(round(temp_vulnerability00 * 0.5 +
                                 flow_vulnerability00_pink * 0.5))

# Year 2040s
chinook_vuln40 = pd.DataFrame(round(temp_vulnerability40 * 0.5 +
                                    flow_vulnerability40_chinook * 0.5))
sockeye_vuln40 = pd.DataFrame(round(temp_vulnerability40 * 0.5 +
                                    flow_vulnerability40_sockeye * 0.5))
coho_vuln40 = pd.DataFrame(round(temp_vulnerability40 * 0.5 +
                                 flow_vulnerability40_coho * 0.5))
pink_vuln40 = pd.DataFrame(round(temp_vulnerability40 * 0.5 +
                                 flow_vulnerability40_pink * 0.5))

# Year 2080s
chinook_vuln80 = pd.DataFrame(round(temp_vulnerability80 * 0.5 +
                                    flow_vulnerability80_chinook * 0.5))
sockeye_vuln80 = pd.DataFrame(round(temp_vulnerability80 * 0.5 +
                                    flow_vulnerability80_sockeye * 0.5))
coho_vuln80 = pd.DataFrame(round(temp_vulnerability80 * 0.5 +
                                 flow_vulnerability80_coho * 0.5))
pink_vuln80 = pd.DataFrame(round(temp_vulnerability80 * 0.5 +
                                 flow_vulnerability80_pink * 0.5))

# Combining all model outputs to a dataframe
# Make a sub-dataframe for each species - historical

# Chinook
chinook_00 = data_wea00
chinook_00 = chinook_00.assign(Species='Chinook')
chinook_00["Viability"] = chinook_vuln00
# Sockeye
sockeye_00 = data_wea00
sockeye_00 = sockeye_00.assign(Species='Sockeye')
sockeye_00["Viability"] = sockeye_vuln00
# Coho
coho_00 = data_wea00
coho_00 = coho_00.assign(Species='Coho')
coho_00["Viability"] = coho_vuln00
# Pink
pink_00 = data_wea00
pink_00 = pink_00.assign(Species='Pink')
pink_00["Viability"] = pink_vuln00

# make a sub-dataframe for each species - 40s

# Chinook
chinook_40 = data_wea40
chinook_40 = chinook_40.assign(Species='Chinook')
chinook_40["Viability"] = chinook_vuln40
# Sockeye
sockeye_40 = data_wea40
sockeye_40 = sockeye_40.assign(Species='Sockeye')
sockeye_40["Viability"] = sockeye_vuln40
# Coho
coho_40 = data_wea40
coho_40 = coho_40.assign(Species='Coho')
coho_40["Viability"] = coho_vuln40
# Pink
pink_40 = data_wea40
pink_40 = pink_40.assign(Species='Pink')
pink_40["Viability"] = pink_vuln40

# make a sub-dataframe for each species - 80s

# Chinook
chinook_80 = data_wea80
chinook_80 = chinook_80.assign(Species='Chinook')
chinook_80["Viability"] = chinook_vuln80
# Sockeye
sockeye_80 = data_wea80
sockeye_80 = sockeye_80.assign(Species='Sockeye')
sockeye_80["Viability"] = sockeye_vuln80
# Coho
coho_80 = data_wea80
coho_80 = coho_80.assign(Species='Coho')
coho_80["Viability"] = coho_vuln80
# Pink
pink_80 = data_wea80
pink_80 = pink_80.assign(Species='Pink')
pink_80["Viability"] = pink_vuln80

# Merging output
fish_vulnerability_00 = chinook_00.append(sockeye_00). \
                                   append(coho_00). \
                                   append(pink_00)
fish_vulnerability_40 = chinook_40.append(sockeye_40). \
                                   append(coho_40). \
                                   append(pink_40)
fish_vulnerability_80 = chinook_80.append(sockeye_80). \
                                   append(coho_80). \
                                   append(pink_80)
fish_vulnerability = fish_vulnerability_00. \
                     append(fish_vulnerability_40). \
                     append(fish_vulnerability_80)

fish_vulnerability.to_csv("../data/fish_vulnerability_new.csv")
