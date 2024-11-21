import numpy as np


A = np.matrix([[4, 3],
              [1, 2]])

autov_A = np.linalg.eig(A)

#Apresenta tanto autovalores como autovetores
print(autov_A)
print('\n') 

#Autovalores
print(autov_A[0])
print('\n')

#Primeiro autovalor
print(autov_A[0][0])
print('\n')

#Segundo autovalor
print(autov_A[0][1])
print('\n')

#Autovetores
print(autov_A[1])
print('\n')

#Primeiro autovetor
print(autov_A[1][:,0])
print('\n')

#Segundo autovetor
print(autov_A[1][:,1])
print('\n')

#Primeiro autovetor normalizado
print(autov_A[1][:,0]/autov_A[1][1,0])
print('\n')

#Segundo autovetor normalizado
print(autov_A[1][:,1]/autov_A[1][1,1])
print('\n')

#Matriz Diagonal
print(np.diag(autov_A[0]))