from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import time

# Configuração de opções para rodar o Chrome de modo furtivo
def init_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Caminho para o ChromeDriver
service = Service('/caminho/para/seu/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL da pesquisa no Google
url = "https://www.google.com/search?q=empresa+exemplo+linkedin"
driver.get(url)

# Tempo de espera para o carregamento da página
time.sleep(2)  # Ajuste conforme necessário

# Captura do texto da página
page_text = driver.find_element(By.TAG_NAME, "body").text

# Usando regex para encontrar todo o texto até "seguidores"
pattern = r"(.*?seguidores)"
matches = re.findall(pattern, page_text, re.IGNORECASE)

# Imprimindo o resultado até a palavra "seguidores"
for match in matches:
    print(match)

# Fechando o navegador
driver.quit()
