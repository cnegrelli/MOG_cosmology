#en este programa vamos a calcular el chi2 MOG-sn considerando todos los parametros fijos. Solo hay que prestarle atencion al valor de H0.
import math
import numpy as np
from numpy.linalg import inv
import  matplotlib.pyplot as mp
#Ojo que el valor de H0 esta puesto a mano!tiene que ser el mismo que el del mathe que genero la tabla que se lee mas abajo
H0=73.48*3.154e7/(3.086e19)
#leo la tabla de la funcion que tengo que integrar que viene del mathematica (donde tambien use H0). en la tabla esta: 1/(H/H0)=H0/H 
z, Integ = np.loadtxt('H7348_0.dat', unpack=True)
# como queremos H hay que invertir y multiplicar por H0. y convertir de nuevo a las unidades tipicas de H que es como viene la tabla
Hz=(1.0/Integ)*H0*3.086e19/3.154e7
# leo la tabla de datos:
zobs,Hobs,eHobs=np.loadtxt('CC.dat',unpack=True)
#calculo chi2. me falta ver que elemento hacer corresponder de la tabla! o sea en cual valor tengo que evaluar a Hz[i]!!!
chi2=0.0
chi2a=np.zeros(len(zobs))
for i in range(len(zobs)):	
    j=int(round(zobs[i]/0.00001))
    chi2a = ((Hobs[i]-Hz[j])/eHobs[i])**2;
    chi2+=chi2a;
#chequeado que esta agarrando bien cada valor de H teorico correspondiente al observado
print(chi2, len(zobs),chi2/len(zobs))
#graficos
mp.errorbar(zobs,Hobs,yerr=eHobs, fmt='.')
mp.plot(z,Hz)
mp.savefig('comparacion.pdf')
#mp.clf()
#mp.plot(zcmb,(muth-muobs)/muobs,'r.')
#mp.savefig('diferencias7348.pdf')

