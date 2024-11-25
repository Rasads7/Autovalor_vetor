import numpy as np

# Matriz 4x4
A = np.matrix([[0, 0, 1, 0],
               [0, 0, 0, 1],
               [1, 0, 0, 0],
               [0, 1, 0, 0]])

# Cálculo dos autovalores e autovetores
autov_A = np.linalg.eig(A)

# Apresenta tanto autovalores como autovetores
print("Autovalores e Autovetores:\n", autov_A)
print('\n')

# Autovalores
print("Autovalores:\n", autov_A[0])
print('\n')

# Primeiro autovalor
print("Primeiro autovalor:\n", autov_A[0][0])
print('\n')

# Segundo autovalor
print("Segundo autovalor:\n", autov_A[0][1])
print('\n')

# Terceiro autovalor
print("Terceiro autovalor:\n", autov_A[0][2])
print('\n')

# Quarto autovalor
print("Quarto autovalor:\n", autov_A[0][3])
print('\n')

# Autovetores
print("Autovetores:\n", autov_A[1])
print('\n')

# Primeiro autovetor
print("Primeiro autovetor:\n", autov_A[1][:, 0])
print('\n')

# Segundo autovetor
print("Segundo autovetor:\n", autov_A[1][:, 1])
print('\n')

# Terceiro autovetor
print("Terceiro autovetor:\n", autov_A[1][:, 2])
print('\n')

# Quarto autovetor
print("Quarto autovetor:\n", autov_A[1][:, 3])
print('\n')

'''# Primeiro autovetor normalizado
print("Primeiro autovetor normalizado:\n", autov_A[1][:, 0] / autov_A[1][1, 0])
print('\n')

# Segundo autovetor normalizado
print("Segundo autovetor normalizado:\n", autov_A[1][:, 1] / autov_A[1][1, 1])
print('\n')'''

# Terceiro autovetor normalizado
print("Primeiro autovetor normalizado:\n", autov_A[1][:, 2] / autov_A[1][1, 2])
print('\n')

# Quarto autovetor normalizado
print("Segundo autovetor normalizado:\n", autov_A[1][:, 3] / autov_A[1][1, 3])
print('\n')

# Matriz Diagonal
print("Matriz Diagonal (autovalores):\n", np.diag(autov_A[0]))