from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

books = soup.find_all('li' , class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_ ='price_color').text
    availability = book.find('p', class_ = 'instock availability').text.strip()

    print(f"📚 {title} | 💰 {price} | 📦 {availability}")
    print('=' * 90)
