# Projeto-de-Software-Grupo-5 (AllEvent)

Repositório destinado à criação do Website relacionado ao curso ENG4O21 PROJETO INTEGRADO - SOFTWARE, Turma A, Time 5.

**Integrantes:**
- CAROLINA DE ALMEIDA M CHAVES
- RAFAELA ARAUJO DE SOUSA
- BRENNO TAVORA BARBOSA
- DANIEL DOS SANTOS FERREIRA
- VINICIUS R M C DA SILVA

## Descrição do Projeto

O **AllEvent** é um portal web de entretenimento focado na descoberta, avaliação e gerenciamento de eventos. O sistema permite que usuários se cadastrem, façam login, personalizem seus perfis, favoritem eventos e naveguem por um catálogo completo.

Este projeto foi desenvolvido utilizando uma arquitetura web moderna, com o back-end em Django e o front-end em HTML/CSS.

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python
* **Framework:** Django
* **Front-end:** HTML5, CSS3
* **Banco de Dados:** SQLite3 (padrão do Django)

## 🚀 Como Rodar o Projeto Localmente

Para executar este projeto no seu computador, siga os passos abaixo:

1.  **Clone o Repositório**
    ```bash
    git clone [https://github.com/SEU-USUARIO/Projeto-de-Softwre-Grupo-5.git](https://github.com/SEU-USUARIO/Projeto-de-Softwre-Grupo-5.git)
    cd Projeto-de-Softwre-Grupo-5
    ```

2.  **Navegue até a Pasta do Projeto Django**
    O projeto principal está dentro da pasta `Projeto`:
    ```bash
    cd Projeto
    ```

3.  **Crie e Ative o Ambiente Virtual (`venv`)**
    *Se a pasta `venv` já existir, delete-a primeiro.*
    ```bash
    # Criar o venv
    python -m venv venv

    # Ativar no Windows (CMD/PowerShell)
    venv\Scripts\activate
    
    # Ativar no Mac/Linux (ou Git Bash)
    source venv/bin/activate
    ```

4.  **Instale as Dependências**
    Todas as bibliotecas necessárias (incluindo o Django) estão no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure o Banco de Dados**
    Este comando cria o arquivo `db.sqlite3` e as tabelas necessárias:
    ```bash
    python manage.py migrate
    ```

6.  **Crie um Superusuário (Opcional, mas recomendado)**
    Isso permite que você acesse o painel `/admin`:
    ```bash
    python manage.py createsuperuser
    ```
    (Siga as instruções para criar seu usuário admin)

7.  **Rode o Servidor!**
    ```bash
    python manage.py runserver
    ```

8.  Acesse o site no seu navegador em: **`http://127.0.0.1:8000/`**