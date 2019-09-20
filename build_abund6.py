#Author AndrewAmmons

#Normalize GIM data to ACE/SWICS 2 hour time bins.

import numpy as np
import aswics2python_unknown2dnum as apu 

gim_mom = np.load('/Users/aa245567/Desktop/pythonstuff/gim_mom_sav.npy')
aswix = np.load('/Users/aa245567/Desktop/pythonstuff/aswics_sav.npy')
swepam = np.load('/Users/aa245567/Desktop/pythonstuff/swepam_sav.npy')

#photospheric abundnaces relative to photospheric oxygen.
PhotoAbundO = {'he2o':174.0,
               'c2o':0.550,
               'n2o':0.138,
               'ne2o':0.174,
               'mg2o':0.0813,
               'si2o':0.0661,
               's2o':0.0269,
               'fe2o':0.0646}

#Define Genesis start and end times (day number 699 to dnum 1552).
d_start = round(min(gim_mom['dnum']))
d_end = round(max(gim_mom['dnum']))

#Select ACE data for Genesis period.
abundn = aswix[np.where((aswix['dnum'] >= d_start) & (aswix['dnum'] <= d_end))]
swep = swepam[np.where((swepam['dnum'] >= d_start) & (swepam['dnum'] <= d_end))]

lngth = len(abundn) #Assign array length.
regime = np.zeros((lngth,),dtype=[('dnum','d'),('v_p','d'),('n_p','d'),('t_p','d'),('he2p','d'),('flag', 'i2')])

#Average GIM data to two hour values and store in regime struct.

for i in range(len(abundn)-1):
    #find the GIM data >= the current abundn time and
    #< the next one:
    drp = np.where((swep['dnum'] >= abundn['dnum'][i]) & (swep['dnum'] < abundn['dnum'][i+1]) & (swep['prot_spd'] > 0.0) 
                    & (swep['prot_den'] > 0.0) & (swep['prot_temp'] > 0.0))
    if np.size(drp) > 0:
        regime['dnum'][i] = abundn['dnum'][i]
        regime['v_p'][i] = (np.average(swep['prot_spd'][drp]))
        regime['n_p'][i] = (np.average(swep['prot_den'][drp]))
        regime['t_p'][i] = (np.average(swep['prot_temp'][drp]))
        regime['he2p'][i] = (np.average(swep['he42p'][drp]))
        regime['dnum'][i+1] = abundn['dnum'][i+1]

# open regime time files: 
c_h = np.loadtxt('/Users/aa245567/Desktop/pythonstuff/GNS_CH.txt',skiprows=2)
cme = np.loadtxt('/Users/aa245567/Desktop/pythonstuff/GNS_CME.txt',skiprows=2)
i_s = np.loadtxt('/Users/aa245567/Desktop/pythonstuff/GNS_IS.txt',skiprows=2)

#Fit regime numbers to data and add flag to regime struct array: 

for i in range(len(c_h)):
    ig = ((regime['dnum'] >= apu.unknown2dnum(c_h[i][:2])+(2./24)) & (regime['dnum'] <= apu.unknown2dnum(c_h[i][2:4])))
    regime['flag'][ig] = 2 
for i in range(len(cme)):
    ig = ((regime['dnum'] >= apu.unknown2dnum(cme[i][:2])+(2./24)) & (regime['dnum'] <= apu.unknown2dnum(cme[i][2:4])))
    regime['flag'][ig] = 1
for i in range(len(i_s)):
    ig = ((regime['dnum'] >= apu.unknown2dnum(i_s[i][:2])+(2./24)) & (regime['dnum'] <= apu.unknown2dnum(i_s[i][2:4])))
    regime['flag'][ig] = 3  
    
#fractionation factor array contains: Fractionation factor, 
#and regime number for corresponding species.
#############********************##############
#finding the fractionation factor:   
#     fip = ((|Mg| + |si| + |s| + |fe|)
#           --------------------------
#            (|C| + |N| + |O| + |Ne|))   <--Solar Wind
#      -----------------------------------
#           ((|Mg| + |Si| + |S| + |Fe|)
#           --------------------------
#            (|C| + |N| + |O| + |Ne|))   <--Photosphere
#flags correspond to regime as 0 = bulk (which we dont use), 1 = cme, 2 = ch, 3 = is 

fractor = []
flag = []
v_p = []


for i in range(4):
    for j,k in zip(abundn[np.where(regime['flag'] == i)],regime[np.where(regime['flag'] == i)]):
        fracfactor = ((j['mg2o'] + j['si2o'] + j['s2o'] + j['fe2o'])/\
                      (j['c2o'] + j['n2o'] + j['ne2o'] + 1.0))/\
                      ((PhotoAbundO['mg2o'] + PhotoAbundO['si2o'] + PhotoAbundO['s2o'] + PhotoAbundO['fe2o'])/\
                       (PhotoAbundO['c2o'] + PhotoAbundO['n2o'] + PhotoAbundO['ne2o'] + 1.0))
        fractor.append(fracfactor)
        flag.append(i)
        v_p.append(k['v_p'])
        
        
fractor = np.array(fractor)
flag = np.array(flag)
v_p = np.array(v_p)
        
#fractorray = np.array([(fractor),(flag),(dnum)],dtype = [('FracFactor',float), ('flag',int), ('dnum',float)])

fractorray = np.recarray((len(fractor),), dtype = [('fracfactor',float), ('flag',int), ('v_p',float)])

for x,i,j,k in zip(range(len(fractor)),fractor,flag,v_p):
    fractorray['fracfactor'][x] = i
    fractorray['flag'][x] = j
    fractorray['v_p'][x] = k


#Save that stuff! :
np.save('/Users/aa245567/Desktop/pythonstuff/fractorray',fractorray)
np.save('/Users/aa245567/Desktop/pythonstuff/abund_struct',abundn)
np.save('/Users/aa245567/Desktop/pythonstuff/regime_struct',regime)
