from bs4 import *
from requests import *
import csv

file = open('output/com_book.csv', 'w')
writer = csv.writer(file,delimiter=";")
data = ['Name', 'URL', 'Author', 'Price', 'Number of Ratings', 'Average Rating']
writer.writerow(data)

URLS = []
URLS.append('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/')
URLS.append('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_2/142-3163014-5727941?_encoding=UTF8&pg=2')
URLS.append('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_3?_encoding=UTF8&pg=3')
URLS.append('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_4?_encoding=UTF8&pg=4')
URLS.append('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_5?_encoding=UTF8&pg=5')

for URL in URLS:
    url = get(URL)
    soup = BeautifulSoup(url.text, 'html.parser')
    books = soup.find_all('div', class_='zg_itemWrapper')
    for book in books:
        name = book.find('div', class_="p13n-sc-truncate p13n-sc-line-clamp-1")
        url = book.find('a', class_='a-link-normal')
        star = book.find('span', class_='a-icon-alt')
        price = book.find('span', class_='a-size-base a-color-price')
        ratings = book.find('a', class_='a-size-small a-link-normal')
        author = book.find('a', class_='a-size-small a-link-child')
        try:
            name_book = name.text
        except:
            name_book = 'Not available'
        try:
            url_book = 'https://www.amazon.com'+url['href']
        except:
            url_book = 'Not available'
        try:
            author_book = author.text
        except:
            author_book = 'Not available'
        try:
            price_book = price.text
        except:
            price_book = 'Not available'
        try:
            rating_book = ratings.text
        except:
            rating_book = 'Not available'
        try:
            stars_book = star.text
            if stars_book == 'Prime':
                stars_book = 'Not available'
        except:
            stars_book = 'Not available'
        data = [name_book, url_book, author_book, price_book, rating_book, stars_book]
        writer.writerow(data)
