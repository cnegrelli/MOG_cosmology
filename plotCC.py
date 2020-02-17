import math
import numpy as np
from numpy.linalg import inv
import  matplotlib.pyplot as mp
from scipy import optimize
from scipy.integrate import simps
# leo la tabla de datos:
zobs,Hobs,eHobs=np.loadtxt('Hz.dat',unpack=True)
#teoricas:
z, H11 = np.loadtxt('H6737_0.dat', unpack=True)
z, H12 = np.loadtxt('H6737++.dat', unpack=True)
z, H13 = np.loadtxt('H6737--.dat', unpack=True)
z, H15 = np.loadtxt('H6737.dat', unpack=True)
z, H18 = np.loadtxt('H6737+25.dat', unpack=True)
z1, H21 = np.loadtxt('H7200.dat', unpack=True)
z, H32 = np.loadtxt('H7348--.dat', unpack=True)
z, H35 = np.loadtxt('H7348.dat', unpack=True)
z, H37 = np.loadtxt('H7348++.dat', unpack=True)
z, H38 = np.loadtxt('H7348_0.dat', unpack=True)
H01=67.37*3.154e7/(3.086e19)
H02=72.00*3.154e7/(3.086e19)
H03=73.48*3.154e7/(3.086e19)
Hz11=(1.0/H11)*H01*3.086e19/3.154e7
Hz12=(1.0/H12)*H01*3.086e19/3.154e7
Hz13=(1.0/H13)*H01*3.086e19/3.154e7
Hz15=(1.0/H15)*H01*3.086e19/3.154e7
Hz18=(1.0/H18)*H01*3.086e19/3.154e7
Hz21=(1.0/H21)*H02*3.086e19/3.154e7
Hz32=(1.0/H32)*H03*3.086e19/3.154e7
Hz35=(1.0/H35)*H03*3.086e19/3.154e7
Hz37=(1.0/H37)*H03*3.086e19/3.154e7
Hz38=(1.0/H38)*H03*3.086e19/3.154e7
#para el modelo estandar
Om=0.299
OL=1-0.299
H0s=69.013
Hzs=H0s*np.sqrt(Om*(1+z)**(3.)+OL)
#plot
#las dos lineas sigientes son para usar latex
mp.figure(figsize=(8,5))
mp.rc('text', usetex=True)
mp.rc('font', family='serif')
mp.errorbar(zobs,Hobs,yerr=eHobs, fmt='.', label='Cronometros cosmicos')
mp.plot(z,Hz12, '-.', label=r'$H_0=67.37$, $V_G+20\%$, $\tilde{\chi}^2=1.94$')
mp.plot(z,Hz15, '-.', label=r'$H_0=67.37$, $V_G$, $\tilde{\chi}^2=0.53$')
mp.plot(z,Hz13, '-.', label=r'$H_0=67.37$, $V_G-20\%$, $\tilde{\chi}^2=0.78$')
mp.plot(z,Hz11, '-.', label=r'$H_0=67.37$, $V_G=0$, $\tilde{\chi}^2=7.87$')
#mp.plot(z,Hz18, '-.', label='H0=67.37, Vg=+25')
#mp.plot(z1,Hz21, '--', label='H0=72.00, Vg')
mp.plot(z,Hz37, label=r'$H_0=73.48$, $V_G+20\%$, $\tilde{\chi}^2=0.71$')
mp.plot(z,Hz35, label=r'$H_0=73.48$, $V_G$, $\tilde{\chi}^2=1.71$')
mp.plot(z,Hz32, label=r'$H_0=73.48$, $V_G-20\%$, $\tilde{\chi}^2=3.41$')
mp.plot(z,Hz38, label=r'$H_0=73.48$, $V_G=0$, $\tilde{\chi}^2=13.64$')
mp.plot(z,Hzs,  '--', color='brown', label=r'$\Lambda {\rm CDM}$ $H_0=69.01$, $\Omega_m=0.299$, $\tilde{\chi}^2=0.74$')
mp.legend(loc='upper left', fontsize = 'small')
mp.xlim(0,2.1)
mp.ylim(25,425)
mp.xlabel('$z$')
mp.ylabel('$H(z)$')
#mp.ylim(0,1.5)
mp.savefig('comparacionH.ps')
