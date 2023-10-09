#import necessary modules 
from libsysfunctions import indexNumber, menu, Student, Library
from os import system
import pickle

libraryData={'The Adventures of Huckleberry Finn':'Mark Twain',
            'The Great Gatsby':'F. Scott Fitzgerald',
            'Anna Karenina':'Leo Tolstoy',
            'Madame Bovary':'Gustave Flaubert',
            'Moby Dick':'Herman Melville',
            'One Hundred Years of Solitude':'Gabriel Garcia Marquez',
            '1984':'George Orwell',
            'Brave New World':'Aldous Huxley',
            'The Feast of the Goat':'Mario Vargas Llosa',
            'In Search of Lost Time':'Marcel Proust'}

borrowed = dict()

index_Number = indexNumber()

proceed = "yes"
while proceed =="yes":
    try:
        # Try loading the books 
        with open("library.pkl", "rb") as file:
            loaded_table = pickle.load(file)
    except (FileNotFoundError, pickle.PickleError, Exception):
        # Handle the exception (file not found or pickle error)
        loaded_table = libraryData    
   
    try:
        # Try loading the borrowed data
        with open("borrowed.pkl", "rb") as file:
            borrowed_table = pickle.load(file)
    except (FileNotFoundError, pickle.PickleError,Exception):
        # Handle the exception (file not found or pickle error)
        borrowed_table = borrowed
    
    student = Student(index_Number, borrowed_table)
    library = Library(loaded_table)
    
    # Display menu   
    choice = menu()
    #take actions based on user choice
    if choice == 1:
        allBooks = library.showAvailableBooks()
        
    elif choice == 2:
        allBooks = library.showAvailableBooks()
        borrow = student.requestBook()
        lend = library.lendBook(student, borrow)
        
    elif choice == 3:
        bringBookBack = student.returnBook()
        takeBookBack = library.returnBook(student,bringBookBack)
        
            
    elif choice == 4:
        viewBorrowed = student.viewBorrowedBook()
    
    elif choice == 5:
        # Save the updated table to the pickled document
        exit(system("cls"))

    with open("library.pkl", "wb") as file:
            pickle.dump(library.available_books, file)
    with open("borrowed.pkl", "wb") as file:
            pickle.dump(student.borrowed_books, file)
            
    proceed = input("Do you want to return to the main menu?(yes/no)").lower()
    if proceed!="yes":
        exit("Terminating Program")
        
    
    system("cls")