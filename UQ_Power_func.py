# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:50:18 2020

@author: fcosta
"""

from ImportModules import *


def UQ_PowerSource(inputs):
    if inputs.atm_inp.TimeSeries==True:
        UQ_power_source=[(inputs.atm_inp.Atmospheric_inputs['temperature'][i]*1+
                          inputs.atm_inp.Atmospheric_inputs['humidity'][i]*1+
                          (inputs.lidar_inp.Lidar_inputs['Wavelength'][0]/1000)+
                          inputs.power_inp.PowerSource_uncertainty_inputs['noise_powersource'][0]+
                          inputs.power_inp.PowerSource_uncertainty_inputs['OtherChanges_PowerSource'][0])\
                          for i in range(len(inputs.atm_inp.Atmospheric_inputs['temperature']))]
    else: 
        UQ_power_source=[(temp*1+hum*1+wave/1000+noise_ps+o_c_ps) \
                         for wave     in inputs.lidar_inp.Lidar_inputs['Wavelength']\
                         for temp     in inputs.atm_inp.Atmospheric_inputs['temperature']\
                         for hum      in inputs.atm_inp.Atmospheric_inputs['humidity']\
                         for noise_ps in inputs.power_inp.PowerSource_uncertainty_inputs['noise_powersource'] \
                         for o_c_ps   in inputs.power_inp.PowerSource_uncertainty_inputs['OtherChanges_PowerSource']]
    UQ_power_source=[round(UQ_power_source[i_dec],3) for i_dec in range(len(UQ_power_source))]
    return UQ_power_source

def UQ_Converter(inputs):
    if inputs.atm_inp.TimeSeries==True:
        UQ_converter=[inputs.atm_inp.Atmospheric_inputs['temperature'][i]*1+
                      inputs.atm_inp.Atmospheric_inputs['humidity'][i]*1+
                      inputs.lidar_inp.Lidar_inputs['Wavelength'][0]/1100+
                      inputs.power_inp.Converter_uncertainty_inputs['noise_conv'][0]+
                      inputs.power_inp.Converter_uncertainty_inputs['OtherChanges_conv'][0]\
                      for i in range(len(inputs.atm_inp.Atmospheric_inputs['temperature']))]
    else: 
        UQ_converter=[(temp*1+hum*1+wave/1100+noise_conv+o_c_conv)\
                      for wave in inputs.lidar_inp.Lidar_inputs['Wavelength']\
                      for temp in inputs.atm_inp.Atmospheric_inputs['temperature']\
                      for hum in inputs.atm_inp.Atmospheric_inputs['humidity']\
                      for noise_conv in inputs.power_inp.Converter_uncertainty_inputs['noise_conv'] \
                      for o_c_conv in inputs.power_inp.Converter_uncertainty_inputs['OtherChanges_conv']]
    UQ_converter=[round(UQ_converter[i_dec],3) for i_dec in range(len(UQ_converter))]
    return UQ_converter

def Losses_Converter(losses):
    return losses