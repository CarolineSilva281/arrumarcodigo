# Importa a biblioteca de gráficos
import matplotlib.pyplot as plt
 
# Dados para o gráfico
categorias = ['Huawei', 'Iphone', 'Samsung','Motorola']
quantidade = [40, 85, 90,60]
 
# Cria o gráfico de barras
plt.bar(categorias, quantidade)
# Adiciona título e rótulos
plt.title("Marcas de celulares famosas de 2025")
plt.xlabel("")
plt.ylabel("Quantidade")
 
# Mostra o gráfico na tela
plt.show()