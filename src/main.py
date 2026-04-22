import requests
import os

url = "https://www.google.com.br"  # Adicionando um link do Google a uma variável

try:
    response = requests.get(
        url
    )  

    if (
        response.status_code == 200
    ):  
        print("Sucesso! Status:", response.status_code)
        print("Conteúdo (primeiros 100 chars):", response.text[:100])

        os.makedirs(
            "files", exist_ok=True
        )  

        with open("files/page.html", "w", encoding="UTF-8") as page:
            page.write(response.text)

        print("Página salva em files/page.html")
    else:
        print(f"Status Inválido: {response.status_code}")

except (
    requests.exceptions.RequestException,
    IOError,
    Exception,
) as e:  
    print(f"Erro no request: {e}.")
