import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


dados_reais = [1.692, 2.933, 3.343, 4.069, 5.946, 6.244, 7.249, 8.792, 9.111, 10.849, 
               11.833, 12.376, 13.555, 14.423, 15.148, 16.811, 17.537, 18.583, 19.385, 
               20.102, 21.526, 22.810, 23.326, 24.898, 25.820, 26.589, 27.152, 28.705, 
               29.613, 30.390, 31.104, 32.730, 33.481, 34.011, 35.287, 36.952, 37.507, 
               38.550, 39.113, 40.065]

modelo_1 = [5.039, 5.466, 6.514, 6.034, 8.419, 8.122, 10.374, 11.396, 12.167, 13.425, 
            15.250, 15.188, 16.833, 16.211, 18.222, 19.406, 20.805, 21.291, 21.577, 
            22.051, 23.788, 24.405, 25.489, 26.449, 29.231, 29.295, 30.228, 30.353, 
            32.920, 33.195, 34.155, 35.365, 35.722, 37.005, 38.430, 39.476, 39.760, 
            40.275, 42.170, 42.033]

modelo_2 = [8.270, 5.929, 6.598, 3.418, 14.936, 3.929, 9.620, 1.267, 10.166, 2.782, 
            19.751, 8.802, 18.830, 10.406, 16.557, 9.106, 22.635, 13.047, 23.038, 
            19.136, 26.519, 15.113, 26.422, 16.370, 33.615, 20.990, 28.595, 22.005, 
            35.437, 26.685, 32.088, 25.796, 38.055, 33.909, 38.012, 27.912, 42.320, 
            33.324, 40.187, 39.446]


df = pd.DataFrame({
    'Dado Real': dados_reais,
    'Modelo 1': modelo_1,
    'Modelo 2': modelo_2
})


df['Erro Modelo 1'] = df['Modelo 1'] - df['Dado Real']
df['Erro Modelo 2'] = df['Modelo 2'] - df['Dado Real']


df['Erro Absoluto Modelo 1'] = np.abs(df['Erro Modelo 1'])
df['Erro Absoluto Modelo 2'] = np.abs(df['Erro Modelo 2'])


df['Erro Quadrático Modelo 1'] = df['Erro Modelo 1'] ** 2
df['Erro Quadrático Modelo 2'] = df['Erro Modelo 2'] ** 2


def calcular_moda(serie):
    try:
        
        return stats.mode(serie, keepdims=False).mode
    except TypeError:
        try:
            
            return stats.mode(serie).mode[0]
        except:
            
            return stats.mode(serie)[0][0]


medidas_erro_m1 = {
    'Média': df['Erro Modelo 1'].mean(),
    'Mediana': df['Erro Modelo 1'].median(),
    'Moda': calcular_moda(df['Erro Modelo 1']),
    'Mínimo': df['Erro Modelo 1'].min(),
    'Máximo': df['Erro Modelo 1'].max(),
    'Primeiro Quartil': df['Erro Modelo 1'].quantile(0.25),
    'Terceiro Quartil': df['Erro Modelo 1'].quantile(0.75)
}

medidas_erro_m2 = {
    'Média': df['Erro Modelo 2'].mean(),
    'Mediana': df['Erro Modelo 2'].median(),
    'Moda': calcular_moda(df['Erro Modelo 2']),
    'Mínimo': df['Erro Modelo 2'].min(),
    'Máximo': df['Erro Modelo 2'].max(),
    'Primeiro Quartil': df['Erro Modelo 2'].quantile(0.25),
    'Terceiro Quartil': df['Erro Modelo 2'].quantile(0.75)
}


dispersao_erro_m1 = {
    'Amplitude': df['Erro Modelo 1'].max() - df['Erro Modelo 1'].min(),
    'Variância': df['Erro Modelo 1'].var(),
    'Desvio Padrão': df['Erro Modelo 1'].std(),
    'Coeficiente de Variação': (df['Erro Modelo 1'].std() / df['Erro Modelo 1'].mean()) * 100 if df['Erro Modelo 1'].mean() != 0 else float('inf')
}

