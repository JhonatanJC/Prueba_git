print("Hola mundo, estoy aprendiendo a usar git.")
print("ESTE ES EL PRIMER CAMBIO PARA ESTE CODIGO :D")

import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(-5,5,1000)
def f(x):
    return np.cos(x)
plt.plot(x,f(x),"r",label="Funcion ")
plt.legend(loc=2)
plt.grid()
plt.show()

