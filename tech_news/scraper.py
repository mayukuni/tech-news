import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str):
    time.sleep(1)
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"User-Agent": "Fake user-agent"}
        )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content: str):
    selector = Selector(text=html_content)
    links = selector.css(".entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content: str):
    selector = Selector(text=html_content)
    next_page = selector.css(".next.page-numbers::attr(href)").get()
    if next_page:
        return next_page
    else:
        return None


# Requisito 4
def scrape_news(html_content: str):
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = selector.css(
        ".post-comments .title-block::text"
    ).get()
    summary = "".join(selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()).strip()
    tags = selector.css(".post-tags ul li a::text").getall()
    category = selector.css(".meta-category a .label::text").get()

    data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": (
            int(comments_count.split()[0])
            if comments_count else 0
        ),
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
