#é um serviço que pode usar  para acessar dados ou funcionalidades externas ja codadas
#apli de (clima, libras,IA)
#
#define o endereço da api com nome 'lucas'


# Importa a biblioteca para conectar com a internet
import requests

# Pede ao usuário para digitar um nome
nome = input("Digite um nome: ")

# Usa o nome digitado na URL da API
url = f"https://api.agify.io?name={nome}"

# Faz a requisição e guarda a resposta
resposta = requests.get(url)

# Converte a resposta para um dicionário
dados = resposta.json()

# Verifica se a resposta contém os dados esperados
if 'name' in dados and 'age' in dados:
    print(f"Nome: {dados['name']}")
    print(f"Idade estimada: {dados['age']}")
else:
    print("Não foi possível estimar a idade para esse nome.")
