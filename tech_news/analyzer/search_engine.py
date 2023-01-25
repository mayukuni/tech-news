from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = []
    search = {"title": {"$regex": title, "$options": "i"}}
    results = search_news(search)
    for result in results:
        news.append((result["title"], result["url"]))
    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