dispersao_erro_m2 = {
    'Amplitude': df['Erro Modelo 2'].max() - df['Erro Modelo 2'].min(),
    'Variância': df['Erro Modelo 2'].var(),
    'Desvio Padrão': df['Erro Modelo 2'].std(),
    'Coeficiente de Variação': (df['Erro Modelo 2'].std() / df['Erro Modelo 2'].mean()) * 100 if df['Erro Modelo 2'].mean() != 0 else float('inf')
}


metricas_erro = {
    'MAE Modelo 1': df['Erro Absoluto Modelo 1'].mean(),  
    'MAE Modelo 2': df['Erro Absoluto Modelo 2'].mean(),
    'MSE Modelo 1': df['Erro Quadrático Modelo 1'].mean(),  
    'MSE Modelo 2': df['Erro Quadrático Modelo 2'].mean(),
    'RMSE Modelo 1': np.sqrt(df['Erro Quadrático Modelo 1'].mean()),  
    'RMSE Modelo 2': np.sqrt(df['Erro Quadrático Modelo 2'].mean()),
    'MAPE Modelo 1': (df['Erro Absoluto Modelo 1'] / df['Dado Real']).mean() * 100,  
    'MAPE Modelo 2': (df['Erro Absoluto Modelo 2'] / df['Dado Real']).mean() * 100
}


resumo_medidas_posicao = pd.DataFrame({
    'Modelo 1': pd.Series(medidas_erro_m1),
    'Modelo 2': pd.Series(medidas_erro_m2)
})

resumo_medidas_dispersao = pd.DataFrame({
    'Modelo 1': pd.Series(dispersao_erro_m1),
    'Modelo 2': pd.Series(dispersao_erro_m2)
})

resumo_metricas_erro = pd.Series(metricas_erro)


print("Resumo das medidas de posição dos erros:")
print(resumo_medidas_posicao)
print("\nResumo das medidas de dispersão dos erros:")
print(resumo_medidas_dispersao)
print("\nMétricas de erro:")
print(resumo_metricas_erro)


plt.figure(figsize=(10, 6))
plt.hist(df['Erro Modelo 1'], bins=10, alpha=0.5, label='Modelo 1')
plt.hist(df['Erro Modelo 2'], bins=10, alpha=0.5, label='Modelo 2')
plt.title('Distribuição dos Erros')
plt.xlabel('Erro')
plt.ylabel('Frequência')
plt.legend()
plt.grid(True)


plt.figure(figsize=(10, 6))
plt.boxplot([df['Erro Modelo 1'], df['Erro Modelo 2']], labels=['Modelo 1', 'Modelo 2'])
plt.title('Boxplot dos Erros')
plt.ylabel('Erro')
plt.grid(True)


plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(df['Dado Real'], df['Modelo 1'])
plt.plot([min(df['Dado Real']), max(df['Dado Real'])], [min(df['Dado Real']), max(df['Dado Real'])], 'r--')
plt.title('Modelo 1: Valor Real vs. Previsto')
plt.xlabel('Valor Real')
plt.ylabel('Valor Previsto')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(df['Dado Real'], df['Modelo 2'])
plt.plot([min(df['Dado Real']), max(df['Dado Real'])], [min(df['Dado Real']), max(df['Dado Real'])], 'r--')
plt.title('Modelo 2: Valor Real vs. Previsto')
plt.xlabel('Valor Real')
plt.ylabel('Valor Previsto')
plt.grid(True)


print("\nPrimeiros registros com erros calculados:")
print(df[['Dado Real', 'Modelo 1', 'Modelo 2', 'Erro Modelo 1', 'Erro Modelo 2']].head(10))


plt.tight_layout()
plt.show()