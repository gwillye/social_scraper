import requests
import re
import gspread
from google.oauth2.service_account import Credentials
from bs4 import BeautifulSoup
import traceback

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        return content
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None

def search_in_content(content, keyword):
    try:
        # Analisando o conteúdo HTML com BeautifulSoup
        soup = BeautifulSoup(content, 'lxml')
        
        # Encontrando todos os spans que contêm a palavra-chave
        spans = soup.find_all('span')
        
        for span in spans:
            span_text = span.get_text()
            if keyword in span_text.lower():
                # Pegando os 15 caracteres anteriores ao 'seguidores'
                start_index = span_text.lower().find(keyword.lower())
                snippet = span_text[max(0, start_index - 15):start_index]
                
                # Removendo tudo que não é número
                numbers = re.findall(r'\d+', snippet)
                
                if numbers:
                    return ''.join(numbers)
        
        return "Palavra não encontrada no conteúdo."
    except Exception as e:
        print(f"Ocorreu um erro ao processar o conteúdo: {e}")
        return None

def get_next_available_cell(worksheet):
    try:
        column_values = worksheet.col_values(10)  # Coluna "J" é a 10ª coluna
        next_row = len(column_values) + 1
        return f'J{next_row}'
    except Exception as e:
        print("Erro ao obter a próxima célula disponível:")
        traceback.print_exc()
        return 'J2'  # Fallback para 'J2' em caso de erro

def save_to_google_sheet(value, spreadsheet_url):
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file('key.json', scopes=scopes)
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_url(spreadsheet_url)
        
        worksheet = spreadsheet.get_worksheet(0)  # Seleciona a primeira aba
        next_cell = get_next_available_cell(worksheet)
        
        worksheet.update_acell(next_cell, value)
        print(f"Valor '{value}' salvo com sucesso na célula {next_cell}!")
    except Exception as e:
        print("Erro ao salvar na planilha:")
        traceback.print_exc()  # Isso exibirá a stack trace completa

if __name__ == "__main__":
    url = 'https://www.google.com/search?q=empresa+exemplo+linkedin'
    
    content = fetch_page_content(url)
    
    if content:
        keyword = 'seguidores'
        number_extracted = search_in_content(content, keyword)
        
        if number_extracted and number_extracted.isdigit():
            print(f"Número encontrado: {number_extracted}")

            # URL da planilha Google Sheets
            spreadsheet_url = 'https://docs.google.com/spreadsheets/d/SEU_SHEET_ID_AQUI/edit?usp=sharing'
            
            # Salva o valor na próxima célula disponível na coluna J
            save_to_google_sheet(number_extracted, spreadsheet_url)
        else:
            print("Nenhum número válido encontrado.")
