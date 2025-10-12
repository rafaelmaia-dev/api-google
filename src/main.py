import requests
import os 

url = "https://www.google.com.br" # Adicionando um link do Google a uma variável 

try:
    response = requests.get(url) # Aqui a variável 'response' recebe uma requição com o método 'get' do HTTP para buscar dados da URL

    if response.status_code == 200: # Aqui é uma condição verificando se a resposta da requição pode alcançar o resultado de sucesso
        print('Sucesso! Status:', response.status_code)
        print('Conteúdo (primeiros 100 chars):', response.text[:100])

        os.makedirs('files', exist_ok = True) # Criando o diretório sem erro se já existir

        with open("files/page.html", "w", encoding = "UTF-8") as page:
                page.write(response.text)

        print("Página salva em files/page.html")
    else:
        print(f'Status Inválido: {response.status_code}')

except (requests.exceptions.RequestException, IOError, Exception) as e: # Aqui como o except válida uma condição como booleana, usei as 'tuplas' para adicionar os possíveis erros 
    print(f'Erro no request: {e}.')




