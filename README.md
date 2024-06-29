# ConsultasV

## Visão Geral
ConsultasV é uma aplicação web desenvolvida para facilitar o agendamento de consultas veterinárias. A aplicação permite que os usuários agendem, visualizem e cancelem consultas com facilidade.

## Funcionalidades
- Agendamento de Consultas
- Visualização de Consultas
- Cancelamento de Consultas
- Autenticação de Usuário

## Tecnologias Utilizadas
- Python
- Django
- HTML
- CSS
- JavaScript

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/RodrigoMaciel00/ConsultasV.git
    ```
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Execute as migrações:
    ```bash
    python manage.py migrate
    ```
5. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

## Uso
- Acesse `http://127.0.0.1:8000` no navegador.
- Crie uma conta ou faça login.
- Agende uma nova consulta, visualize ou cancele consultas existentes.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests. Para contribuições maiores, por favor abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

