## 🌐 Requisição via API usando o método GET do protocolo HTTP

## API Google

<!-- Badges -->
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/github/license/rafaelmaia-dev/api-google)
[![Python CI](https://github.com/rafaelmaia-dev/api-google/actions/workflows/python.yml/badge.svg)](https://github.com/rafaelmaia-dev/api-google/actions/workflows/python.yml)

 **Este mini projeto consulta o Google usando o método GET do protocolo HTTP para acessar o status code da URL, com TRY e EXCEPT para tratamento de exceções. Utiliza a biblioteca `requests` para comunicação HTTPS e o módulo `os` (built-in) para interação com o sistema operacional.**

---

## 📂 Foco da API

- Trabalhar com APIs reais (Google)
- Praticar Python com bibliotecas como Requests
- Implementar tratamento de erros e boas práticas
- Organizar um projeto com estrutura limpa e documentação clara

---

## 📁 Estrutura do projeto

```
api-google/
├── src/
│   ├── __init__.py
│   └── main.py              # Script principal
├── tests/
│   └── test_main.py         # Testes automatizados
├── .github/workflows/       # CI com GitHub Actions
├── requirements.txt
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python 3.11 ou superior

---

## 💻 Como usar

**1. Clone o repositório:**

```bash
git clone https://github.com/rafaelmaia-dev/api-google
cd api-google
```

**2. Crie e ative o ambiente virtual (recomendado):**

```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # Linux/Mac
```

**3. Instale as dependências e execute:**

```bash
pip install -r requirements.txt
python src/main.py
```

**Saída esperada:**

```
Sucesso! Status: 200
Conteúdo (primeiros 100 chars): <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="pt-BR"><head><meta cont
Página salva em files/page.html
```

---

## 🛠️ Teste automatizado

**Rodar todos os testes:**

```bash
pytest
```

**Ou apenas o teste principal:**

```bash
pytest tests/test_main.py
```

**Saída esperada:**

```
================= test session starts =================
collected 1 item

tests/test_main.py .                                [100%]

================= 1 passed in 0.10s =================
```

---

## 🛠 Tecnologias

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="45" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="45" />
</p>

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
