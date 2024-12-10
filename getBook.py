from Utils.getPrice import extractPrice
from Utils.getRating import numRating

def extractBook(book):
    img = book.find('div', attrs = {'class': 'image_container'}).a.img
    imgData = {
        'src': img.attrs['src'],
        'alt': img.attrs['alt']
    }
    price = extractPrice(book)
    rating = numRating(book)
    title = book.find('h3').a['title']
    bookData = {
        'imgData':imgData,
        'Price':price,
        'Rating':rating,
        'Title':title
    }
    return bookData