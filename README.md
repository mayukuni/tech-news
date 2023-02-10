# Tech News
O projeto que tem como principal objetivo fazer consultas em notícias sobre tecnologia.
As notícias podem ser obtidas através da raspagem do blog da Trybe: https://blog.betrybe.com.

Projeto feito enquanto estudante da Trybe.

### Habilidades trabalhadas:
* Utilizar o terminal interativo do Python
* Aplicar técnicas de raspagem de dados
* Extrair dados de conteúdo HTML
* Armazenar os dados obtidos em um banco de dados

### Os arquivos alterados por mim foram:
* tech_news/analyzer/ratings.py
* tech_news/analyzer/search_engine.py
* tech_news/menu.py
* tech_news/scraper.py

### Para executar o projeto:
* Criar o ambiente virtual: `python3 -m venv .venv`
* Ativar o ambiente virtual: `source .venv/bin/activate`
* Instalar as dependências no ambiente virtual: `python3 -m pip install -r dev-requirements.txt`
* Caso queira desativar o ambiente virtual: `deactivate`
* Para rodar o MongoDB via Docker: `docker-compose up -d mongodb`

### Para executar a função fetch: 
* Dentro do terminal Python, execute a função `python3 -i tech_news/scraper.py`
* Invoque as funções utilizando diferentes parâmetros: `html = fetch("url_da_noticia")` e depois `scrape_news(html)`

