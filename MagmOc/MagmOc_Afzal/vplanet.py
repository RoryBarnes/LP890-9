#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:46:25 2022

@author: afzal-admin
"""

import matplotlib.pyplot as plt


plt.figure(figsize=(8,10))
#Mass = 2.5
t_solid = [989089.521231,2116618.153073,16275976.898562,46592358.174270,54979000.000000,54997885.461145,54996000,54992000,54997000,54996000] #solidification time [years]
TO       = [0.5,1,5,10,15,20,25,50,75,100] #terristrial ocean [Earth equivalent]
plt.loglog(TO,t_solid,'r-',label=r'$2.5M_\oplus$')



#Mass = 5
t_solid = [1569659.408108, 3375057.920923, 24702805.139166, 62228086.717167, 54564000, 54563000, 54561000, 54565000, 54565000, 54565000] #solidification time [years]
TO       = [0.5,1,5,10,15,20,25,50,75,100] #terristrial ocean [Earth equivalent]


plt.loglog(TO,t_solid,'g-',label=r'$5M_\oplus$')
plt.xlabel('Terrestrial ocean')
plt.ylabel('Solidification time [years]')



#Mass = 10
t_solid = [1597458.192696, 3350309.787952, 20952591.713280, 45337428.356931, 53830775.678055, 53831000, 53831000,53832000, 53832775.875276 ] #solidification time [years]
TO       = [0.5,1,5,10,15,20,25,50,100] #terristrial ocean [Earth equivalent]

plt.loglog(TO,t_solid,'b-',label=r'$10M_\oplus$')


#Mass = 25.3
t_solid = [1335062.337452, 2964736.251365, 30037799.848044, 51795000, 51800000, 51801000, 51802000, 51802000, 51802000] #solidification time [years]
TO       = [0.5,1,5,10,15,20,25,50,100] #terristrial ocean [Earth equivalent]

plt.loglog(TO,t_solid,'k-',label=r'$25.3M_\oplus$')

plt.xlabel('Terrestrial ocean')
plt.ylabel('Solidification time [years]')
plt.legend(loc='best')
plt.savefig(f'TO_vs_T_solid.pdf',bbox_inches='tight', dpi = 600)