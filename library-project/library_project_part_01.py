# 1.create the library class.
class Library:
    book_list = []
    @classmethod
    def entry_book(self, book):
        self.book = book
        self.book_list.append(self.book)
    def veiw_book(self):
        for book in self.book_list:
            print(book)


# 2.create the Book class.
class Book:
    def __init__(self, book_id, title, author, availability) -> None:
        self.__book_id = book_id # 9.private attribute
        self._title = title  # 9.protected attribute
        self._author = author  # 9.protected attribute
        self.__availability = availability # 9.private attribute


# 4. Implement borrow_book() method
    @classmethod
    def borrow_book(self,book_id):
        book = next((book for book in Library.book_list if book.__book_id == book_id and book.__availability == True),None)
        if(book):
            print(f'your are successful to borrow this book\n')
            book.__availability = False
        else:
            print(f'this book is not available\n') # 8. Error handling for invalid bookID.


# 5. Implement return_book() method
    @classmethod
    def return_book(self,book_id):
        book = next((book for book in Library.book_list if book.__book_id == book_id and book.__availability == False),None)
        if(book):
            print(f'your are successful to return this book\n')
            book.__availability = True
        else:
            print(f'this book is not returnable\n')  # 8. Error handling for invalid bookId.


# 6. Implement view_book_info() method
    @classmethod
    def view_book_info(self):
        for book in Library.book_list:
            print (f'ID: {book.__book_id}, Tile: {book._title}, Author: {book._author}, Availability: {book.__availability}')
            print()


# 3. Initialize the books in manually.
book1 = Book(101,'Artificial Intelligence','E.Ritch',True)
book2 = Book(102,'Web Programming','Larry ullman',True)
book3 = Book(103,'Database System','korth',True)
book4 = Book(104,'Computer Architecture','P.Hayes',True)
book5 = Book(105,'Robotics Engineering','Peter Norvig',True)
book6 = Book(106,'Network pProgramming','Deitel',True)
book7 = Book(107,'Cryptography System','William',True)
book8 = Book(108,'Computer Security','Stallings',True)
Library.entry_book(book1)
Library.entry_book(book2)
Library.entry_book(book3)
Library.entry_book(book4)
Library.entry_book(book5)
Library.entry_book(book6)
Library.entry_book(book7)
Library.entry_book(book8)

print('Welcome our Library')
print('1. View All Books')
print('2. Borrow Book')
print('3. Return Book')
print('4. Exit')

# 7. Menu System
while True:
    option = int(input('Enter your option 1 to 4:'))
    if option == 1:
        Book.view_book_info()
    elif option == 2:
        book_id = int(input('Enter your book id:'))
        Book.borrow_book(book_id)
    elif option == 3:
        book_id = int(input('Enter your book id:'))
        Book.return_book(book_id)
    else:
        print('Thanks for visiting our Library')
        break
