# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 20:48:25 2017

@author: andy
"""

import numpy as np
from matplotlib import pyplot as plt
import plottingRoutines as pR


#import all the stuff you need:

path = '/Users/aa245567/Desktop/pythonstuff/'
abundn = np.load(path + 'abund2h_struct.npy')
regime = np.load(path + 'regime2h_struct.npy')
aswix1d = np.load(path + 'aswix_1d.npy')


#plot the differential fluences for each regime,
#

jvel = np.arange(200,1825,25)  #Define jvel because it is convenient to do so here.    

#assigns values to lists corresponding to speed bins before plotting.

datamin = 8 #how much data to average over.

he2olow2, he2oupp2, he2omed2,hespeed2 = pR.histWRanges(2,'he2o',datamin,'Hydrogen')
c2olow2,c2oupp2,c2omed2,cspeed2=pR.histWRanges(2,'c2o',datamin,'Hydrogen')
n2olow2,n2oupp2,n2omed2,nspeed2=pR.histWRanges(2,'n2o',datamin,'Hydrogen')
ne2olow2,ne2oupp2,ne2omed2,nespeed2=pR.histWRanges(2,'ne2o',datamin,'Hydrogen')
mg2olow2,mg2oupp2,mg2omed2,mgspeed2=pR.histWRanges(2,'mg2o',datamin,'Hydrogen')
si2olow2,si2oupp2,si2omed2,sispeed2=pR.histWRanges(2,'si2o',datamin,'Hydrogen')
s2olow2,s2oupp2,s2omed2,sspeed2=pR.histWRanges(2,'s2o',datamin,'Hydrogen')
fe2olow2,fe2oupp2,fe2omed2,fespeed2=pR.histWRanges(2,'fe2o',datamin,'Hydrogen')


he2olow1, he2oupp1, he2omed1,hespeed1 = pR.histWRanges(1,'he2o',datamin,'Hydrogen')
c2olow1,c2oupp1,c2omed1,cspeed1=pR.histWRanges(1,'c2o',datamin,'Hydrogen')
n2olow1,n2oupp1,n2omed1,nspeed1=pR.histWRanges(1,'n2o',datamin,'Hydrogen')
ne2olow1,ne2oupp1,ne2omed1,nespeed1=pR.histWRanges(1,'ne2o',datamin,'Hydrogen')
mg2olow1,mg2oupp1,mg2omed1,mgspeed1=pR.histWRanges(1,'mg2o',datamin,'Hydrogen')
si2olow1,si2oupp1,si2omed1,sispeed1=pR.histWRanges(1,'si2o',datamin,'Hydrogen')
s2olow1,s2oupp1,s2omed1,sspeed1=pR.histWRanges(1,'s2o',datamin,'Hydrogen')
fe2olow1,fe2oupp1,fe2omed1,fespeed1=pR.histWRanges(1,'fe2o',datamin,'Hydrogen')


he2olow3, he2oupp3, he2omed3,hespeed3 = pR.histWRanges(3,'he2o',datamin,'Hydrogen')
c2olow3,c2oupp3,c2omed3,cspeed3=pR.histWRanges(3,'c2o',datamin,'Hydrogen')
n2olow3,n2oupp3,n2omed3,nspeed3=pR.histWRanges(3,'n2o',datamin,'Hydrogen')
ne2olow3,ne2oupp3,ne2omed3,nespeed3=pR.histWRanges(3,'ne2o',datamin,'Hydrogen')
mg2olow3,mg2oupp3,mg2omed3,mgspeed3=pR.histWRanges(3,'mg2o',datamin,'Hydrogen')
si2olow3,si2oupp3,si2omed3,sispeed3=pR.histWRanges(3,'si2o',datamin,'Hydrogen')
s2olow3,s2oupp3,s2omed3,sspeed3=pR.histWRanges(3,'s2o',datamin,'Hydrogen')
fe2olow3,fe2oupp3,fe2omed3,fespeed3=pR.histWRanges(3,'fe2o',datamin,'Hydrogen')


he2olow0, he2oupp0, he2omed0,hespeed0 = pR.histWRanges(0,'he2o',datamin,'Hydrogen')
c2olow0,c2oupp0,c2omed0,cspeed0=pR.histWRanges(0,'c2o',datamin,'Hydrogen')
n2olow0,n2oupp0,n2omed0,nspeed0=pR.histWRanges(0,'n2o',datamin,'Hydrogen')
ne2olow0,ne2oupp0,ne2omed0,nespeed0=pR.histWRanges(0,'ne2o',datamin,'Hydrogen')
mg2olow0,mg2oupp0,mg2omed0,mgspeed0=pR.histWRanges(0,'mg2o',datamin,'Hydrogen')
si2olow0,si2oupp0,si2omed0,sispeed0=pR.histWRanges(0,'si2o',datamin,'Hydrogen')
s2olow0,s2oupp0,s2omed0,sspeed0=pR.histWRanges(0,'s2o',datamin,'Hydrogen')
fe2olow0,fe2oupp0,fe2omed0,fespeed0=pR.histWRanges(0,'fe2o',datamin,'Hydrogen')


#Plots abundance ratios and variances.

#############********************##############

names = ['he2o','c2o','n2o','ne2o','mg2o','si2o','s2o','fe2o']
speeds = ['vhe','vc5','vn5','vne8','vmg10','vsi8','vs8','vfe10']
ylblparams = [[-6,-1,101],[-6,-3,101],[-6,-3.5,101],[-6,-3.5,101],[-5.2,-3.5,101],[-6,-1,101],
              [-6,-1,100], [-6,-1,101]]
reglbls = ['IS+CH','CME','CH','IS']
flagNum = [0,1,2,3]
ind = 0
path = "Users/aa245567/Desktop/"
ymaxparams = [10**(-1.0),10**(-3.00),10.**(-3.5),10**(-3.5),10**(-3.5),10**(-3.0),10**(-3.9),10**(-3.1)]
yminparams = [10**(-2.8),10**(-4.75),10.**(-5.3),10**(-5.4),10**(-5.2),10**(-5.0),10**(-5.3),10**(-5)]
for nm in range(len(names)):
    fig, axs = plt.subplots(2,2,figsize=(15,10))
    axes = np.ravel(axs)
    axind = 0
    for rel in reglbls:
        '''
        if names[nm] == 'n2o' or names[nm] == 's2o':
            x,y = findReg(rel,aswix1d[names[nm]],oneDay = 1)
            x,y = goodBins(x,y)
        
        else:
            '''
        x,y = pR.findReg(abundn[speeds[nm]],rel,abundn[names[nm]])
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
        axes[axind].plot(xbins,bfline,'w-')
        axes[axind].text(0.01,0.01,'Slope = %f +/- %f'%(slope,np.sqrt(covariance[-1][-1]))
        ,verticalalignment='bottom',horizontalalignment='left',transform=axes[axind].transAxes,color='white')
        
        axind += 1
    
    fig.text(0.04,0.6,'%s/H Abundance Ratios'%names[nm][:-2].upper(),rotation='vertical',fontsize='large')
    fig.text(0.5,0,'Solar Wind Speed (km/s)',ha='center',va='center',fontsize='large')
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
fig.suptitle('Elemental Abundance Ratios',fontsize='large')
fig.text(0.5,0,'Solar Wind Speed (km/s)',ha='center',va='center',fontsize='large')
ax0.errorbar(hespeed2 + 5, he2omed2, yerr=[he2olow2, he2oupp2], fmt='bo',label="Coronal Hole")
#ax0.errorbar(hespeed0 + 10,he2omed0[:20],yerr=[he2olow0[:20],he2oupp0[:20]], fmt='ro',label="Bulk")
ax0.errorbar(hespeed1 + 15,he2omed1,yerr=[he2olow1,he2oupp1],fmt='ro',label='CME')
ax0.errorbar(hespeed3 , he2omed3,yerr=[he2olow3,he2oupp3], fmt='go',label="Interstream")
ax0.set_ylabel('He/H',fontweight = 'bold')
ax0.set_yscale('log')
#ax0.set_ylim(ymin=30,ymax=300)

ax0.legend(numpoints=1,loc="lower right")



ax1.errorbar(cspeed2+5, c2omed2, yerr =[c2olow2, c2oupp2], fmt='bo' )
ax1.errorbar(cspeed1+10,c2omed1,yerr=[c2olow1,c2oupp1], fmt='ro')
ax1.errorbar(cspeed3,c2omed3,yerr=[c2olow3,c2oupp3], fmt='go')
#ax1.errorbar(jvel[:20],c2omed0[:25],yerr=[c2olow0[:25],c2oupp0[:25]],fmt='yo')
ax1.set_yscale('log')
ax1.yaxis.set_label_position('right')
ax1.set_ylabel('C/H',fontweight='bold')
#ax1.set_ylim(ymin=0.25,ymax=2.)



ax2.errorbar(nspeed2+5,n2omed2, yerr=[n2olow2,n2oupp2], fmt='bo')
ax2.errorbar(nspeed1+10,n2omed1,yerr=[n2olow1,n2oupp1], fmt='ro')
ax2.errorbar(nspeed3,n2omed3,yerr=[n2olow3,n2oupp3], fmt='go')
#ax2.errorbar(jvel[:20],n2omed0[:25],yerr=[n2olow0[:25],n2oupp0[:25]],fmt='yo')
ax2.set_yscale('log')
ax2.set_ylabel('N/H',fontweight='bold')
#ax2.set_ylim(ymin=0.075,ymax=0.7)



ax3.errorbar(nespeed2+5,ne2omed2,yerr=[ne2olow2,ne2oupp2],fmt='bo')
ax3.errorbar(nespeed1+10,ne2omed1,yerr=[ne2olow1,ne2oupp1], fmt='ro')
ax3.errorbar(nespeed3,ne2omed3,yerr=[ne2olow3,ne2oupp3], fmt='go')
#ax3.errorbar(jvel[:20],ne2omed0[:25],yerr=[ne2olow0[:25],ne2oupp0[:25]],fmt='yo')
ax3.set_yscale('log')
ax3.yaxis.set_label_position('right')
ax3.set_ylabel('Ne/H',fontweight='bold')
#ax3.set_ylim(ymin=0.06,ymax=0.6)



ax4.errorbar(mgspeed2+5,mg2omed2,yerr=[mg2olow2,mg2oupp2],fmt='bo')
ax4.errorbar(mgspeed1+10,mg2omed1,yerr=[mg2olow1,mg2oupp1], fmt='ro')
ax4.errorbar(mgspeed3,mg2omed3,yerr=[mg2olow3,mg2oupp3], fmt='go')
#ax4.errorbar(jvel[:20],mg2omed0[:25],yerr=[mg2olow0[:25],mg2oupp0[:25]],fmt='yo')
ax4.set_yscale('log')
ax4.set_ylabel('Mg/H',fontweight='bold')
#ax4.set_ylim(ymin=0.05,ymax=0.5)



ax5.errorbar(sispeed2+5,si2omed2,yerr=[si2olow2,si2oupp2],fmt='bo')
ax5.errorbar(sispeed1+10,si2omed1,yerr=[si2olow1,si2oupp1], fmt='ro')
ax5.errorbar(sispeed3,si2omed3,yerr=[si2olow3,si2oupp3], fmt='go')
#ax5.errorbar(jvel[:20],si2omed0[:25],yerr=[si2olow0[:25],si2oupp0[:25]],fmt='yo')
ax5.set_yscale('log')
ax5.yaxis.set_label_position('right')
ax5.set_ylabel('Si/H',fontweight='bold')
#ax5.set_ylim(ymin=0.05,ymax=0.5)



ax6.errorbar(sspeed2+5,s2omed2,yerr=[s2olow2,s2oupp2],fmt='bo')
ax6.errorbar(sspeed1+10,s2omed1,yerr=[s2olow1,s2oupp1], fmt='ro')
ax6.errorbar(sspeed3,s2omed3,yerr=[s2olow3,s2oupp3], fmt='go')
#ax6.errorbar(jvel[:20],s2omed0[:25],yerr=[s2olow0[:25],s2oupp0[:25]],fmt='yo')
ax6.set_yscale('log')
ax6.set_ylabel('S/H',fontweight='bold')
#ax6.set_ylim(ymin=0.025)



ax7.errorbar(fespeed2+5,fe2omed2,yerr=[fe2olow2,fe2oupp2],fmt='bo')
ax7.errorbar(fespeed1+10,fe2omed1,yerr=[fe2olow1,fe2oupp1], fmt='ro')
ax7.errorbar(fespeed3,fe2omed3,yerr=[fe2olow3,fe2oupp3], fmt='go')
#ax7.errorbar(jvel[:20],fe2omed0[:25],yerr=[fe2olow0[:25],fe2oupp0[:25]],fmt='yo')
ax7.set_yscale('log')
ax7.yaxis.set_label_position('right')
ax7.set_ylabel('Fe/H',fontweight='bold')
#ax7.set_ylim(ymin=0.07 ymax = )


plt.show()

