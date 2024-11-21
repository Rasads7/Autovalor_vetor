import numpy as np

V = np.array([[8,-2],
              [-2,5]])

#Autovalores e autovetores
v1, v2 = np.linalg.eig(V)

# Normalizando os autovetores
v2_normalizados = v2 / v2[-1, :]

#Autovalor
print(v1)
print('\n')
#Autovetor
print(v2)
print('\n')
#Autovetor normalizado
print(v2_normalizados)
print('\n')

#Matriz diagonal
v3 = np.diag(v1)
print(v3)