#booklover.py

import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = str(name)
        self.email = str(email)
        self.fav_genre = str(fav_genre)
        self.num_books = int(num_books)
        self.book_list = pd.DataFrame(book_list)
    
    def add_book(self, book_name, book_rating):
        self.book_name = str(book_name)
        self.book_rating = int(book_rating)
        self.new_book = pd.DataFrame({'book_name': [self.book_name], 'book_rating': [self.book_rating]})
        if (book_name in list(self.book_list['book_name']) or book_rating < 0 | book_rating >5):
            print("Book already exists in list") 
        else:
            self.book_list = pd.concat([self.book_list, self.new_book], ignore_index = True)
       
    def has_read(self, book_name):
        self.book_name = book_name
        if (book_name in list(self.book_list['book_name'])):
            return True
        else:
            return False
            
    def num_books_read(self):
        self.num_books_read = len(self.book_list)
        print(self.num_books_read)
        
    def fav_books(self):
        self.fav_books = pd.DataFrame(self.book_list[(self.book_list['book_rating'] > 3)])
        print(self.fav_books)
        
if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.has_read("War of the Worlds")
    test_object.num_books_read()
    test_object.fav_books()
    
    
    