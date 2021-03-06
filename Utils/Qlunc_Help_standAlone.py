# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:03:43 2020
@author: fcosta

Francisco Costa García
University of Stuttgart(c) 
"""

from Qlunc_ImportModules import *
import numpy as np

#import Qlunc_Help_standAlone as SA
#from Main.Qlunc_inputs import inputs

#%%# used to flatt at some points along the code:
flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (list,tuple)) else (a,))) 


#%% Combine uncertainties:
# The uncertainty combination is made following GUM
def unc_comb(data): # data is provided as a list of elements want to add on. Data is expected to be in dB (within this functions dB are transformed into watts).
    data_watts  = []
    res_dB      = []
    res_watts   = []
    zipped_data = []
    if not isinstance (data,np.ndarray):
        data=np.array(data)    
    for data_row in range(np.shape(data)[0]):# transform into watts
        
        try:    
            data_db=data[data_row,:]
        except:
            data_db=data[data_row][0]
             
        data_watts.append(10**(data_db/10))
    for i in range(len(data_watts[0])): # combining all uncertainties making sum of squares and the sqrt of the sum
        zipped_data.append(list(zip(*data_watts))[i])
        res_watts.append(np.sqrt(sum(map (lambda x: x**2,zipped_data[i]))))
        res_dB=10*np.log10(res_watts)
    del data_db
    return np.array(res_dB)

#%% Spherical into cartesian  coordinate transformation
    #    xcart = rho * cos(phi)*sin(theta)
    #    ycart = rho * sin(phi)*sin(theta)
    #    zcart = rho * cos(theta)
    
def sph2cart(Lidar): 
    x=[]
    y=[]
    z=[]
    
    for i in range(len(Lidar.optics.scanner.focus_dist)):
        x=Lidar.optics.scanner.focus_dist[i]*np.cos(np.deg2rad(Lidar.optics.scanner.phi))*np.sin(np.deg2rad(Lidar.optics.scanner.theta))
        y=Lidar.optics.scanner.focus_dist[i]*np.sin(np.deg2rad(Lidar.optics.scanner.phi))*np.sin(np.deg2rad(Lidar.optics.scanner.theta)) 
        z=Lidar.optics.scanner.focus_dist[i]*np.cos(np.deg2rad(Lidar.optics.scanner.theta)) 
    return(x,y,z)

