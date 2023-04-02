
#booklover_test.py

import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        BookLover1 = BookLover("Nick", "nph4zk@virginia.edu", "nonfiction")
        Book = "Moneyball"
        Rating = 5
        BookLover1.add_book(Book, Rating)
        
        self.assertTrue(Book in list(BookLover1.book_list['book_name']))
        # add a book and test if it is in `book_list`.
        
    def test_2_add_book(self):
        BookLover1 = BookLover("Nick", "nph4zk@virginia.edu", "nonfiction")
        Book1 = "Moneyball"
        Rating1 = 5
        BookLover1.add_book(Book1, Rating1)
        Book2 = "Moneyball"
        Rating2 = 5
        BookLover1.add_book(Book2, Rating2)

        self.assertTrue(BookLover1.book_list[BookLover1.book_list['book_name'] == Book2].shape[0] == 1)
        # add the same book twice. Test if it's in `book_list` only once.

    def test_3_has_read(self):
        BookLover1 = BookLover("Nick", "nph4zk@virginia.edu", "nonfiction")
        Book = "Moneyball"
        Rating = 5
        BookLover1.add_book(Book, Rating)
        BookLover1.has_read(Book)
        
        self.assertTrue(BookLover1.has_read(Book) is True)
        # pass a book in the list and test if the answer is `True`.
        
    def test_4_has_read(self):
        BookLover1 = BookLover("Nick", "nph4zk@virginia.edu", "nonfiction")
        BookLover1.has_read("Harry Potter")
        
        self.assertFalse(BookLover1.has_read("Harry Potter") is True)
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
    def test_5_num_books_read(self):
        BookLover1 = BookLover("Nick", "nph4zk@virginia.edu", "nonfiction")
        Book1 = "Frankenstein"
        Rating1 = 3
        BookLover1.add_book(Book1, Rating1)
        Book2 = "Don Quixote"
        Rating2 = 4
        BookLover1.add_book(Book2, Rating2)
        Book3 = "Cat's Cradle"
        Rating3 = 5
        BookLover1.add_book(Book3, Rating3)
        BookLover1.num_books_read()
        
        expected = 3
        self.assertEqual(BookLover1.num_books_read, expected)
        # add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self):
        BookLover1 = BookLover("Nick", "nph4zk@virginia.edu", "nonfiction")
        Book1 = "Great Expectations"
        Rating1 = 2
        BookLover1.add_book(Book1, Rating1)
        Book2 = "AQOTWF"
        Rating2 = 5
        BookLover1.add_book(Book2, Rating2)
        Book3 = "Animal Farm"
        Rating3 = 4
        BookLover1.add_book(Book3, Rating3)
        BookLover1.fav_books()
         
        self.assertTrue(all(BookLover1.fav_books[BookLover1.fav_books['book_rating'] > 3.0]))
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3

if __name__ == '__main__':
    unittest.main(verbosity = 3)
    
    
    