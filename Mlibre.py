#en este programa vamos a calcular el chi2 MOG-sn considerando alfa y beta parametros fijos pero Mabs libre. Ojo que tenemos un dof menos. Hay que prestarle atencion al valor de H0 y de Vg.
import math
import numpy as np
from numpy.linalg import inv
import  matplotlib.pyplot as mp
from scipy import optimize
c=3.0e8*3.154e7
#Ojo que el valor de H0 esta puesto a mano!tiene que ser el mismo que el del mathe que genero la tabla que se lee mas abajo
H0=67.37*3.154e7/(3.086e19)
conv=1000000*3.0857e16
#leo la tabla de la funcion que tengo que integrar que viene del mathematica (donde tambien use H0)
z, Integrando = np.loadtxt('H6737+++.dat', unpack=True)
# ya chequee graficamente que el archivo se estuviera leyendo bien
# leo la tabla de datos:
zcmb,zhel,dz,mb,dmb=np.loadtxt('lcparam_full_long_zhel.txt', usecols=(1,2,3,4,5),unpack=True)
# ya chequee graficamente que el archivo se estuviera leyendo bien
#creamos la matriz diagonal con los errores de mB. ojo! esto depende de alfa y beta:
Dstat=np.diag(dmb**2.)
# hay que leer la matriz de los errores sistematicos que es de NxN
sn=len(zcmb)
Csys=np.loadtxt('lcparam_full_long_sys.txt',unpack=True)
Csys=Csys.reshape(sn,sn)
#armamos la matriz de cov final y la invertimos:
Ccov=Csys+Dstat
Cinv=inv(Ccov)
from scipy.integrate import simps
#longitud de la tabla de sn:
muth=np.zeros(sn)
#para cada sn voy a hacer la integral correspondiente:
#lo que hago es cortar la lista en el limite superior de la integral que me lo da zcmb.
for i in range(0,sn):
	j=int(round(zcmb[i]/0.00001))
	Intj=Integrando[:j]
	zj=z[:j]
	muth[i] = 25.0+5.0*math.log10((1+zhel[i])*(c/H0)*simps(Intj, zj)/conv)
#chequeado de forma grafica comparando con el mathe y con algunos puntos de forma analitica.
#ya tengo el calculo del modulo de distancia teorico para cada supernova.
#Ahora nos falta el observado que depende de Mabs y lo hacemos variar.
Mabs=np.linspace(-18.8,-20.0,20)
chi2=np.zeros(20)
for k in range(20):
	muobs=mb-Mabs[k]
	deltamu=muobs-muth
	transp=np.transpose(deltamu)
	chi2[k]=np.dot(np.dot(transp,Cinv),deltamu)
	#print(Mabs[k],chi2[k],chi2[k]/(sn-1))
#print(Mabs,chi2/sn)
#chequeado que esto esta funcionando bien
#graficos
#mp.plot(Mabs,chi2,'r.')
#mp.savefig('Mabsvschi27348.pdf')
#efectivamente da una parabola (el grafico lo hace mas abajo con el ajuste ya hecho)
#ajustamos un polinomio de grado dos a la parabola y buscamos el minimo
fit=np.polyfit(Mabs,chi2,2) #esto me devuelve un array con a,b,c
pol=np.poly1d(fit) #esto me lo convierte para poder evaluar el pol
Mmin = optimize.fmin(pol, -19)
#Mmin[0] es el minimo en Mabs. y pol(Mmin[0]) el valor del chi2 en el minimo
#ahora hay que encontrar el error. hay que sumarle 1.00 al chi2 de acuerdo a la tabla de la pg 815 del numerical recipies.
chi2sigma=pol(Mmin[0])+1.00
#ahora hay que encontrar el Mabs asociado a este valor de chi2. depejo la cuadratica considerando c=c-chi2sigma
Mabssigma=(-fit[1]+math.sqrt((fit[1]**2.-4.0*fit[0]*(fit[2]-chi2sigma))))/(2.0*fit[0])
print(Mmin[0],abs(Mabssigma-Mmin[0]),pol(Mmin[0]),pol(Mmin[0])/(sn-1) ) #escribo el minimo, la desviacion a 1 sigma  y el chi2 minimo y el reducido
#plot
xp=np.linspace(-18.8,-20.0,100)
mp.plot(Mabs,chi2,'r.',xp,pol(xp),'-')
mp.savefig('Mabsvschi6737+++.pdf')
#pendientes: combinar las tablas .fits con el zhel de esta tabla. 
#		hacer el calculo de chi2 con los tres parametros y buscar los valores que lo minimizan
