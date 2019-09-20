#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:52:54 2018

@author: Andrew ammons

plot (Solar wind abundance)/(Photospheric abundance)
"""

import numpy as np
import matplotlib.pyplot as plt
import plottingRoutines as pR



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


jvel = np.arange(200,1825,25) 


    

#assigns values to lists corresponding to speed bins before plotting.
#species normalized to hydrogen versus photospheric abundances normalized to hydrogen: 
#******************************************************************************

datamin = 8 #how much data to average over.

he2olowH2, he2ouppH2, he2omedH2,hespeedH2 = pR.histWRanges(2,'he2o',datamin,'Photosphere')
c2olowH2,c2ouppH2,c2omedH2,cspeedH2=pR.histWRanges(2,'c2o',datamin,'Photosphere')
n2olowH2,n2ouppH2,n2omedH2,nspeedH2=pR.histWRanges(2,'n2o',datamin,'Photosphere')
ne2olowH2,ne2ouppH2,ne2omedH2,nespeedH2=pR.histWRanges(2,'ne2o',datamin,'Photosphere')
mg2olowH2,mg2ouppH2,mg2omedH2,mgspeedH2=pR.histWRanges(2,'mg2o',datamin,'Photosphere')
si2olowH2,si2ouppH2,si2omedH2,sispeedH2=pR.histWRanges(2,'si2o',datamin,'Photosphere')
s2olowH2,s2ouppH2,s2omedH2,sspeedH2=pR.histWRanges(2,'s2o',datamin,'Photosphere')
fe2olowH2,fe2ouppH2,fe2omedH2,fespeedH2=pR.histWRanges(2,'fe2o',datamin,'Photosphere')


he2olowH1, he2ouppH1, he2omedH1,hespeedH1 = pR.histWRanges(1,'he2o',datamin,'Photosphere')
c2olowH1,c2ouppH1,c2omedH1,cspeedH1=pR.histWRanges(1,'c2o',datamin,'Photosphere')
n2olowH1,n2ouppH1,n2omedH1,nspeedH1=pR.histWRanges(1,'n2o',datamin,'Photosphere')
ne2olowH1,ne2ouppH1,ne2omedH1,nespeedH1=pR.histWRanges(1,'ne2o',datamin,'Photosphere')
mg2olowH1,mg2ouppH1,mg2omedH1,mgspeedH1=pR.histWRanges(1,'mg2o',datamin,'Photosphere')
si2olowH1,si2ouppH1,si2omedH1,sispeedH1=pR.histWRanges(1,'si2o',datamin,'Photosphere')
s2olowH1,s2ouppH1,s2omedH1,sspeedH1=pR.histWRanges(1,'s2o',datamin,'Photosphere')
fe2olowH1,fe2ouppH1,fe2omedH1,fespeedH1=pR.histWRanges(1,'fe2o',datamin,'Photosphere')


he2olowH3, he2ouppH3, he2omedH3,hespeedH3 = pR.histWRanges(3,'he2o',datamin,'Photosphere')
c2olowH3,c2ouppH3,c2omedH3,cspeedH3=pR.histWRanges(3,'c2o',datamin,'Photosphere')
n2olowH3,n2ouppH3,n2omedH3,nspeedH3=pR.histWRanges(3,'n2o',datamin,'Photosphere')
ne2olowH3,ne2ouppH3,ne2omedH3,nespeedH3=pR.histWRanges(3,'ne2o',datamin,'Photosphere')
mg2olowH3,mg2ouppH3,mg2omedH3,mgspeedH3=pR.histWRanges(3,'mg2o',datamin,'Photosphere')
si2olowH3,si2ouppH3,si2omedH3,sispeedH3=pR.histWRanges(3,'si2o',datamin,'Photosphere')
s2olowH3,s2ouppH3,s2omedH3,sspeedH3=pR.histWRanges(3,'s2o',datamin,'Photosphere')
fe2olowH3,fe2ouppH3,fe2omedH3,fespeedH3=pR.histWRanges(3,'fe2o',datamin,'Photosphere')


he2olowH0, he2ouppH0, he2omedH0,hespeedH0 = pR.histWRanges(0,'he2o',datamin,'Photosphere')
c2olowH0,c2ouppH0,c2omedH0,cspeedH0=pR.histWRanges(0,'c2o',datamin,'Photosphere')
n2olowH0,n2ouppH0,n2omedH0,nspeedH0=pR.histWRanges(0,'n2o',datamin,'Photosphere')
ne2olowH0,ne2ouppH0,ne2omedH0,nespeedH0=pR.histWRanges(0,'ne2o',datamin,'Photosphere')
mg2olowH0,mg2ouppH0,mg2omedH0,mgspeedH0=pR.histWRanges(0,'mg2o',datamin,'Photosphere')
si2olowH0,si2ouppH0,si2omedH0,sispeedH0=pR.histWRanges(0,'si2o',datamin,'Photosphere')
s2olowH0,s2ouppH0,s2omedH0,sspeedH0=pR.histWRanges(0,'s2o',datamin,'Photosphere')
fe2olowH0,fe2ouppH0,fe2omedH0,fespeedH0=pR.histWRanges(0,'fe2o',datamin,'Photosphere')


#Hydrogen: ********************************************************************

he2hlow2, he2hupp2, he2hmed2,hespeed2 = pR.histWRanges(2,'he2o',datamin,'Hydrogen')
c2hlow2,c2hupp2,c2hmed2,cspeed2=pR.histWRanges(2,'c2o',datamin,'Hydrogen')
n2hlow2,n2hupp2,n2hmed2,nspeed2=pR.histWRanges(2,'n2o',datamin,'Hydrogen')
ne2hlow2,ne2hupp2,ne2hmed2,nespeed2=pR.histWRanges(2,'ne2o',datamin,'Hydrogen')
mg2hlow2,mg2hupp2,mg2hmed2,mgspeed2=pR.histWRanges(2,'mg2o',datamin,'Hydrogen')
si2hlow2,si2hupp2,si2hmed2,sispeed2=pR.histWRanges(2,'si2o',datamin,'Hydrogen')
s2hlow2,s2hupp2,s2hmed2,sspeed2=pR.histWRanges(2,'s2o',datamin,'Hydrogen')
fe2hlow2,fe2hupp2,fe2hmed2,fespeed2=pR.histWRanges(2,'fe2o',datamin,'Hydrogen')


he2hlow1, he2hupp1, he2hmed1,hespeed1 = pR.histWRanges(1,'he2o',datamin,'Hydrogen')
c2hlow1,c2hupp1,c2hmed1,cspeed1=pR.histWRanges(1,'c2o',datamin,'Hydrogen')
n2hlow1,n2hupp1,n2hmed1,nspeed1=pR.histWRanges(1,'n2o',datamin,'Hydrogen')
ne2hlow1,ne2hupp1,ne2hmed1,nespeed1=pR.histWRanges(1,'ne2o',datamin,'Hydrogen')
mg2hlow1,mg2hupp1,mg2hmed1,mgspeed1=pR.histWRanges(1,'mg2o',datamin,'Hydrogen')
si2hlow1,si2hupp1,si2hmed1,sispeed1=pR.histWRanges(1,'si2o',datamin,'Hydrogen')
s2hlow1,s2hupp1,s2hmed1,sspeed1=pR.histWRanges(1,'s2o',datamin,'Hydrogen')
fe2hlow1,fe2hupp1,fe2hmed1,fespeed1=pR.histWRanges(1,'fe2o',datamin,'Hydrogen')


he2hlow3, he2hupp3, he2hmed3,hespeed3 = pR.histWRanges(3,'he2o',datamin,'Hydrogen')
c2hlow3,c2hupp3,c2hmed3,cspeed3=pR.histWRanges(3,'c2o',datamin,'Hydrogen')
n2hlow3,n2hupp3,n2hmed3,nspeed3=pR.histWRanges(3,'n2o',datamin,'Hydrogen')
ne2hlow3,ne2hupp3,ne2hmed3,nespeed3=pR.histWRanges(3,'ne2o',datamin,'Hydrogen')
mg2hlow3,mg2hupp3,mg2hmed3,mgspeed3=pR.histWRanges(3,'mg2o',datamin,'Hydrogen')
si2hlow3,si2hupp3,si2hmed3,sispeed3=pR.histWRanges(3,'si2o',datamin,'Hydrogen')
s2hlow3,s2hupp3,s2hmed3,sspeed3=pR.histWRanges(3,'s2o',datamin,'Hydrogen')
fe2hlow3,fe2hupp3,fe2hmed3,fespeed3=pR.histWRanges(3,'fe2o',datamin,'Hydrogen')


he2hlow0, he2hupp0, he2hmed0,hespeed0 = pR.histWRanges(0,'he2o',datamin,'Hydrogen')
c2hlow0,c2hupp0,c2hmed0,cspeed0=pR.histWRanges(0,'c2o',datamin,'Hydrogen')
n2hlow0,n2hupp0,n2hmed0,nspeed0=pR.histWRanges(0,'n2o',datamin,'Hydrogen')
ne2hlow0,ne2hupp0,ne2hmed0,nespeed0=pR.histWRanges(0,'ne2o',datamin,'Hydrogen')
mg2hlow0,mg2hupp0,mg2hmed0,mgspeed0=pR.histWRanges(0,'mg2o',datamin,'Hydrogen')
si2hlow0,si2hupp0,si2hmed0,sispeed0=pR.histWRanges(0,'si2o',datamin,'Hydrogen')
s2hlow0,s2hupp0,s2hmed0,sspeed0=pR.histWRanges(0,'s2o',datamin,'Hydrogen')
fe2hlow0,fe2hupp0,fe2hmed0,fespeed0=pR.histWRanges(0,'fe2o',datamin,'Hydrogen')




#Oxygen: **********************************************************************

he2olowO2, he2ouppO2, he2omedO2,hespeedO2 = pR.histWRanges(2,'he2o',datamin,'Oxygen')
c2olowO2,c2ouppO2,c2omedO2,cspeedO2=pR.histWRanges(2,'c2o',datamin,'Oxygen')
n2olowO2,n2ouppO2,n2omedO2,nspeedO2=pR.histWRanges(2,'n2o',datamin,'Oxygen')
ne2olowO2,ne2ouppO2,ne2omedO2,nespeedO2=pR.histWRanges(2,'ne2o',datamin,'Oxygen')
mg2olowO2,mg2ouppO2,mg2omedO2,mgspeedO2=pR.histWRanges(2,'mg2o',datamin,'Oxygen')
si2olowO2,si2ouppO2,si2omedO2,sispeedO2=pR.histWRanges(2,'si2o',datamin,'Oxygen')
s2olowO2,s2ouppO2,s2omedO2,sspeedO2=pR.histWRanges(2,'s2o',datamin,'Oxygen')
fe2olowO2,fe2ouppO2,fe2omedO2,fespeedO2=pR.histWRanges(2,'fe2o',datamin,'Oxygen')
o8low2, o8upp2, o8med2,o8speed2=pR.histWRanges(2,'o8',datamin,'Oxygen')

he2olowO1, he2ouppO1, he2omedO1,hespeedO1 = pR.histWRanges(1,'he2o',datamin,'Oxygen')
c2olowO1,c2ouppO1,c2omedO1,cspeedO1=pR.histWRanges(1,'c2o',datamin,'Oxygen')
n2olowO1,n2ouppO1,n2omedO1,nspeedO1=pR.histWRanges(1,'n2o',datamin,'Oxygen')
ne2olowO1,ne2ouppO1,ne2omedO1,nespeedO1=pR.histWRanges(1,'ne2o',datamin,'Oxygen')
mg2olowO1,mg2ouppO1,mg2omedO1,mgspeedO1=pR.histWRanges(1,'mg2o',datamin,'Oxygen')
si2olowO1,si2ouppO1,si2omedO1,sispeedO1=pR.histWRanges(1,'si2o',datamin,'Oxygen')
s2olowO1,s2ouppO1,s2omedO1,sspeedO1=pR.histWRanges(1,'s2o',datamin,'Oxygen')
fe2olowO1,fe2ouppO1,fe2omedO1,fespeedO1=pR.histWRanges(1,'fe2o',datamin,'Oxygen')
o76low1, o76upp1, o76med1,o76speed1=pR.histWRanges(1,'o76',datamin,'Oxygen')

he2olowO3, he2ouppO3, he2omedO3,hespeedO3 = pR.histWRanges(3,'he2o',datamin,'Oxygen')
c2olowO3,c2ouppO3,c2omedO3,cspeedO3=pR.histWRanges(3,'c2o',datamin,'Oxygen')
n2olowO3,n2ouppO3,n2omedO3,nspeedO3=pR.histWRanges(3,'n2o',datamin,'Oxygen')
ne2olowO3,ne2ouppO3,ne2omedO3,nespeedO3=pR.histWRanges(3,'ne2o',datamin,'Oxygen')
mg2olowO3,mg2ouppO3,mg2omedO3,mgspeedO3=pR.histWRanges(3,'mg2o',datamin,'Oxygen')
si2olowO3,si2ouppO3,si2omedO3,sispeedO3=pR.histWRanges(3,'si2o',datamin,'Oxygen')
s2olowO3,s2ouppO3,s2omedO3,sspeedO3=pR.histWRanges(3,'s2o',datamin,'Oxygen')
fe2olowO3,fe2ouppO3,fe2omedO3,fespeedO3=pR.histWRanges(3,'fe2o',datamin,'Oxygen')
o76low3,o76upp3,o76med3,o76speed3=pR.histWRanges(3,'o76',datamin,'Oxygen')

he2olowO0, he2ouppO0, he2omedO0,hespeedO0 = pR.histWRanges(0,'he2o',datamin,'Oxygen')
c2olowO0,c2ouppO0,c2omedO0,cspeedO0=pR.histWRanges(0,'c2o',datamin,'Oxygen')
n2olowO0,n2ouppO0,n2omedO0,nspeedO0=pR.histWRanges(0,'n2o',datamin,'Oxygen')
ne2olowO0,ne2ouppO0,ne2omedO0,nespeedO0=pR.histWRanges(0,'ne2o',datamin,'Oxygen')
mg2olowO0,mg2ouppO0,mg2omedO0,mgspeedO0=pR.histWRanges(0,'mg2o',datamin,'Oxygen')
si2olowO0,si2ouppO0,si2omedO0,sispeedO0=pR.histWRanges(0,'si2o',datamin,'Oxygen')
s2olowO0,s2ouppO0,s2omedO0,sspeedO0=pR.histWRanges(0,'s2o',datamin,'Oxygen')
fe2olowO0,fe2ouppO0,fe2omedO0,fespeedO0=pR.histWRanges(0,'fe2o',datamin,'Oxygen')
o76low3,o76upp3,o76med3,o76speed3=pR.histWRanges(3,'o76',datamin,'Oxygen')



#Magnesium: ************************************************************
'''   
he2mglow2, he2mgupp2, he2mgmed2,hespeed2 = pR.histWRanges(2,'he2mg',datamin,'Oxygen')
c2olowO2,c2ouppO2,c2omedO2,cspeedO2=pR.histWRanges(2,'c2o',datamin,'Oxygen')
n2olowO2,n2ouppO2,n2omedO2,nspeedO2=pR.histWRanges(2,'n2o',datamin,'Oxygen')
ne2olowO2,ne2ouppO2,ne2omedO2,nespeedO2=pR.histWRanges(2,'ne2o',datamin,'Oxygen')
mg2olowO2,mg2ouppO2,mg2omedO2,mgspeedO2=pR.histWRanges(2,'mg2o',datamin,'Oxygen')
si2olowO2,si2ouppO2,si2omedO2,sispeedO2=pR.histWRanges(2,'si2o',datamin,'Oxygen')
s2olowO2,s2ouppO2,s2omedO2,sspeedO2=pR.histWRanges(2,'s2o',datamin,'Oxygen')
fe2olowO2,fe2ouppO2,fe2omedO2,fespeedO2=pR.histWRanges(2,'fe2o',datamin,'Oxygen')


he2olowO1, he2ouppO1, he2omedO1,hespeedO1 = pR.histWRanges(1,'he2o',datamin,'Oxygen')
c2olowO1,c2ouppO1,c2omedO1,cspeedO1=pR.histWRanges(1,'c2o',datamin,'Oxygen')
n2olowO1,n2ouppO1,n2omedO1,nspeedO1=pR.histWRanges(1,'n2o',datamin,'Oxygen')
ne2olowO1,ne2ouppO1,ne2omedO1,nespeedO1=pR.histWRanges(1,'ne2o',datamin,'Oxygen')
mg2olowO1,mg2ouppO1,mg2omedO1,mgspeedO1=pR.histWRanges(1,'mg2o',datamin,'Oxygen')
si2olowO1,si2ouppO1,si2omedO1,sispeedO1=pR.histWRanges(1,'si2o',datamin,'Oxygen')
s2olowO1,s2ouppO1,s2omedO1,sspeedO1=pR.histWRanges(1,'s2o',datamin,'Oxygen')
fe2olowO1,fe2ouppO1,fe2omedO1,fespeedO1=pR.histWRanges(1,'fe2o',datamin,'Oxygen')


he2olowO3, he2ouppO3, he2omedO3,hespeedO3 = pR.histWRanges(3,'he2o',datamin,'Oxygen')
c2olowO3,c2ouppO3,c2omedO3,cspeedO3=pR.histWRanges(3,'c2o',datamin,'Oxygen')
n2olowO3,n2ouppO3,n2omedO3,nspeedO3=pR.histWRanges(3,'n2o',datamin,'Oxygen')
ne2olowO3,ne2ouppO3,ne2omedO3,nespeedO3=pR.histWRanges(3,'ne2o',datamin,'Oxygen')
mg2olowO3,mg2ouppO3,mg2omedO3,mgspeedO3=pR.histWRanges(3,'mg2o',datamin,'Oxygen')
si2olowO3,si2ouppO3,si2omedO3,sispeedO3=pR.histWRanges(3,'si2o',datamin,'Oxygen')
s2olowO3,s2ouppO3,s2omedO3,sspeedO3=pR.histWRanges(3,'s2o',datamin,'Oxygen')
fe2olowO3,fe2ouppO3,fe2omedO3,fespeedO3=pR.histWRanges(3,'fe2o',datamin,'Oxygen')


he2olowO0, he2ouppO0, he2omedO0,hespeedO0 = pR.histWRanges(0,'he2o',datamin,'Oxygen')
c2olowO0,c2ouppO0,c2omedO0,cspeedO0=pR.histWRanges(0,'c2o',datamin,'Oxygen')
n2olowO0,n2ouppO0,n2omedO0,nspeedO0=pR.histWRanges(0,'n2o',datamin,'Oxygen')
ne2olowO0,ne2ouppO0,ne2omedO0,nespeedO0=pR.histWRanges(0,'ne2o',datamin,'Oxygen')
mg2olowO0,mg2ouppO0,mg2omedO0,mgspeedO0=pR.histWRanges(0,'mg2o',datamin,'Oxygen')
si2olowO0,si2ouppO0,si2omedO0,sispeedO0=pR.histWRanges(0,'si2o',datamin,'Oxygen')
s2olowO0,s2ouppO0,s2omedO0,sspeedO0=pR.histWRanges(0,'s2o',datamin,'Oxygen')
fe2olowO0,fe2ouppO0,fe2omedO0,fespeedO0=pR.histWRanges(0,'fe2o',datamin,'Oxygen')
'''


#############********************##############
#plotting the fractionation factor:
    
#     fip = ((|Mg| + |si| + |s| + |fe|)
#           --------------------------
#            (|C| + |N| + |O| + |Ne|))   <--Solar Wind
#      -----------------------------------
#           ((|Mg| + |Si| + |S| + |Fe|)
#           --------------------------
#            (|C| + |N| + |O| + |Ne|))   <--Photosphere

#flags correspond to regime as 0 = bulk (which we dont use), 1 = cme, 2 = ch, 3 = is 


fraclow0, fracupp0, fracmed0, fracspeed0 = pR.histWRanges(0,'fracfactor',datamin,'Fractionation Factor')
fraclow1, fracupp1, fracmed1, fracspeed1 = pR.histWRanges(1,'fracfactor',datamin,'Fractionation Factor')
fraclow2, fracupp2, fracmed2, fracspeed2 = pR.histWRanges(2,'fracfactor',datamin,'Fractionation Factor')
fraclow3, fracupp3, fracmed3, fracspeed3 = pR.histWRanges(3,'fracfactor',datamin,'Fractionation Factor')
            
            
            
            
#Table 7 from page 146:
    
def fitArrays(arr1, arr2):
    
    arr1len = len(arr1)
    arr2len = len(arr2)
    
    if (arr1len > arr2len):
        ind = arr1len - arr2len
        return (arr1[:-ind])/arr2
    else:
        return
    
    
#flags correspond to regime as 0 = bulk (which we dont use), 1 = cme, 2 = ch, 3 = is 


#Plots abundance ratios and variances.

#############********************##############

names = ['he2o','c2o','n2o','ne2o','mg2o','si2o','s2o','fe2o']
speeds = ['vhe','vc5','vn5','vne8','vmg10','vsi8','vs8','vfe10']
ylblparams = [[-6,0.5,101],[-6,1,101],[-4,1,101],[-4,1.5,101],[-4,1.5,101],[-4,1.5,101],
              [-4,1.5,100], [-4,1.5,101]]
reglbls = ['IS+CH','CME','CH','IS']
flagNum = [0,1,2,3]
ind = 0
path = "Users/aa245567/Desktop/"
ymaxparams = [10**(0.50),10**(1.00),10.**(1.00),10**(1.00),10**(1.00),10**(1.20),10**(1.50),10**(1.20)]
yminparams = [10**(-1.5),10**(-1.0),10.**(-1.0),10**(-1.0),10**(-1.0),10**(-0.5),10**(-0.5),10**(-0.6)]
for nm in range(len(names)):
    fig, axs = plt.subplots(2,2,figsize=(15,10))
    axes = np.ravel(axs)
    axind = 0
    for rel in reglbls:
#        if names[nm] == 'n2o' or names[nm] == 's2o':
#            x,y = findReg(rel,aswix1d[names[nm]],oneDay = 1)
#            x,y = goodBins(x,y)
        
#        else:
    
        x,y = pR.findReg(abundn[speeds[nm]],rel,abundn[names[nm]]/PhotoAbundH[names[nm]])
        x,y = pR.goodBins(x,y)
       # print y
        
        xbins = np.linspace(0,851,75)
        ybins = np.logspace(ylblparams[nm][0],ylblparams[nm][1],ylblparams[nm][2])
        #print ybins
        X,Y = np.meshgrid(xbins,ybins)
        px,py = pR.meanOfLog(5,x,y,speed = abundn[speeds[nm]])
        #print py
        fit = np.polyfit(px,py,1,full=False,cov=True)
        slope = fit[0][0]
        intercept = fit[0][1]
        covariance = fit[1]
        bfline = 10**(slope * xbins + intercept)
        counts,xedges,yedges = np.histogram2d(x,y,bins=(xbins,ybins))
        #print counts[np.where(counts != 0.0)]
        cl = axes[axind].pcolormesh(X,Y,np.transpose(counts),cmap='jet')
        axes[axind].pcolormesh(xedges,yedges,np.transpose(counts),cmap = 'jet')
        axes[axind].set_ylim(ymin=yminparams[nm], ymax=ymaxparams[nm])
        axes[axind].set_title(rel,fontweight='bold')
        axes[axind].set_yscale('log')
        axes[axind].plot(xbins,bfline,'w--')
        axes[axind].text(0.01,0.01,'Slope = %f +/- %f'%(slope,np.sqrt(covariance[-1][-1]))
        ,verticalalignment='bottom',horizontalalignment='left',transform=axes[axind].transAxes,color='white')
        
        axind += 1
    
    fig.text(0.04,0.6,'%s/H Solar Wind Abund to %s/H PhotoSphere Abund'%(names[nm][:-2].upper(),names[nm][:-2].upper()),rotation='vertical',fontsize='large')
    fig.text(0.5,0.03,'Solar Wind Speed (km/s)',ha='center',va='center',fontsize='large')
    cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
    fig.colorbar(cl,cax=cax)
    #plt.savefig(path + "x2h_" + str(ind))
    ind += 1

#################**************************########################


#Abundance ratios with 10-90% variances.

'''
fit ((ax0,ax1)) = plt.subplots(nrows = 1, ncols = 2)
fig.suptitle("experimental plot", fontsize = 'large')
'''



fig, ((ax0,ax1),(ax2,ax3),(ax4,ax5),(ax6,ax7)) = plt.subplots(nrows=4,ncols=2,figsize=(15,10))
fig.suptitle('Elemental Solar Wind Abundance to Photospheric Abundance Ratios:',fontsize='large')
fig.text(0.5,0.02,'Solar Wind Speed (km/s)',ha='center',va='center',fontsize='large')
ax0.errorbar(hespeedH2 + 5, he2omedH2, yerr=[he2olowH2, he2ouppH2], fmt='bo',label="CH")
ax0.errorbar(hespeedH1 + 15,he2omedH1,yerr=[he2olowH1,he2ouppH1],fmt='ro',label='CME')
ax0.errorbar(hespeedH3 , he2omedH3,yerr=[he2olowH3,he2ouppH3], fmt='go',label="IS")
ax0.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
ax0.set_ylabel('He/H',fontweight = 'bold')
ax0.set_yscale('log')
#ax0.set_ylim(ymin=30,ymax=300)

ax0.legend(numpoints=1,loc="upper right")



ax1.errorbar(cspeedH2+5, c2omedH2, yerr =[c2olowH2, c2ouppH2], fmt='bo' )
ax1.errorbar(cspeedH1+10,c2omedH1,yerr=[c2olowH1,c2ouppH1], fmt='ro')
ax1.errorbar(cspeedH3,c2omedH3,yerr=[c2olowH3,c2ouppH3], fmt='go')
ax1.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
#ax1.errorbar(jvel[:20],c2omed0[:25],yerr=[c2olow0[:25],c2oupp0[:25]],fmt='yo')
ax1.set_yscale('log')
ax1.yaxis.set_label_position('right')
ax1.set_ylabel('C/H',fontweight='bold')
#ax1.set_ylim(ymin=0.25,ymax=2.)



ax2.errorbar(nspeedH2+5,n2omedH2, yerr=[n2olowH2,n2ouppH2], fmt='bo')
ax2.errorbar(nspeedH1+10,n2omedH1,yerr=[n2olowH1,n2ouppH1], fmt='ro')
ax2.errorbar(nspeedH3,n2omedH3,yerr=[n2olowH3,n2ouppH3], fmt='go')
ax2.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
#ax2.errorbar(jvel[:20],n2omed0[:25],yerr=[n2olow0[:25],n2oupp0[:25]],fmt='yo')
ax2.set_yscale('log')
ax2.set_ylabel('N/H',fontweight='bold')
#ax2.set_ylim(ymin=0.075,ymax=0.7)



ax3.errorbar(nespeedH2+5,ne2omedH2,yerr=[ne2olowH2,ne2ouppH2],fmt='bo')
ax3.errorbar(nespeedH1+10,ne2omedH1,yerr=[ne2olowH1,ne2ouppH1], fmt='ro')
ax3.errorbar(nespeedH3,ne2omedH3,yerr=[ne2olowH3,ne2ouppH3], fmt='go')
ax3.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
#ax3.errorbar(jvel[:20],ne2omed0[:25],yerr=[ne2olow0[:25],ne2oupp0[:25]],fmt='yo')
ax3.set_yscale('log')
ax3.yaxis.set_label_position('right')
ax3.set_ylabel('Ne/H',fontweight='bold')
#ax3.set_ylim(ymin=0.06,ymax=0.6)



ax4.errorbar(mgspeedH2+5,mg2omedH2,yerr=[mg2olowH2,mg2ouppH2],fmt='bo')
ax4.errorbar(mgspeedH1+10,mg2omedH1,yerr=[mg2olowH1,mg2ouppH1], fmt='ro')
ax4.errorbar(mgspeedH3,mg2omedH3,yerr=[mg2olowH3,mg2ouppH3], fmt='go')
ax4.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
#ax4.errorbar(jvel[:20],mg2omed0[:25],yerr=[mg2olow0[:25],mg2oupp0[:25]],fmt='yo')
ax4.set_yscale('log')
ax4.set_ylabel('Mg/H',fontweight='bold')
#ax4.set_ylim(ymin=0.05,ymax=0.5)



ax5.errorbar(sispeedH2+5,si2omedH2,yerr=[si2olowH2,si2ouppH2],fmt='bo')
ax5.errorbar(sispeedH1+10,si2omedH1,yerr=[si2olowH1,si2ouppH1], fmt='ro')
ax5.errorbar(sispeedH3,si2omedH3,yerr=[si2olowH3,si2ouppH3], fmt='go')
ax5.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
#ax5.errorbar(jvel[:20],si2omed0[:25],yerr=[si2olow0[:25],si2oupp0[:25]],fmt='yo')
ax5.set_yscale('log')
ax5.yaxis.set_label_position('right')
ax5.set_ylabel('Si/H',fontweight='bold')
#ax5.set_ylim(ymin=0.05,ymax=0.5)



ax6.errorbar(sspeedH2+5,s2omedH2,yerr=[s2olowH2,s2ouppH2],fmt='bo')
ax6.errorbar(sspeedH1+10,s2omedH1,yerr=[s2olowH1,s2ouppH1], fmt='ro')
ax6.errorbar(sspeedH3,s2omedH3,yerr=[s2olowH3,s2ouppH3], fmt='go')
ax6.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
#ax6.errorbar(jvel[:20],s2omed0[:25],yerr=[s2olow0[:25],s2oupp0[:25]],fmt='yo')
ax6.set_yscale('log')
ax6.set_ylabel('S/H',fontweight='bold')
#ax6.set_ylim(ymin=0.025)



ax7.errorbar(fespeedH2+5,fe2omedH2,yerr=[fe2olowH2,fe2ouppH2],fmt='bo')
ax7.errorbar(fespeedH1+10,fe2omedH1,yerr=[fe2olowH1,fe2ouppH1], fmt='ro')
ax7.errorbar(fespeedH3,fe2omedH3,yerr=[fe2olowH3,fe2ouppH3], fmt='go')
ax7.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
#ax7.errorbar(jvel[:20],fe2omed0[:25],yerr=[fe2olow0[:25],fe2oupp0[:25]],fmt='yo')
ax7.set_yscale('log')
ax7.yaxis.set_label_position('right')
ax7.set_ylabel('Fe/H',fontweight='bold')


#flags correspond to regime as 0 = bulk (which we dont use), 1 = cme, 2 = ch, 3 = is 
'''
fig, (axfip) = plt.subplots(nrows=1,ncols=1,figsize=(9,3.5))
#fig.suptitle('Elemental Solar Wind Abundance to Photospheric Abundance Ratios:',fontsize='large')
fig.text(0.5,0.02,'Solar Wind Speed (km/s)',ha='center',va='center',fontsize='large')
axfip.errorbar(fracspeed2 + 5, fracmed2, yerr=[fraclow2, fracupp2], fmt='bo',label="CH")
axfip.errorbar(fracspeed1 + 15,fracmed1,yerr=[fraclow1,fracupp1],fmt='ro',label='CME')
axfip.errorbar(fracspeed3 , fracmed3,yerr=[fraclow3,fracupp3], fmt='go',label="IS")
#axfip.axhline(y=1,xmin = 0, c = 'black',linestyle='dashed')
axfip.set_ylabel('Fractionation Factor',fontweight = 'bold')
axfip.set_yscale('log')
axfip.set_ylim(ymin=10**(-0.2),ymax=10**1)

axfip.legend(numpoints=1,loc="upper right")
'''

plt.show()
