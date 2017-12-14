import os
import itertools
import pandas as pd


def temp_vulnerability(temp, r_max, t_max, t_min, t_opt):
    """
    Determine vulnerability index based on temperature.
    Vulnerability scale goes from 1 to 5 with 1 being
    the most vulnerable and 5 being the least.

    Input
    -----
    temp (pd.Series): Temperature (C)
    r_max (float): Parameter
    t_max (float): Maximum temp parameter
    t_min (float): Minimum temp parameter
    t_opt (float): Optimal temp parameter

    Output
    ------
    temp_vulnerability (pd.Series): Index of vulnerability
        due to input temperatures.
    """
    output = (r_max
              * ((t_max - temp) / (t_max - t_opt))
              * ((temp - t_min) / (t_opt - t_min))
              ** ((t_opt - t_min) / (t_max - t_opt)))
    output = pd.DataFrame(output)
    output.columns = ["growth_rate"]
    output[(output < 0)] = 1
    output[(output > 0) & (output < (r_max / 4))] = 2
    output[(output > (r_max / 4)) & (output < (r_max / 4) * 2)] = 3
    output[(output > (r_max / 4) * 2) & (output < (r_max / 4) * 3)] = 4
    output[(output > (r_max / 4) * 3)] = 5
    temp_vulnerability = output["growth_rate"]
    return temp_vulnerability


def flow_vulnerability(flow, fo, a, b):
    """
    Determine vulnerability index based on temperature.
    Vulnerability scale goes from 1 to 5 with 1 being
    the most vulnerable and 5 being the least.

    Input
    -----
    flow (pd.Series): Streamflow discharge (CFS)
    fo (float): Flow parameter
    a (float): Parameter
    b (float): Parameter

    Output
    ------
    flow_vulnerability (pd.Series): Index of vulnerability
        due to input flow rates.
    """
    output = a / (1 + ((flow - fo) / b) ** 2)
    output = pd.DataFrame(output)
    output.columns = ["spawn_area"]
    output[(output < (a / 5))] = 1
    output[(output > (a / 5)) & (output < (a / 5) * 2)] = 2
    output[(output > (a / 5) * 2) & (output < (a / 5) * 3)] = 3
    output[(output > (a / 5) * 3) & (output < (a / 5) * 4)] = 4
    output[(output > (a / 5) * 4)] = 5
    flow_vulnerability = output["spawn_area"]
    return flow_vulnerability


def flow_vulnerability_pink(flow, a_max, f_max, f_min, f_opt):
    """
    Determine vulnerability index for pink salmon based on flow.
    Vulnerability scale goes from 1 to 5 with 1 being
    the most vulnerable and 5 being the least.

    Input
    -----
    temp (pd.Series): Temperature (C)
    a_max (float): Parameter
    f_max (float): Maximum flow parameter
    f_min (float): Minimum flow parameter
    f_opt (float): Optimal flow parameter

    Output
    ------
    flow_vulnerability (pd.Series): Index of vulnerability
        due to input temperatures.
   """
    output = (a_max
              * ((f_max - flow) / (f_max - f_opt))
              * ((flow - f_min) / (f_opt - f_min))
              ** ((f_opt - f_min) / (f_max - f_opt)))
    output = pd.DataFrame(output)
    output.columns = ["spawn_area"]
    output[(output < (f_max / 5))] = 1
    output[(output > (f_max / 5)) & (output < (f_max / 5) * 2)] = 2
    output[(output > (f_max / 5) * 2) & (output < (f_max / 5) * 3)] = 3
    output[(output > (f_max / 5) * 3) & (output < (f_max / 5) * 4)] = 4
    output[(output > (f_max / 5) * 4)] = 5
    flow_vulnerability_pink = output["spawn_area"]
    return flow_vulnerability_pink


def viability(df, specie, flow_params, temp_params):
    """
    Calculate the joint vulnerabilty for a species and time period
    """
    df = df.assign(Species=specie)
    temp_vuln = temp_vulnerability(df['Temperature'], **temp_params)
    if specie != 'Pink':
        flow_vuln = flow_vulnerability(df['Streamflow'], **flow_params)
    else:
        flow_vuln = flow_vulnerability_pink(df['Streamflow'], **flow_params)
    return pd.DataFrame(round(0.5*temp_vuln + 0.5*flow_vuln))


def run_model(out_file=None):
    """
    Run full fish viability model
    """
    PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    temp_file = os.path.join(PATH, "sites_streamflow_stream_temperature.csv")
    info_file = os.path.join(PATH, "full_site_test_dataset.csv")

    data_wea = pd.read_csv(temp_file)
    data_latlon = pd.read_csv(info_file).iloc[:, 0:4]

    # Parameters
    temp_params = dict(r_max=4, t_max=30, t_min=-5, t_opt=17.6)
    chinook_params = dict(fo=424, a=12818, b=424)
    sockeye_params = dict(fo=390, a=946, b=390)
    coho_params = dict(fo=362, a=12124, b=362)
    pink_params = dict(a_max=1052, f_max=1200, f_min=0, f_opt=420)
    species = ['Chinook', 'Sockeye', 'Coho', 'Pink']
    params_list = [chinook_params, sockeye_params, coho_params, pink_params]

    # Decade parameters
    ix_historical = ["Site ID", "Stream Temperature Historical",
                     "Streamflow Historical"]
    decade_historical = '1993-2005'
    ix_2040 = ["Site ID", "Stream Temperature 2040s", "Streamflow 2040s"]
    decade_2040 = '2030-2059'
    ix_2080 = ["Site ID", "Stream Temperature 2080s", "Streamflow 2080s"]
    decade_2080 = '2070-2099'
    decade_list = [decade_historical, decade_2040, decade_2080]
    ix_list = [ix_historical, ix_2040, ix_2080]
    df_total = pd.DataFrame()
    for ix, dec in zip(ix_list, decade_list):
        dec_df = data_wea.ix[:, ix].assign(Decade=dec)
        dec_df.columns = ["Site ID", "Temperature", "Streamflow", "Decade"]
        dec_df = pd.merge(data_latlon, dec_df)
        for spec, params in zip(species, params_list):
            dec_df = dec_df.assign(Species=spec)
            dec_df['Viability'] = viability(dec_df, spec, params, temp_params)
        df_total = df_total.append(dec_df)
    if out_file:
        df_total.to_csv(out_file)
    return df_total
