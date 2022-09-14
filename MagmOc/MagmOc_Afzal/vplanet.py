#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:46:25 2022

@author: afzal-admin
"""

import matplotlib.pyplot as plt


t_solid = [989089.521231,2116618.153073,16275976.898562,46592358.174270,54979000.000000,54997885.461145,54996000,54992000,54997000,54996000] #solidification time [years]
TO       = [0.5,1,5,10,15,20,25,50,75,100] #terristrial ocean [Earth equivalent]


plt.figure(figsize=(8,10))
plt.semilogy(TO,t_solid,'r-')
plt.xlabel('Terrestrial ocean')
plt.ylabel('Solidification time [years]')

plt.savefig(f'TO_vs_T_solid.pdf',bbox_inches='tight', dpi = 600)
