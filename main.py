import bs4
import requests

page_num = 12
base_URL = "http://books.toscrape.com/catalogue/page-{}.html"
res = requests.get(base_URL.format(1))

print(base_URL)