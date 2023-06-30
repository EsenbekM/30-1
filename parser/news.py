import datetime

import requests
from bs4 import BeautifulSoup


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
              "avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def get_url(year, month, day, ordering):
    url = f"https://kaktus.media/?lable=8&date=" \
          f"{year}-{month}-{day}" \
          f"&order={ordering}"
    return url


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all(
        "div",
        class_="Tag--article",
        # class_=lambda value: value and value.startswith("Tag--article"),
        limit=5
    )
    parserd_data = [
        {
            "title": item.find("a", class_="ArticleItem--name").string.replace("\n", ""),
            "url": item.find("a", class_="ArticleItem--name").get("href"),
            "time": item.find("div", class_="ArticleItem--time").getText().strip(),
            "image": item.find("img").get("src").replace("small", "big")
        } for item in items
    ]

    return parserd_data


def parser():
    current_date = datetime.datetime.now()
    url = get_url(current_date.year, current_date.month, current_date.day, "time")
    html = get_html(url)
    parsed_data = get_data(html.text)
    return parsed_data
