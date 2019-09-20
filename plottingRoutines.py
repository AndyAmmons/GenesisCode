#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:49:19 2018

@author: aa245567
"""

import numpy as np

from decimal import Decimal


def fexp(number):
    (sign, digits, exponent) = Decimal(number).as_tuple()
    return len(digits) + exponent - 1

def fman(number):
    return round((Decimal(number).scaleb(-fexp(number)).normalize()),5)


path = '/Users/aa245567/Desktop/pythonstuff/'
abundn = np.load(path + 'abund2h_struct.npy')
regime = np.load(path + 'regime2h_struct.npy')
aswix1d = np.load(path + 'aswix_1d.npy')
abundnO = np.load(path + 'abund_struct.npy')
regimeO = np.load(path + 'regime_struct.npy')
fractorray = np.load(path + 'fractorray.npy')



PhotoAbundH = {'he2o':0.0851138,
              'c2o':0.00026915,
              'n2o':0.000067608,
              'ne2o':0.000085114,
              'mg2o':0.000039811,
              'si2o':0.000032359,
              's2o':0.000013183,
              'fe2o':0.000031623,}
PhotoAbundO = {'he2o':174.0,
               'c2o':0.550,
               'n2o':0.138,
               'ne2o':0.174,
               'mg2o':0.0813,
               'si2o':0.0661,
               's2o':0.0269,
               'fe2o':0.0646}
PhotoAbundMg = {'he2mg':2140.0,
                'c2mg':6.76,
                'n2mg':1.7,
                'ne2mg':2.14,
                'mg2mg':1.0,
                'si2mg':0.813,
                's2mg':0.331,
                'fe2mg':0.794}




def geoMean(Array):
    
    
    sumOfLogs = 0
    geometricMean = 0
    
    N = len(Array)
    for i in Array:
        if (i != 0) & (i != np.inf) & (i != np.nan) & (i > 0):
            sumOfLogs += np.log10(i)
        elif (i == 0):
            sumOfLogs = 0
            return 0
        else:
            pass
        
    geometricMean = 10.**((1/float(N)) * sumOfLogs)
    
    return geometricMean


#find the error for the high range in variances from the mean.
def ErrorHigh(Array):
    error = 0.0
    mean = geoMean(Array)
    N = float(len(Array))
    errorFromMean = 0
    #valist = []
    
    for i in Array:
        errorFromMean += (np.log10(i/mean)**2)
        #valist.append(np.log(i/mean))
        
    error = (np.sqrt((1./N) *(errorFromMean)))
    
    return (error*mean - error),N



#find the error for the low range in variances from the mean.
def ErrorLow(Array):
    error = 0.0
    mean = geoMean(Array)
    N = float(len(Array))
    errorFromMean = 0.
    
    for i in Array:
        errorFromMean += (np.log10(1/mean)**2)
        
    error = (np.sqrt((1./N) * (errorFromMean)))
    
    return (error - mean/error)


def fracUncert(error1, error2, val1, val2,N):
    
    fracuncert = np.sqrt((error1**2)/(val1**2) + (error2**2)/(val2**2))
    return fracuncert
    
    

def findRegMg(regimeNum,name,array,oneDay=0):
    
    '''Purpose: find data for corresponding regime.
    '''
        
    flagArr = regime['flag']
    speedArr = regime['v_p']
    
    if name == 'mg2o':
        if regimeNum == 'IS+CH':
            ind = np.where((flagArr != 1) & (flagArr != 0))
            lst1 = 1.0/np.array(abundn[ind]['mg2o'])
            lst2 = speedArr[ind]
        elif regimeNum == 'all':
            ind = np.where((flagArr[:]))
            lst1 = 1.0/np.array(abundn[np.where(flagArr[:])]['mg2o'])
            lst2 = speedArr[ind]
        elif regimeNum == 'CME':
            ind = np.where((flagArr == 1))
            lst1 = 1.0/np.array(abundn[ind]['mg2o'])
            lst2 = speedArr[ind]
        elif regimeNum == 'CH':
            ind = np.where((flagArr == 2))
            lst1 = 1.0/np.array(abundn[ind]['mg2o'])
            lst2 = speedArr[ind]
        elif regimeNum == 'IS':
            ind = np.where((flagArr == 3))
            lst1 = 1.0/np.array(abundn[ind]['mg2o'])
            lst2 = speedArr[ind]
        else:
            lst1 = []
            lst2 = []
        
    else:
        if regimeNum == 'IS+CH':
            ind = np.where((flagArr != 1) & (flagArr != 0))
            lst1 = array[ind]/abundn[ind]['mg2o']
            lst2 = speedArr[ind]
        elif regimeNum == 'all':
            ind = np.where((flagArr[:]))
            lst1 = array[np.where(flagArr[:])]/abundn[np.where(flagArr[:])]['mg2o']
            lst2 = speedArr[ind]
        elif regimeNum == 'CME':
            ind = np.where((flagArr == 1))
            lst1 = array[ind]/abundn[ind]['mg2o']
            lst2 = speedArr[ind]
        elif regimeNum == 'CH':
            ind = np.where((flagArr == 2))
            lst1 = array[np.where(flagArr == 2)]/abundn[ind]['mg2o']
            lst2 = speedArr[ind]
        elif regimeNum == 'IS':
            ind = np.where((flagArr == 3))
            lst1 = array[np.where(flagArr == 3)]/abundn[ind]['mg2o']
            lst2 = speedArr[ind]
        else:
            lst1 = []
            lst2 = []
    return lst2,lst1
    

def findReg(speedArray,regimeNum,array,oneDay=0):
    
    if oneDay == 1:
        flagArr = aswix1d['flag']
        speedArr = speedArray
    else:
        flagArr = regime['flag']
        speedArr = speedArray
    if regimeNum == 'IS+CH':
        ind = np.where((flagArr != 1) & (flagArr != 0))
        lst1 = array[ind]
        lst2 = speedArr[ind]
    elif regimeNum == 'all':
        ind = np.where((flagArr[:]))
        lst1 = array[np.where(flagArr[:])]
        lst2 = speedArr[ind]
    elif regimeNum == 'CME':
        ind = np.where((flagArr == 1))
        lst1 = array[np.where(flagArr == 1)]
        lst2 = speedArr[ind]
    elif regimeNum == 'CH':
        ind = np.where((flagArr == 2))
        lst1 = array[np.where(flagArr == 2)]
        lst2 = speedArr[ind]
    elif regimeNum == 'IS':
        ind = np.where((flagArr == 3))
        lst1 = array[np.where(flagArr == 3)]
        lst2 = speedArr[ind]
    else:
        lst1 = []
        lst2 = []
    return lst2,lst1
    

def fracs(arr1,name=None):
    lst = []
    if (name != None):
        for i in arr1:
            if i > 0.0:
                lst.append(i)
    if (name == None):
        for i in arr1:
            if i > 0.0:
                lst.append(i)
    return lst


def geoMeanOfLog(dataLim, xdata, ydata, speed=np.arange(200,1825,25)):
    
    dBins = []
    vBins = []

    for i in range(1,len(speed)):
        yvals = ydata[np.where((xdata >= speed[i-1]) & (xdata <= speed[i]))]
        xvals = xdata[np.where((xdata >= speed[i-1]) & (xdata <= speed[i]))]
        
        if (len(yvals) >= dataLim) & (np.nan not in yvals):
            dBins.append(geoMean(np.log10(yvals)))
            vBins.append(geoMean(xvals))
            
     #       bBins.append(np.log10(var))
    return vBins,dBins



def meanOfLog(dataLim,xdata,ydata,speed=np.arange(200,1825,25)):
    '''
    INPUTS: 
        speed    - array of speeds in range low -> high with steps, user defined.
        dataLim  - scalar limit to which taking the mean of the log(data) applies.
        xdata    - wind speed data to check against speed input.
        ydata    - data to be weighted.
    '''
    dBins = []
    vBins = []
    #bBins = []
    
    for i in range(1,len(speed)):
        yvals = ydata[np.where((xdata >= speed[i-1]) & (xdata <= speed[i]))]
        xvals = xdata[np.where((xdata >= speed[i-1]) & (xdata <= speed[i]))]
        
        if (len(yvals) >= dataLim) & (np.nan not in yvals):
            dBins.append(np.mean(np.log10(yvals)))
            vBins.append(np.mean(xvals))
            
     #       bBins.append(np.log10(var))
    return vBins,dBins
            
    
def goodBins(lst1,lst2):
    '''return properly aligned data arrays.'''
    arr1 = lst1[np.where((lst1 > 0.0) & (lst2 > 0.0) & (lst1 != np.nan) & (lst2 != np.nan))]
    arr2 = lst2[np.where((lst1 > 0.0) & (lst2 > 0.0) & (lst1 != np.nan) & (lst2 != np.nan))]
    
    return arr1, arr2


def histWRangesMg(flagnum,fluence,dataLim,speed=np.arange(200,1825,25)):
    '''returns the minimum, average, and maximum variances of fluence ratios
    per speed bin (200km/s - 800km/s)
    
    INPUTS:
        speed   - wind speed array to select ranges of data against.
        flagnum - regime number for species (1:CME, 2:CH, 3:IS, 0:bulk)
        fluence - name of species
        dataLim - scalar limit for purity of data ranges to be analyzed
    '''    
    lower = []
    upper = []
    ratiomean = []
    xspeed = []
    
    if fluence == 'mg2o':
        for i in range(1,len(speed)):
            ind = np.where((regime['v_p'] >= speed[i-1] - 12.5) & (regime['v_p'] <= speed[i]-12.5) & (regime['flag'] == flagnum)
            & (regime['v_p'] != np.inf))
            
            var = np.array(sorted(abundn[ind]['mg2o']))
            var = 1.0/var
            
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regime['v_p'][ind]))
                
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = geoMean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(geoMean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
                
    elif fluence == 'o76':
        
        for i in range(1,len(speed)):
            ind = np.where((regime['v_p'] >= speed[i-1]-12.5) & (regime['v_p'] <= speed[i]-12.5) & (regime['flag'] == flagnum))
            var = sorted(abundn[ind][fluence])
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regime['v_p'][ind]))
                
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = geoMean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(geoMean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
    
    else:
    
        for i in range(1,len(speed)):
            ind = np.where((regime['v_p'] >= speed[i-1]-12.5) & (regime['v_p'] <= speed[i]-12.5) & (regime['flag'] == flagnum))
            var = sorted(abundn[ind][fluence]/abundn[ind]['mg2o'])
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regime['v_p'][ind]))
                
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = geoMean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(geoMean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
    return lower,upper,ratiomean, xspeed
    
def geoHistWRanges(flagnum,fluence,dataLim,normSpec,speed=np.arange(200,1825,25)):
    '''returns the minimum, average, and maximum variances of fluence ratios
    per speed bin (200km/s - 800km/s)
    
    INPUTS:
        speed   - wind speed array to select ranges of data against.
        flagnum - regime number for species (1:CME, 2:CH, 3:IS, 0:bulk)
        fluence - name of species
        dataLim - scalar limit for purity of data ranges to be analyzed
    '''    
    #print speed
    lower = []
    upper = []
    ratiomean = []
    xspeed = []

        
    if (normSpec == 'Photosphere'):
        
        for i in range(1,len(speed)):
            ind = np.where((regime['v_p'] >= speed[i-1]-12.5) & (regime['v_p'] <= speed[i]-12.5) & (regime['flag'] == flagnum))
            var = np.array(sorted(abundn[ind][fluence]))/PhotoAbundH[fluence]
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regime['v_p'][ind]))
            
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = geoMean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(geoMean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
        return lower,upper,ratiomean, np.array(xspeed)
    if (normSpec == 'Hydrogen'):
        
        for i in range(1,len(speed)):
            ind = np.where((regime['v_p'] >= speed[i-1]-12.5) & (regime['v_p'] <= speed[i]-12.5) & (regime['flag'] == flagnum))
            var = np.array(sorted(abundn[ind][fluence]))
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regime['v_p'][ind]))
            
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = geoMean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(geoMean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
        return lower,upper,ratiomean, np.array(xspeed)
    
    if (normSpec == 'Oxygen'):
        
        for i in range(1,len(speed)):
            ind = np.where((regimeO['v_p'] >= speed[i-1]-12.5) & (regimeO['v_p'] <= speed[i]-12.5) & (regimeO['flag'] == flagnum))
            var = np.array(sorted(abundnO[ind][fluence]))
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regimeO['v_p'][ind]))
            
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = geoMean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(geoMean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
        return np.array(lower),np.array(upper),np.array(ratiomean), np.array(xspeed)
    
    if (normSpec == 'Fractionation Factor'):
        
        for i in range(1,len(speed)):
            ind = np.where((fractorray['v_p'] >= speed[i-1]-12.5) & (fractorray['v_p'] <= speed[i]-12.5) & (fractorray['flag'] == flagnum) & (fractorray['fracfactor'] > 0.0))
            var = np.array(sorted(fractorray[fluence][ind]))
            #print ind
            #print var
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(fractorray['v_p'][ind]))
                
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = geoMean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(geoMean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
        return np.array(lower),np.array(upper),np.array(ratiomean), np.array(xspeed)
    
def histWRanges(flagnum,fluence,dataLim,normSpec,speed=np.arange(200,1825,25)):
    '''returns the minimum, average, and maximum variances of fluence ratios
    per speed bin (200km/s - 800km/s)
    
    INPUTS:
        speed   - wind speed array to select ranges of data against.
        flagnum - regime number for species (1:CME, 2:CH, 3:IS, 0:bulk)
        fluence - name of species
        dataLim - scalar limit for purity of data ranges to be analyzed
    '''    
    #print speed
    lower = []
    upper = []
    ratiomean = []
    xspeed = []

        
    if (normSpec == 'Photosphere'):
        
        for i in range(1,len(speed)):
            ind = np.where((regime['v_p'] >= speed[i-1]-12.5) & (regime['v_p'] <= speed[i]-12.5) & (regime['flag'] == flagnum))
            var = np.array(sorted(abundn[ind][fluence]))/PhotoAbundH[fluence]
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regime['v_p'][ind]))
            
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = np.mean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(np.mean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
        return lower,upper,ratiomean, np.array(xspeed)
    if (normSpec == 'Hydrogen'):
        
        for i in range(1,len(speed)):
            ind = np.where((regime['v_p'] >= speed[i-1]-12.5) & (regime['v_p'] <= speed[i]-12.5) & (regime['flag'] == flagnum))
            var = np.array(sorted(abundn[ind][fluence]))
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regime['v_p'][ind]))
            
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = np.mean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(np.mean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
        return lower,upper,ratiomean, np.array(xspeed)
    
    if (normSpec == 'Oxygen'):
        
        for i in range(1,len(speed)):
            ind = np.where((regimeO['v_p'] >= speed[i-1]-12.5) & (regimeO['v_p'] <= speed[i]-12.5) & (regimeO['flag'] == flagnum))
            var = np.array(sorted(abundnO[ind][fluence]))
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(regimeO['v_p'][ind]))
            
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = np.mean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(np.mean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
        return np.array(lower),np.array(upper),np.array(ratiomean), np.array(xspeed)
    
    if (normSpec == 'Fractionation Factor'):
        
        for i in range(1,len(speed)):
            ind = np.where((fractorray['v_p'] >= speed[i-1]-12.5) & (fractorray['v_p'] <= speed[i]-12.5) & (fractorray['flag'] == flagnum) & (fractorray['fracfactor'] > 0.0))
            var = np.array(sorted(fractorray[fluence][ind]))
            #print ind
            #print var
            #xspeed = sorted()
            if (np.size(var) != 0) & (len(var) >= dataLim):
                xspeed.append(np.average(fractorray['v_p'][ind]))
                
                try:
                    upp = fracs([var[int(len(var)*0.90)]],name=None)
                    low = fracs([var[int(len(var)* 0.10)]],name=None)
                    med = np.mean(fracs(var,name=fluence))
                    lower.append(med-low)
                    upper.append(upp-med)
                    ratiomean.append(np.mean(fracs(var,name=fluence)))
                    # xspeed.append(np.average(regime['v_p'][np.where()]))
                except ValueError:
                    pass
        return np.array(lower),np.array(upper),np.array(ratiomean), np.array(xspeed)
    