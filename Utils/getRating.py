def numRating(book):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    Rating = rating_map[book.find('p')['class'][1]]
    return Rating