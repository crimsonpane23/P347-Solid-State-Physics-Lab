import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r'6. Phase Transitions of BaTiO3\table1.csv')
C4 = data['C4'].values
R4 = data['R4'].values
f = data['f'].values
R3 = 1000           #ohm
C2 = 1000           #pF
r = (10.56e-3)/2    #m
t = 1.6e-3          #m
C1 = C2*R4/(R3/1000) #pF

data['C1'] = C1
R1 = R3*C4/C2       #ohm

data['R1'] = R1  #ohm

C0 = (8.854e-12)*(np.pi*(r**2)/t)/1e-12     #pF
print(C0,'pF')
data['Dielectric constant'] = C1/C0

#Temperature variation for Different frquencies 
T = np.array([50,60,70,80,90,100,110,120,125,130,135,140,150,168])

#OP f = 15kHz
R4_15kHz = np.array([0.876,0.892,0.922,0.964,1.010,1.094,1.210,1.398,1.532,1.680,1.772,1.744,1.528,1.202])
C4_15kHz = np.array([350,350,400,500,500,600,600,650,750,950,600,1150,1150,400])
C1_15kHz = C2*R4_15kHz/(R3/1000)
E_15kHz = C1_15kHz/C0
print(np.round(E_15kHz,1))

#OP f = 25kHz
R4_25kHz = np.array([0.866,0.884,0.916,0.952,1.002,1.082,1.184,1.372,1.498,1.606,1.736,1.684,1.484,1.174])
C4_25kHz = np.array([200,250,250,250,350,350,450,400,600,600,850,1100,400])
C1_25kHz = C2*R4_25kHz/(R3/1000)
E_25kHz = C1_25kHz/C0
print(np.round(E_25kHz,1))


#OP f = 35kHz
R4_35kHz = np.array([0.862,0.878,0.910,0.948,0.996,1.066,1.170,1.348,1.460,1.592,1.720,1.682,1.466,1.170])
C4_35kHz = np.array([150,200,200,200,350,350,300,350,450,450,500,750,900,400])
C1_35kHz = C2*R4_35kHz/(R3/1000)
E_35kHz = C1_35kHz/C0
print(np.round(E_35kHz,1))

#OP f = 45kHz
R4_45kHz = np.array([0.858,0.874,0.906,0.942,0.996,1.060,1.166,1.334,1.440,1.556,1.690,1.624,1.428,1.152])
C4_45kHz = np.array([150,150,150,150,250,250,300,450,350,750,700,400])
C1_45kHz = C2*R4_45kHz/(R3/1000)
E_45kHz = C1_45kHz/C0
print(np.round(E_45kHz,1))


#Plotting temperature variations of dielectric constant for various frequencies

plt.figure()
plt.plot(T, E_15kHz, label='15kHz', marker='x')
plt.plot(T, E_25kHz, label='25kHz', marker='o')
plt.plot(T, E_35kHz, label='35kHz', marker='v')
plt.plot(T, E_45kHz, label='45kHz', marker='*')
plt.xlabel('Temperature')
plt.ylabel('Dielectric constant')
plt.grid()
plt.legend()
plt.show()