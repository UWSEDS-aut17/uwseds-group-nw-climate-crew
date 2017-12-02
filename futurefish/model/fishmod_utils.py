import pandas as pd

def temp_mod(temp, r_max, t_max, t_min, t_opt):
    """Reads in stream temperature.
    Outputs fish growth vulnerability on a scale of 1-5.
    1 being the most vulnerable.
    """
    output = r_max*((t_max-temp)/(t_max-t_opt))*((temp-t_min)/(t_opt-t_min))**((t_opt-t_min)/(t_max-t_opt))
    output = pd.DataFrame(output)
    output.columns = ["growth_rate"]
    output[(output<0)] = 1
    output[(output>0) & (output<(r_max/4))] = 2
    output[(output>(r_max/4)) & (output<(r_max/4)*2)] = 3
    output[(output>(r_max/4)*2) & (output<(r_max/4)*3)] = 4
    output[(output>(r_max/4)*3)] = 5
    temp_vulnerability = output["growth_rate"]
    print("model output = temp_vulnerability")
    return temp_vulnerability
    
def stream_mod(flow, fo, a, b):
    """Reads in stram flow. 
    Outputs fish spawn area vulnerability on a scale of 1-5.
    1 being the most vulnerable.
    This model relationship only applies to slamon species: Chinook, Sockeye and Coho.
    """
    output = a/(1+((flow-fo)/b)**2)
    output = pd.DataFrame(output)
    output.columns = ["spawn_area"]
    output[(output<(a/5))] = 1
    output[(output>(a/5)) & (output<(a/5)*2)] = 2
    output[(output>(a/5)*2) & (output<(a/5)*3)] = 3
    output[(output>(a/5)*3) & (output<(a/5)*4)] = 4
    output[(output>(a/5)*4)] = 5
    flow_vulnerability = output["spawn_area"]
    print("model output = flow_vulnerability")
    return flow_vulnerability

def stream_mod_pink(flow, a_max, f_max, f_min, f_opt):
    """Reads in stream flow.
    Outputs fish spawn area vulnerability on a scale of 1-5.
    1 being the most vulnerable.
    This model relationship only applies to pink salmon.
    """
    output = a_max*((f_max-flow)/(f_max-f_opt))*((flow-f_min)/(f_opt-f_min))**((f_opt-f_min)/(f_max-f_opt))
    output = pd.DataFrame(output)
    output.columns = ["spawn_area"]
    output[(output<(f_max/5))] = 1
    output[(output>(f_max/5)) & (output<(f_max/5)*2)] = 2
    output[(output>(f_max/5)*2) & (output<(f_max/5)*3)] = 3
    output[(output>(f_max/5)*3) & (output<(f_max/5)*4)] = 4
    output[(output>(f_max/5)*4)] = 5
    flow_vulnerability_pink = output["spawn_area"]
    print("model output = flow_vulnerability_pink")
    return flow_vulnerability_pink

    
    
    
    
    
    
    
    