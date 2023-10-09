from tabulate import tabulate

# define student class
class Student:
    #inititalize student class
    def __init__(self, index, borrowed_table):
        # Assign student's index number to private variable id
        self.id= index  
        self.borrowed_books = borrowed_table
    
    #method to view a student's borrowed books  
    def viewBorrowedBook(self):
        print("Borrowed Books")
        print("---------------")
        
        head = ["Books", "Authors"]
           
        print(tabulate(self.borrowed_books.items(), headers=head, tablefmt="grid"))
            
    #to request a book or more
    def requestBook(self): 
        bookRequest = input("Enter the name of the book you want to borrow: ") 
        return bookRequest
                
    #return a book
    def returnBook(self):
        returnBook = input("Enter the name of the book you want to return: ")
        return returnBook

#define library class
class Library:
    def __init__(self, loaded_table):
        self.available_books = loaded_table
            
    #display books in the library
    def showAvailableBooks(self):
        print("Books Available")
        print("---------------")
        head = ["Books", "Authors"]
        print(tabulate(self.available_books.items(), headers=head, tablefmt="grid"))
        
    #lend a book to a student
    def lendBook(self, student, book_name):
        if book_name in self.available_books :
            student.borrowed_books[book_name] = self.available_books[book_name]
            del self.available_books[book_name]    
            print("You have successfully borrowed a book!")
            return True
        else:
            print("Book not found in the library.")
            return False
        
    #return a book the user is returning to the library
    def returnBook(self, student, bookName):
        if bookName in student.borrowed_books:
            self.available_books[bookName] = student.borrowed_books[bookName]
            del student.borrowed_books[bookName]
            print(f"You have successfully returned {bookName}!")
            return True
        else:
            print("Invalid book title.")
            return False
     
# function to display menu and accept choice    
def menu():
    print("\n\t \t Library Management System")
    print("\t \t -------------------------")
    print("1. Display books \n2. Borrow book \n3. Return book \
    \n4. View borrowed books \n5. Quit")

    while True: 
        try: 
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid input. Choice should be from 1-5")
        except ValueError:
            print("Invalid input. Choice should be from 1-5")

#function to accept index number from user
def indexNumber():
    indexNumber=0
    while indexNumber<=0 or ValueError:
        try:
            indexNumber = int(input("What is your index number?"))
        except ValueError:
            print("Index number can only contain digits")
        else:
            if indexNumber<=0:
                print("Invalid index number")
            else:
                break
    return indexNumber



