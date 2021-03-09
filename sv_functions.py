#----- Package for the notebook Sverdrup_critical_depth ------#

import numpy as np

# find I_z for each day (which is the index of I_e)

def Iz(z,I_e, k):
    """
    z = depth array
    I_e = energy through surface, per day
    k= extinction coeff'
    """
    exp_val = np.exp(-k*z)
    
    vals = np.dot(I_e[:,None],exp_val[None]).ravel()
    
    return np.reshape(vals, (-1,500))

# find h (solar elevation (deg)). just for solar noon

def high_noon(latitude, time=1):
    """
    latitude, in degrees
    time = array of integer days. default is just 1 = Jan 1
    """
    lat = np.radians(latitude)
    # declination
    delta = np.radians(-23.45) * np.cos(((np.radians(360)/365) * (time+10)))
    # noon elevation
    elev = np.radians(180) - (np.radians(90) + lat - delta)

    return np.degrees(elev), np.degrees(delta)

# get extracted data and make it neat.

def get_me_data(file_name_1='Fig1_k0.1.csv', file_name_2='Fig1_k0.075.csv'):
    """
    file_name, file names (str)
    """
    path_to_folder = 'C:/Users/uv20102/OneDrive - University of Bristol/Documents/Mini_experiments/Sverdrup_phytoplankton/extracted_data/'
    
    f1 = np.genfromtxt(path_to_folder + file_name_1, delimiter = ',')
   
    f2 = np.genfromtxt(path_to_folder + file_name_2, delimiter = ',')
    
    return f1, f2

# critical depth calc

def crit_depth_calc(k, I_c, I_e, ds):
    
    D_cr = I_e[0:len(ds),] / ( k * I_c)
    
    return D_cr

# stop legend labels duplicating 

def stop_duplicate_labels(ax):
    
    handles, labels = ax.get_legend_handles_labels()
    
    unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
    
    ax.legend(*zip(*unique))
