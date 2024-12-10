import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
from getBook import extractBook

bookUrl = 'https://books.toscrape.com/'
bookHeader = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
bookResp = rq.get(url=bookUrl,headers=bookHeader)
bookSoup = BeautifulSoup(bookResp.content,'html.parser')
books = [extractBook(book) for book in  bookSoup.find_all('article',attrs={'class':'product_pod'})]
booksDf = pd.DataFrame(books)
booksDf.to_csv('books.csv')


    