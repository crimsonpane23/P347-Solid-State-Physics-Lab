import numpy as np
import matplotlib.pyplot as plt



#Monoatomic lattice C = 149.28 nF, L = 0.974mH
x = np.array([0,90,180,270,360,450,540,630,720,810,900,990,1080,1170,1260,1350,1440])
x = x/10
y = np.array([0.025,1.695,3.80,5.75,7.90,9.85,11.80,13.70,15.55,17.30,19.00,20.60,22.10,23.45,24.75,25.90,27.05])

plt.plot(x,y, label='data points')
plt.grid()
plt.legend()
plt.title('Monoatomic Lattice Vibration')
plt.xlabel('Phase difference per unit cell(ϕ) (degrees)')
plt.ylabel('Frequency (f) (kHz)')
plt.show()

#Monoatomic lattice C = 48.02 nF, L = 0.974mH
x = np.array([0,90,180,270,360,450,540,630,720,810,900,990,1080,1178,1255,1340])
x = x/10
y = np.array([0.025,3.25,7.00,10.65,14.35,17.70,21.30,24.65,27.95,31.00,34.0,36.5,39.0,41.5,43.5,45.5])

plt.plot(x,y, label='data points')
plt.grid()
plt.legend()
plt.title('Monoatomic Lattice Vibration')
plt.xlabel('Phase difference per unit cell(ϕ) (degrees)')
plt.ylabel('Frequency (f) (kHz)')
plt.show()

#Diatomic lattice C = 48.02 nF, L = 0.974mH
x = np.array([0,90,180,270,360,450,540,630,720,810,990,1080,1160,1240,1370,1450])
x = x/10
y = np.array([0.025,2.075,4.505,6.95,9.25,11.55,13.75,15.70,17.65,19.55,33.5,35.0,36.0,37.0,38.5,39.5])
print(x[10:], y[10:])
plt.plot(x[:10],y[:10], label='Acoustic Branch')
plt.plot(x[10:],y[10:], label='Optical Branch')
plt.grid()
plt.legend()
plt.title('Diatomic Lattice Vibration')
plt.xlabel('Phase difference per unit cell(ϕ) (degrees)')
plt.ylabel('Frequency (f) (kHz)')
plt.show()