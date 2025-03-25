import numpy as np
import pandas as pd

np.random.seed(42)

# 1. Gerar população de 10 mil idades
populacao = np.random.randint(low=0, high=111, size=10000)
df_populacao = pd.DataFrame(populacao, columns=['idade'])
df_populacao.to_csv('populacao.csv', index=False)

# 2. Calcular tamanho da amostra
N = len(df_populacao)  
E0 = 0.05              

n0 = 1 / (E0 ** 2)
n = int(round((N * n0) / (N + n0)))  

# Mostrar resultados
print(f"Primeira aproximação (n0): {n0:.0f}")
print(f"Tamanho da amostra (n): {n}")

# 3. Gerar amostra com erro
amostra = df_populacao.sample(n=n, random_state=42)

qtd_erros = (int(round(n * 0.05)))

indices_erro = np.random.choice(amostra.index, size=qtd_erros, replace=False)

amostra.loc[indices_erro, 'idade'] = np.random.randint(0, 111, size=qtd_erros)

amostra.to_csv('amostra.csv', index=False)