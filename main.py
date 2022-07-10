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
