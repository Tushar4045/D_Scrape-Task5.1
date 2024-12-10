import re
def extractPrice(book):
    Price = book.find('p', attrs={'class': 'price_color'}).text
    floatPrice = re.sub(r'[^\d.]', '',Price)  # Consistent use of 'Price'

    return float(floatPrice)