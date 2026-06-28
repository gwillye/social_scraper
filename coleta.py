import requests
from bs4 import BeautifulSoup
import re

# URL da pesquisa do Google
url = "https://www.google.com/search?q=empresa+exemplo+linkedin"

# Cabeçalho para simular um navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# Enviando a requisição para obter o HTML da página
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Utilizando BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Procurando todas as instâncias de texto
    all_text = soup.get_text(separator=' ')
    
    # Usando regex para capturar o texto até a palavra "seguidores"
    pattern = r"(.*?seguidores)"
    matches = re.findall(pattern, all_text, re.IGNORECASE)
    
    # Imprimindo cada linha que contém até "seguidores"
    for match in matches:
        print(match)
else:
    print("Erro ao acessar a página:", response.status_code)
