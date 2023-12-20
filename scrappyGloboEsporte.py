import requests
from bs4 import BeautifulSoup
import csv

# URL da página que você deseja fazer o scraping
url = 'https://ge.globo.com/'

# Enviar uma solicitação HTTP para a página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar os elementos HTML que contêm as notícias
    noticias = soup.find_all('a', class_='feed-post-link')

    # Lista para armazenar os dados das notícias
    dados_noticias = []

    # Iterar sobre as notícias e extrair os títulos e links
    for noticia in noticias:
        titulo = noticia.get_text()
        dados_noticias.append([titulo])
        print(titulo)

    # Selecionar apenas os 10 últimos itens da lista
    dados_noticias = dados_noticias[-10:]

    # Salvar os dados em um arquivo CSV com codificação latin1
    with open('ultimas_noticias_esportes.csv', 'w', newline='', encoding='latin1') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        # Escrever o cabeçalho
        writer.writerow(['Título'])
        # Escrever os dados das notícias
        writer.writerows(dados_noticias)

    print('Os 10 últimos dados foram salvos em ultimas_noticias_esportes.csv com codificação latin1.')
else:
    print('Não foi possível acessar a página.')