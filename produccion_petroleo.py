#!/usr/bin/env python
# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('SENER_05_ProduccionPetroleo.csv')

AS01 = data.iloc[1]
AS02 = data.iloc[11]
SUR = data.iloc[27]                 
NORTE = data.iloc[37]
                 
                 
AS01 = pd.to_numeric(AS01, errors='coerce').fillna(0, downcast='infer')
AS02 = pd.to_numeric(AS02, errors='coerce').fillna(0, downcast='infer')
SUR = pd.to_numeric(SUR, errors='coerce').fillna(0, downcast='infer')
NORTE = pd.to_numeric(NORTE, errors='coerce').fillna(0, downcast='infer')

fig, ax = plt.subplots(figsize=(10,10))
p1 = AS01.plot(color='peru', linewidth=0.7)
p2 = AS02.plot(color='blue', linewidth=0.7)
p3 = SUR.plot(color='forestgreen', linewidth=0.7)
p4 = NORTE.plot(color='red', linewidth=0.7)
plt.legend(loc='upper right')
plt.title('Producción de petróleo crudo del 2005-2018 (miles de barriles)', fontweight='bold')
plt.grid()
plt.show()