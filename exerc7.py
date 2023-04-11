import numpy as np;

dieimes_matriz = np.array([[3, 4, 5],[6, 7, 8]]);

soma_extra = np.sum(dieimes_matriz);

soma = 0;

for i in dieimes_matriz:
    for l in i:
        soma += l;

print(f"Soma com for: {soma} ;\nsoma com numpy: {soma_extra} ;");