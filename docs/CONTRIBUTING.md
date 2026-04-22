# Contributing

Thank you for your interest in contributing!

---

## Quick Setup & Contribution Flow

Run the following commands:

```bash

git clone <repository-url>
cd <repository-folder>

python -m venv venv # Criando um ambiente virtual

venv\Scripts\activate # Ativando o ambiente

source venv/bin/activate

pip install -r requirements.txt # Instalando as dependências

git checkout -b feature/your-feature-name # Mudando de branch e criando outra

pytest

git add . # Adicionando todos os arquivos

git commit -m "feat: describe your feature" # Enviando a atualização

git push origin feature/your-feature-name # Dando push para o repo remoto/original
