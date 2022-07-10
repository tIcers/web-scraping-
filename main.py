import bs4
import requests

base_URL = "http://books.toscrape.com/catalogue/page-{}.html"

req = requests.get(base_URL.format(1))
soup = bs4.BeautifulSoup(req.text, 'html.parser')
product = (soup.select(".product_pod"))

title = product[0]
print(title.select("a")[1]['title']) # i can get title now

two_stars_title = []

for n in range(1,51):
    scrape_url = base_URL.format(n)
    req = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(req.text,'html.parser')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_stars_title.append(book_title)

import requests,lxml,bs4

req = requests.get("http://quotes.toscrape.com/page/{}/")
soup = bs4.BeautifulSoup(req.text,'lxml')

for authors in soup.select(".author"):
    print(authors.text)

for quotes in soup.select(".text"):
    print(quotes.text)

# print(soup.select(".tag-item"))
for tags in soup.select(".tag-item"):
    print(tags.text)

base_url = ("http://quotes.toscrape.com/page/{}/")

authors_name = set()
for page in range(1, 10):
    page_url = base_url + str(page)
    req = requests.get(base_url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')

    for authors in soup.select(".author"):
        authors_name.append(authors)