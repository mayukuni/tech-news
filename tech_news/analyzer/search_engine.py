from tech_news.database import search_news
from datetime import datetime


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
    try:
        date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        time = {"timestamp": {"$eq": date}}
        results = search_news(time)

        return [(news["title"], news["url"]) for news in results]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = []
    search = {"tags": {"$regex": tag, "$options": "i"}}
    results = search_news(search)
    for result in results:
        news.append((result["title"], result["url"]))
    return news


# Requisito 9
def search_by_category(category):
    news = []
    search = {"category": {"$regex": category, "$options": "i"}}
    results = search_news(search)
    for result in results:
        news.append((result["title"], result["url"]))
    return news
