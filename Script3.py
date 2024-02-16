# https://matplotlib.org/stable/users/installing/index.html
# https://matplotlib.org/stable/users/explain/quick_start.html
# https://stackoverflow.com/questions/29550124/pythons-attributeerror-module-object-has-no-attribute-require-version
# https://matplotlib.org/stable/users/getting_started/index.html

# import matplotlib as mpl
# Usamos `.pyplot.figure` para crear la Figura
import matplotlib.pyplot as plt
import numpy as np

"""
plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
"""

"""
# Datos de la muestra
x = np.linspace(0,2,100)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# Traza algunos datos en los ejes.
ax.plot(x,x,label='linear')
# Añade una etiqueta x a los ejes.
ax.set_xlabel('x label')
# Añade una etiqueta y a los ejes.
ax.set_ylabel('y label')
# Añade un título a los ejes.
ax.set_title("Simple Plot") 
# Añade una leyenda.
ax.legend() 

plt.show()
"""

#"""
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
#"""