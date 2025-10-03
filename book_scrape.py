from bs4 import BeautifulSoup
import requests
import lxml

base_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/'
page_num = 1

while True:
    
    url = f'{base_url}page-{page_num}.html' #to add the page number to the url 
    response = requests.get(url) # return status code either 200 or 404

    if response.status_code == 404:
        break

    soup = BeautifulSoup(response.text, 'lxml')
    books = soup.find_all('li' , class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
    
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_ ='price_color').text
        availability = book.find('p', class_ = 'instock availability').text.strip()
    
        print(f"📚 {title} | 💰 {price} | 📦 {availability}")
        print('=' * 90)
        
    page_num += 1
