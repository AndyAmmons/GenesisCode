#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:40:07 2018

@author: aa245567
"""




import numpy as np
import plottingRoutines as pR


path = '/Users/aa245567/Desktop/pythonstuff/'
abundn = np.load(path + 'abund2h_struct.npy')
regime = np.load(path + 'regime2h_struct.npy')
aswix1d = np.load(path + 'aswix_1d.npy')
abundnO = np.load(path + 'abund_struct.npy')
regimeO = np.load(path + 'regime_struct.npy')
fractorray = np.load(path + 'fractorray.npy')

PhotoAbundH = {'he2o':0.0851138,'c2o':0.00026915,'n2o':0.000067608,'ne2o':0.000085114,'mg2o':0.000039811,'si2o':0.000032359,'s2o':0.000013183,'fe2o':0.000031623,}
#PhotoAbundO = {'he2o':174.0,'c2o':0.550,'n2o':0.138,'ne2o':0.174,'mg2o':0.0813,'si2o':0.0661,'s2o':0.0269,'fe2o':0.0646}
#PhotoAbundMg = {'he2mg':2140.0,'c2mg':6.76,'n2mg':1.7,'ne2mg':2.14,'mg2mg':1.0,'si2mg':0.813,'s2mg':0.331,'fe2mg':0.794}


jvel = np.arange(200,1825,25) 


datamin = 8

#Hydrogen: ********************************************************************

_,_, he2hmed2,_ = pR.geoHistWRanges(2,'he2o',datamin,'Hydrogen')
_,_,c2hmed2,_=pR.geoHistWRanges(2,'c2o',datamin,'Hydrogen')
_,_,n2hmed2,_=pR.geoHistWRanges(2,'n2o',datamin,'Hydrogen')
_,_,ne2hmed2,_=pR.geoHistWRanges(2,'ne2o',datamin,'Hydrogen')
_,_,mg2hmed2,_=pR.geoHistWRanges(2,'mg2o',datamin,'Hydrogen')
_,_,si2hmed2,_=pR.geoHistWRanges(2,'si2o',datamin,'Hydrogen')
_,_,s2hmed2,_=pR.geoHistWRanges(2,'s2o',datamin,'Hydrogen')
_,_,fe2hmed2,_=pR.geoHistWRanges(2,'fe2o',datamin,'Hydrogen')


_,_,he2hmed1,_ = pR.geoHistWRanges(1,'he2o',datamin,'Hydrogen')
_,_,c2hmed1,_=pR.geoHistWRanges(1,'c2o',datamin,'Hydrogen')
_,_,n2hmed1,_=pR.geoHistWRanges(1,'n2o',datamin,'Hydrogen')
_,_,ne2hmed1,_=pR.geoHistWRanges(1,'ne2o',datamin,'Hydrogen')
_,_,mg2hmed1,_=pR.geoHistWRanges(1,'mg2o',datamin,'Hydrogen')
_,_,si2hmed1,_=pR.geoHistWRanges(1,'si2o',datamin,'Hydrogen')
_,_,s2hmed1,_=pR.geoHistWRanges(1,'s2o',datamin,'Hydrogen')
_,_,fe2hmed1,_=pR.geoHistWRanges(1,'fe2o',datamin,'Hydrogen')


_,_,he2hmed3,_ = pR.geoHistWRanges(3,'he2o',datamin,'Hydrogen')
_,_,c2hmed3,_=pR.geoHistWRanges(3,'c2o',datamin,'Hydrogen')
_,_,n2hmed3,_=pR.geoHistWRanges(3,'n2o',datamin,'Hydrogen')
_,_,ne2hmed3,_=pR.geoHistWRanges(3,'ne2o',datamin,'Hydrogen')
_,_,mg2hmed3,_=pR.geoHistWRanges(3,'mg2o',datamin,'Hydrogen')
_,_,si2hmed3,_=pR.geoHistWRanges(3,'si2o',datamin,'Hydrogen')
_,_,s2hmed3,_=pR.geoHistWRanges(3,'s2o',datamin,'Hydrogen')
_,_,fe2hmed3,_=pR.geoHistWRanges(3,'fe2o',datamin,'Hydrogen')


_,_,he2hmed0,_ = pR.geoHistWRanges(0,'he2o',datamin,'Hydrogen')
_,_,c2hmed0,_=pR.geoHistWRanges(0,'c2o',datamin,'Hydrogen')
_,_,n2hmed0,_=pR.geoHistWRanges(0,'n2o',datamin,'Hydrogen')
_,_,ne2hmed0,_=pR.geoHistWRanges(0,'ne2o',datamin,'Hydrogen')
_,_,mg2hmed0,_=pR.geoHistWRanges(0,'mg2o',datamin,'Hydrogen')
_,_,si2hmed0,_=pR.geoHistWRanges(0,'si2o',datamin,'Hydrogen')
_,_,s2hmed0,_=pR.geoHistWRanges(0,'s2o',datamin,'Hydrogen')
_,_,fe2hmed0,_=pR.geoHistWRanges(0,'fe2o',datamin,'Hydrogen')




#Oxygen: **********************************************************************

_,_, he2omedO2,hespeed2= pR.geoHistWRanges(2,'he2o',datamin,'Oxygen')
_,_,c2omedO2,cspeed2=pR.geoHistWRanges(2,'c2o',datamin,'Oxygen')
_,_,n2omedO2,nspeed2=pR.geoHistWRanges(2,'n2o',datamin,'Oxygen')
_,_,ne2omedO2,nespeed2=pR.geoHistWRanges(2,'ne2o',datamin,'Oxygen')
_,_,mg2omedO2,mgspeed2=pR.geoHistWRanges(2,'mg2o',datamin,'Oxygen')
_,_,si2omedO2,sispeed2=pR.geoHistWRanges(2,'si2o',datamin,'Oxygen')
_,_,s2omedO2,sspeed2=pR.geoHistWRanges(2,'s2o',datamin,'Oxygen')
_,_,fe2omedO2,fespeed2=pR.geoHistWRanges(2,'fe2o',datamin,'Oxygen')
_,_,o76med2,o76speed2=pR.geoHistWRanges(2,'o76',datamin,'Oxygen')
_,_,c56med2,c56speed2 = pR.geoHistWRanges(2,'c56',datamin,'Oxygen')

_,_,he2omedO1,hespeed1 = pR.geoHistWRanges(1,'he2o',datamin,'Oxygen')
_,_,c2omedO1,cspeed1=pR.geoHistWRanges(1,'c2o',datamin,'Oxygen')
_,_,n2omedO1,nspeed1=pR.geoHistWRanges(1,'n2o',datamin,'Oxygen')
_,_,ne2omedO1,nespeed1=pR.geoHistWRanges(1,'ne2o',datamin,'Oxygen')
_,_,mg2omedO1,mgspeed1=pR.geoHistWRanges(1,'mg2o',datamin,'Oxygen')
_,_,si2omedO1,sispeed1=pR.geoHistWRanges(1,'si2o',datamin,'Oxygen')
_,_,s2omedO1,sspeed1=pR.geoHistWRanges(1,'s2o',datamin,'Oxygen')
_,_,fe2omedO1,fespeed1=pR.geoHistWRanges(1,'fe2o',datamin,'Oxygen')
_,_,o76med1,o76speed1=pR.geoHistWRanges(1,'o76',datamin,'Oxygen')
_,_,c56med1,c56speed1 = pR.geoHistWRanges(1,'c56',datamin,'Oxygen')

_,_,he2omedO3,hespeed3 = pR.geoHistWRanges(3,'he2o',datamin,'Oxygen')
_,_,c2omedO3,cspeed3=pR.geoHistWRanges(3,'c2o',datamin,'Oxygen')
_,_,n2omedO3,nspeed3=pR.geoHistWRanges(3,'n2o',datamin,'Oxygen')
_,_,ne2omedO3,nespeed3=pR.geoHistWRanges(3,'ne2o',datamin,'Oxygen')
_,_,mg2omedO3,mgspeed3=pR.geoHistWRanges(3,'mg2o',datamin,'Oxygen')
_,_,si2omedO3,sispeed3=pR.geoHistWRanges(3,'si2o',datamin,'Oxygen')
_,_,s2omedO3,sspeed3=pR.geoHistWRanges(3,'s2o',datamin,'Oxygen')
_,_,fe2omedO3,fespeed3=pR.geoHistWRanges(3,'fe2o',datamin,'Oxygen')
_,_,o76med3,o76speed3=pR.geoHistWRanges(3,'o76',datamin,'Oxygen')
_,_,c56med3,c56speed3=pR.geoHistWRanges(3,'c56',datamin,'Oxygen')

_,_,he2omedO0,hespeed0 = pR.geoHistWRanges(0,'he2o',datamin,'Oxygen')
_,_,c2omedO0,cspeed0=pR.geoHistWRanges(0,'c2o',datamin,'Oxygen')
_,_,n2omedO0,nspeed0=pR.geoHistWRanges(0,'n2o',datamin,'Oxygen')
_,_,ne2omedO0,nespeed0=pR.geoHistWRanges(0,'ne2o',datamin,'Oxygen')
_,_,mg2omedO0,mgspeed0=pR.geoHistWRanges(0,'mg2o',datamin,'Oxygen')
_,_,si2omedO0,sispeed0=pR.geoHistWRanges(0,'si2o',datamin,'Oxygen')
_,_,s2omedO0,sspeed0=pR.geoHistWRanges(0,'s2o',datamin,'Oxygen')
_,_,fe2omedO0,fespeed0=pR.geoHistWRanges(0,'fe2o',datamin,'Oxygen')
_,_,o76med0,o76speed0=pR.geoHistWRanges(0,'o76',datamin,'Oxygen')
_,_,c56med0,c56speed0=pR.geoHistWRanges(0,'c56',datamin,'Oxygen')



#Magnesium: ************************************************************

_,_,he2mgmedO2,hespeedmg2 = pR.histWRangesMg(2,'he2o',datamin)
_,_,c2mgmedO2,cspeedmg2 = pR.histWRangesMg(2,'c2o',datamin)
_,_,n2mgmedO2,nspeedmg2 = pR.histWRangesMg(2,'n2o',datamin)
_,_,ne2mgmedO2,nespeedmg2 = pR.histWRangesMg(2,'ne2o',datamin)
_,_,o2mgmedO2,ospeedmg2 = pR.histWRangesMg(2,'mg2o',datamin)
_,_,si2mgmedO2,sispeedmg2 = pR.histWRangesMg(2,'si2o',datamin)
_,_,s2mgmedO2,sspeedmg2 = pR.histWRangesMg(2,'s2o',datamin)
_,_,fe2mgmedO2,fespeedmg2 = pR.histWRangesMg(2,'fe2o',datamin)


_,_,he2mgmedO1,hespeedmg1 = pR.histWRangesMg(1,'he2o',datamin)
_,_,c2mgmedO1,cspeedmg1 =pR.histWRangesMg(1,'c2o',datamin)
_,_,n2mgmedO1,nspeedmg1 =pR.histWRangesMg(1,'n2o',datamin)
_,_,ne2mgmedO1,nespeedmg1 =pR.histWRangesMg(1,'ne2o',datamin)
_,_,o2mgmedO1,ospeedmg1 =pR.histWRangesMg(1,'mg2o',datamin)
_,_,si2mgmedO1,sispeedmg1 =pR.histWRangesMg(1,'si2o',datamin)
_,_,s2mgmedO1,sspeedmg1 =pR.histWRangesMg(1,'s2o',datamin)
_,_,fe2mgmedO1,fespeedmg1 =pR.histWRangesMg(1,'fe2o',datamin)


_,_,he2mgmedO3,hespeedmg3 = pR.histWRangesMg(3,'he2o',datamin)
_,_,c2mgmedO3,cspeedmg3 =pR.histWRangesMg(3,'c2o',datamin)
_,_,n2mgmedO3,nspeedmg3 =pR.histWRangesMg(3,'n2o',datamin)
_,_,ne2mgmedO3,nespeedmg3 =pR.histWRangesMg(3,'ne2o',datamin)
_,_,o2mgmedO3,ospeedmg3 =pR.histWRangesMg(3,'mg2o',datamin)
_,_,si2mgmedO3,sispeedmg3 =pR.histWRangesMg(3,'si2o',datamin)
_,_,s2mgmedO3,sspeedmg3 =pR.histWRangesMg(3,'s2o',datamin)
_,_,fe2mgmedO3,fespeedmg3 =pR.histWRangesMg(3,'fe2o',datamin)


_,_,he2mgmedO0,hespeedmg0 = pR.histWRangesMg(0,'he2o',datamin)
_,_,c2mgmedO0,cspeedmg0 =pR.histWRangesMg(0,'c2o',datamin)
_,_,n2mgmedO0,nspeedmg0 =pR.histWRangesMg(0,'n2o',datamin)
_,_,ne2mgmedO0,nespeedmg0 =pR.histWRangesMg(0,'ne2o',datamin)
_,_,o2mgmedO0,ospeedmg0 =pR.histWRangesMg(0,'mg2o',datamin)
_,_,si2mgmedO0,sispeedmg0 =pR.histWRangesMg(0,'si2o',datamin)
_,_,s2mgmedO0,sspeedmg0 =pR.histWRangesMg(0,'s2o',datamin)
_,_,fe2mgmedO0,fespeedmg0 =pR.histWRangesMg(0,'fe2o',datamin)

fraclow0, fracupp0, fracmed0, fracspeed0 = pR.histWRanges(0,'fracfactor',datamin,'Fractionation Factor')
fraclow1, fracupp1, fracmed1, fracspeed1 = pR.histWRanges(1,'fracfactor',datamin,'Fractionation Factor')
fraclow2, fracupp2, fracmed2, fracspeed2 = pR.histWRanges(2,'fracfactor',datamin,'Fractionation Factor')
fraclow3, fracupp3, fracmed3, fracspeed3 = pR.histWRanges(3,'fracfactor',datamin,'Fractionation Factor')


#x to oxygen table:
#flags correspond to regime as 0 = bulk, 1 = cme, 2 = ch, 3 = is 

def table7_X2O():
    
    species = ['He/O','C/O','N/O','Mg/O','Si/O','S/O','Fe/O','Ne/O','C6/C5','O7/O6','Frac']
    ISSpecies = [he2omedO3,c2omedO3,n2omedO3,mg2omedO3,si2omedO3,s2omedO3,fe2omedO3,ne2omedO3,c56med3,o76med3,fracmed3]
    CHSpecies = [he2omedO2,c2omedO2,n2omedO2,mg2omedO2,si2omedO2,s2omedO2,fe2omedO2,ne2omedO2,c56med2,o76med2,fracmed2]
    CMESpecies = [he2omedO1,c2omedO1,n2omedO1,mg2omedO1,si2omedO1,s2omedO1,fe2omedO1,ne2omedO1,c56med1,o76med1,fracmed1]
    BulkSpecies = [he2omedO0,c2omedO0,n2omedO0,mg2omedO0,si2omedO0,s2omedO0,fe2omedO0,ne2omedO0,c56med0,o76med0,fracmed0]
    PhotoAbundO = [174.0,0.550,0.138,0.174,0.0813,0.0661,0.0269,0.0646,'-','-','-']
    photoSpecUncrt = [4.0,0.0634,0.0159,0.0075,0.00457,0.00186,0.00596,0.0404,'--','--','--']
    
    
    for name, IS, CH, CME, Bulk, PhotAbund, PhotUncrt in zip(species,ISSpecies,CHSpecies,CMESpecies,BulkSpecies,PhotoAbundO,photoSpecUncrt):
        ISMean = pR.geoMean(IS)
        ISErrHigh,N1 = pR.ErrorHigh(IS)
        
        CHMean = pR.geoMean(CH)
        CHErrHigh,N2 = pR.ErrorHigh(CH)
        
        ISErrLow = pR.ErrorLow(IS)
        CHErrLow = pR.ErrorLow(CH)
        
        N = (N1 + N2)/2
        
        CMEMean = pR.geoMean(CME)
        #CMEstdD,_ = pR.stdDev(CME)
        BulkMean = pR.geoMean(Bulk)
        #BulkstdD,_ = pR.stdDev(Bulk)
        
        highFracUncert = pR.fracUncert(ISErrHigh,CHErrHigh,ISMean,CHMean,N)
        lowFracUncert = pR.fracUncert(ISErrLow,CHErrLow,ISMean, CHMean,N)
        highuncert = highFracUncert 
        lowuncert = lowFracUncert 
        #errorInMean = uncert/np.sqrt(N)
        
        photMean = PhotAbund
        photstdD = PhotUncrt
        
        
        print (name + '\t' + str(np.round(ISMean,3)) + '\t' + str(np.round(CHMean,3)) + '\t' + str(np.round(CMEMean,3)) + '\t'\
       + str(np.round(BulkMean,3)) + '\t' + str(np.round(ISMean/CHMean,3)) + '(' + '+' + str(np.round(highuncert,5)) + '/' + '-' + str(np.round(lowuncert,5)) + ')'\
       + '\t' + str(photMean) + '(' + str(photstdD) + ')')
        



#*************************************************************************

#table 7 for x 2 magnesium.
def table7_X2Mg():
    
    species = ['He/Mg','C/Mg','N/Mg','O/Mg','Si/Mg','S/Mg','Fe/Mg','Ne/Mg']
    
    ISSpecies = [he2mgmedO3,c2mgmedO3,n2mgmedO3,o2mgmedO3,si2mgmedO3,s2mgmedO3,fe2mgmedO3,ne2mgmedO3]
    CHSpecies = [he2mgmedO2,c2mgmedO2,n2mgmedO2,o2mgmedO2,si2mgmedO2,s2mgmedO2,fe2mgmedO2,ne2mgmedO2]
    CMESpecies = [he2mgmedO1,c2mgmedO1,n2mgmedO1,o2mgmedO1,si2mgmedO1,s2mgmedO1,fe2mgmedO1,ne2mgmedO1]
    BulkSpecies = [he2mgmedO0,c2mgmedO0,n2mgmedO0,o2mgmedO0,si2mgmedO0,s2mgmedO0,fe2mgmedO0,ne2mgmedO0]
    PhotoAbundMg = {'he2mg':2140.0,'c2mg':6.76,'n2mg':1.7,'ne2mg':2.14,'mg2mg':1.0,'si2mg':0.813,'s2mg':0.331,'fe2mg':0.794}
    photoSpecUncrt = [49.2,0.780,0.196,1.42,0.0562,0.0229,0.0733,0.497]
    
    
    for name, IS, CH, CME, Bulk, PhotAbund, PhotUncrt in zip(species,ISSpecies,CHSpecies,CMESpecies,BulkSpecies,PhotoAbundMg.values(),photoSpecUncrt):
        ISMean = pR.geoMean(IS)
        ISErrHigh,N1 = pR.ErrorHigh(IS)
        
        CHMean = pR.geoMean(CH)
        CHErrHigh,N2 = pR.ErrorHigh(CH)
        
        ISErrLow = pR.ErrorLow(IS)
        CHErrLow = pR.ErrorLow(CH)
        
        N = (N1 + N2)/2
        
        CMEMean = pR.geoMean(CME)
        CMEstdD,_ = pR.Error(CME)
        BulkMean = pR.geoMean(Bulk)
        BulkstdD,_ = pR.Error(Bulk)
        
        highFracUncert = pR.fracUncert(ISErrHigh,CHErrHigh,ISMean,CHMean,N)
        lowFracUncert = pR.fracUncert(ISErrLow,CHErrLow,ISMean, CHMean,N)
        highuncert = highFracUncert
        lowuncert = lowFracUncert
        
        photMean = PhotAbund
        photstdD = PhotUncrt
        
        print (name + '\t' + str(np.round(ISMean,3)) + '\t' + str(np.round(CHMean,3)) + '\t' + str(np.round(CMEMean,3)) + '\t'\
       + str(np.round(BulkMean,3)) + '\t' + str(np.round(ISMean/CHMean,3)) + '(' + '+' + str(np.round(highuncert,5)) + '/' + '-' + str(np.round(lowuncert,5)) + ')'\
       + '\t' + str(photMean) + '(' + str(photstdD) + ')')
    
#*************************************************************************


def table7_X2H():
    species = ['He/H','C/H','N/H','Mg/H','Si/H','S/H','Fe/H','Ne/H']
    ISSpecies = [he2hmed3,c2hmed3,n2hmed3,mg2hmed3,si2hmed3,s2hmed3,fe2hmed3,ne2hmed3]
    CHSpecies = [he2hmed2,c2hmed2,n2hmed2,mg2hmed2,si2hmed2,s2hmed2,fe2hmed2,ne2hmed2]
    CMESpecies = [he2hmed1,c2hmed1,n2hmed1,mg2hmed1,si2hmed1,s2hmed1,fe2hmed1,ne2hmed1]
    BulkSpecies = [he2hmed0,c2hmed0,n2hmed0,mg2hmed0,si2hmed0,s2hmed0,fe2hmed0,ne2hmed0]
    #photoSpecAbund = [0.0851,0.0002692,0.00006761,0.0000398,0.0000324,0.00001318,0.000031623,0.0000851]
    photoSpecUncrt = [0.00196,0.0000311,0.0000078,0.00000367,0.0000224,0.000000911,0.00000292,0.0000198]
    
    
    for name, IS, CH, CME, Bulk, PhotAbund, PhotUncrt in zip(species,ISSpecies,CHSpecies,CMESpecies,BulkSpecies,PhotoAbundH.values(),photoSpecUncrt):
        ISMean = pR.geoMean(IS)
        ISErrHigh,N1 = pR.ErrorHigh(IS)
        
        CHMean = pR.geoMean(CH)
        CHErrHigh,N2 = pR.ErrorHigh(CH)
        
        ISErrLow = pR.ErrorLow(IS)
        CHErrLow = pR.ErrorLow(CH)
        
        N = (N1 + N2)/2
        
        CMEMean = pR.geoMean(CME)
        CMEstdD,_ = pR.Error(CME)
        BulkMean = pR.geoMean(Bulk)
        BulkstdD,_ = pR.Error(Bulk)
        
        highFracUncert = pR.fracUncert(ISErrHigh,CHErrHigh,ISMean,CHMean,N)
        lowFracUncert = pR.fracUncert(ISErrLow,CHErrLow,ISMean, CHMean,N)
        highuncert = highFracUncert
        lowuncert = lowFracUncert
        
        photMean = PhotAbund
        photstdD = PhotUncrt
        
        print (name + '\t' + str(np.round(ISMean,3)) + '\t' + str(np.round(CHMean,3)) + '\t' + str(np.round(CMEMean,3)) + '\t'\
       + str(np.round(BulkMean,3)) + '\t' + str(np.round(ISMean/CHMean,3)) + '(' + '+' + str(np.round(highuncert,5)) + '/' + '-' + str(np.round(lowuncert,5)) + ')'\
       + '\t' + str(photMean) + '(' + str(photstdD) + ')')


#*************************************************************************


#Table 8's for x/(O,Mg,H):
    
    
    
#This table lists the IS/CH ratio for between the speeds 425 km/s to 525, however, I think it should span to 575, since my plots show that IS
# and CH overlap for up to that speed.

def table8_X2O():
    
    species = ['He/O','C/O','N/O','Mg/O','Si/O','S/O','Fe/O','Ne/O','C6/C5','O7/O6','Frac']
    ISSpecies = [he2omedO3,c2omedO3,n2omedO3,mg2omedO3,si2omedO3,s2omedO3,fe2omedO3,ne2omedO3,c56med3,o76med3,fracmed3]
    CHSpecies = [he2omedO2,c2omedO2,n2omedO2,mg2omedO2,si2omedO2,s2omedO2,fe2omedO2,ne2omedO2,c56med2,o76med2,fracmed2]
    ISSpeed = [hespeed3,cspeed3,nspeed3,mgspeed3,sispeed3,sspeed3,fespeed3,nespeed3,c56speed3,o76speed3,fracspeed3]
    CHSpeed = [hespeed2,cspeed2,nspeed2,mgspeed2,sispeed2,sspeed2,fespeed2,nespeed2,c56speed2,o76speed2,fracspeed2]
    
    
    for spec,IS,CH,speedis,speedch in zip(species,ISSpecies,CHSpecies,ISSpeed,CHSpeed):
        
        interstream = (IS[np.where((speedis >= 425.0) & (speedis <= 575.0))])
        coronalHole = (CH[np.where((speedch >= 425.0) & (speedch <= 575.0))])

        
        ISMean = pR.geoMean(interstream)
        CHMean = pR.geoMean(coronalHole)
        
        isErrorHigh,N1 = pR.ErrorHigh(interstream)
        isErrorLow = pR.ErrorLow(interstream)
        chErrorHigh,N2 = pR.ErrorHigh(coronalHole)
        chErrorLow = pR.ErrorLow(coronalHole)
        
        N = (N1 + N2)/2
        
        highFracUncert = pR.fracUncert(isErrorHigh,chErrorHigh,ISMean,CHMean,N)
        lowFracUncert = pR.fracUncert(isErrorLow,chErrorLow,ISMean, CHMean,N)
        highuncert = highFracUncert
        lowuncert = lowFracUncert
        
        
        IS2CH = pR.geoMean(interstream)/pR.geoMean(coronalHole)
        
        print spec + '\t' + str(np.round(IS2CH,3)) + '\t' + '+' + str(np.round(highuncert,5)) + '/' + '-' + str(np.round(lowuncert,5))
        
        
def table8_X2Mg():
    
    species = ['He/Mg','C/Mg','N/Mg','O/Mg','Si/Mg','S/Mg','Fe/Mg','Ne/Mg']
    
    ISSpecies = [he2mgmedO3,c2mgmedO3,n2mgmedO3,o2mgmedO3,si2mgmedO3,s2mgmedO3,fe2mgmedO3,ne2mgmedO3]

    CHSpecies = [he2mgmedO2,c2mgmedO2,n2mgmedO2,o2mgmedO2,si2mgmedO2,s2mgmedO2,fe2mgmedO2,ne2mgmedO2]
    ISSpeed = [hespeedmg3,cspeedmg3,nspeedmg3,ospeedmg3,sispeedmg3,sspeedmg3,fespeedmg3,nespeedmg3]
    CHSpeed = [hespeedmg2,cspeedmg2,nspeedmg2,ospeedmg2,sispeedmg2,sspeedmg2,fespeedmg2,nespeedmg2]
    print np.dtype(hespeedmg3)
    
    for spec,IS,CH,speedis,speedch in zip(species,ISSpecies,CHSpecies,ISSpeed,CHSpeed):
        print np.dtype(speedis)
        print speedch
        interstream = (IS[np.where((speedis >= 425.0) & (speedis <= 575.0))])
        coronalHole = (CH[np.where((speedch >= 425.0) & (speedch <= 575.0))])
        
        print IS
        print CH
        
        
        ISMean = pR.geoMean(interstream)
        CHMean = pR.geoMean(coronalHole)
        
        isErrorHigh,N1 = pR.ErrorHigh(interstream)
        isErrorLow = pR.ErrorLow(interstream)
        chErrorHigh,N2 = pR.ErrorHigh(coronalHole)
        chErrorLow = pR.ErrorLow(coronalHole)
        
        N = (N1 + N2)/2
        
        highFracUncert = pR.fracUncert(isErrorHigh,chErrorHigh,ISMean,CHMean,N)
        lowFracUncert = pR.fracUncert(isErrorLow,chErrorLow,ISMean, CHMean,N)
        highuncert = highFracUncert
        lowuncert = lowFracUncert
        
        
        
        IS2CH = pR.geoMean(interstream)/pR.geoMean(coronalHole)
        
        print spec + '\t' + str(np.round(IS2CH,3)) + '\t' + '+' + str(np.round(highuncert,5)) + '/' + '-' + str(np.round(lowuncert,5))
































