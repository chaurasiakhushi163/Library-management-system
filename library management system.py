library=["python", "dbms","maths","operating system","english"]
def add_books():
    book=input("Enter book name:")
    library.append(book)
    print("book added sucessfully!")
def view_books():
    if len(library)==0:
        print("books are not available \nlibrary is empty ")
    else:
        print("total books:",len(library))
        print("\nbooks are availble")
        for books in library:
            print(books)
def search_books():
    book=input("Enter your book name to search:")
    if book in library:
        print("book is available")

    else:
        print("book is not available")
def delete_books():
    book =input("enter the book name u want to delete")
    if book in library:
        library.remove(book)
        print("book deleted successfully!")
    else:
        print("book not found")
while True:
    print("Library management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books")
    print("4. Delete Books")
    print("5. Exit")

    choice=input("enter your choice:")
    if choice=="1":
        add_books()
    elif choice=="2":
        view_books()
    elif choice=="3":
        search_books()
    elif choice=="4":
        delete_books()
    elif choice=="5":
        print("thank you!")
        break
    else:
        print("invalid  choice")
        


    


    
    
            
