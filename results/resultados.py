import pandas as pd

dados_completos = [
    # 100 Imagens
    ["Sequencial", 1, 100, 91.64, 86.99, 85.97, 80.14, 87.83, 86.52],
    ["Threading", 2, 100, 98.87, 88.07, 67.91, 71.08, 85.81, 82.35],
    ["Threading", 4, 100, 65.80, 65.86, 59.25, 41.96, 41.97, 54.97],
    ["Threading", 8, 100, 33.77, 42.30, 37.79, 31.94, 32.99, 35.76],
    ["Multiprocessing", 2, 100, 73.49, 80.71, 62.16, 82.53, 72.90, 74.36],
    ["Multiprocessing", 4, 100, 47.13, 49.27, 59.96, 48.60, 47.64, 50.52],
    ["Multiprocessing", 8, 100, 41.83, 40.50, 35.35, 31.84, 37.34, 37.37],
    ["Futures", 2, 100, 65.91, 62.18, 58.46, 59.98, 55.83, 60.47],
    ["Futures", 4, 100, 40.35, 36.08, 35.32, 36.35, 39.53, 37.53],
    ["Futures", 8, 100, 30.23, 28.61, 28.51, 29.04, 29.19, 29.12],

    # 500 Imagens
    ["Sequencial", 1, 500, 422.90, 422.16, 411.18, 444.49, 506.56, 441.46],
    ["Threading", 2, 500, 410.21, 403.22, 360.05, 328.44, 322.26, 364.84],
    ["Threading", 4, 500, 189.55, 192.60, 189.58, 189.25, 235.66, 199.33],
    ["Threading", 8, 500, 162.86, 149.62, 150.12, 144.28, 136.67, 148.71],
    ["Multiprocessing", 2, 500, 430.43, 359.03, 438.76, 336.11, 406.90, 394.25],
    ["Multiprocessing", 4, 500, 201.76, 306.36, 264.05, 243.68, 263.37, 255.84],
    ["Multiprocessing", 8, 500, 141.59, 143.10, 206.07, 201.12, 145.53, 167.48],
    ["Futures", 2, 500, 288.49, 538.67, 299.20, 307.28, 298.42, 346.41],
    ["Futures", 4, 500, 176.05, 177.23, 202.12, 188.28, 193.27, 187.39],
    ["Futures", 8, 500, 143.46, 145.18, 145.09, 145.46, 143.64, 144.56],

    # 1000 Imagens
    ["Sequencial", 1, 1000, 1047.46, 1014.78, 1194.66, 1646.75, 1367.34, 1254.20],
    ["Threading", 2, 1000, 627.50, 791.97, 689.92, 632.84, 748.90, 698.23],
    ["Threading", 4, 1000, 513.58, 734.12, 750.67, 737.93, 562.82, 659.82],
    ["Threading", 8, 1000, 463.91, 428.60, 408.04, 576.38, 519.86, 479.36],
    ["Multiprocessing", 2, 1000, 906.24, 823.16, 881.46, 867.04, 774.89, 850.56],
    ["Multiprocessing", 4, 1000, 624.53, 481.87, 440.91, 537.43, 432.36, 503.42],
    ["Multiprocessing", 8, 1000, 368.01, 358.88, 393.70, 425.77, 402.65, 389.80],
    ["Futures", 2, 1000, 546.20, 547.40, 554.14, 543.73, 565.85, 551.46],
    ["Futures", 4, 1000, 385.93, 380.78, 381.42, 384.42, 385.24, 383.56],
    ["Futures", 8, 1000, 294.14, 292.20, 292.46, 290.58, 296.29, 293.13]
]

colunas = [
    "Abordagem", "Workers", "Qtd_Imagens", 
    "Rodada_1", "Rodada_2", "Rodada_3", "Rodada_4", "Rodada_5", "Media_s"
]

df_resultados = pd.DataFrame(dados_completos, columns=colunas)

print("Amostra dos Dados:")
print(df_resultados.head())

# Exportando para CSV
df_resultados.to_csv("resultados_completos_pokeapi.csv", index=False)
print("\nArquivo 'resultados_completos_pokeapi.csv' gerado com sucesso!")

# para exportar para Excel (opcional): necessário: "pip install openpyxl"
#df_resultados.to_excel("resultados_completos_pokeapi.xlsx", index=False)