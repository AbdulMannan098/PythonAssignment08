books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Checked Out"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "status": "Available"}
]

users = [
    {"id": 1, "name": "Abid", "borrowed_books": []},
    {"id": 2, "name": "Sajid", "borrowed_books": []}
]

def view_all_books():
    print("\n All Books: ")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Status: {book['status']}")
        
def search_books():
    query=input("Enter title, author, or genre to search: ").lower()
    found_books=[book for book in books if query in book['title'].lower() or query in book['author'].lower() or query in book['genre'].lower() ]
    if found_books:
        print("\n--- Search Results ---")
        for book in found_books:
            print(f"{book['id']}. \"{book['title']}\" by {book['author']} ({book['status']})")
    else:
        print("\nNo matching books found.")

def borrow_books():
    user_id=int(input("Enter User Id:"))
    book_id=int(input("Enter Id of book you want to borrow :"))
    
    user=next((user for user in users if user["id"]==user_id))
    book=next((book for book in books if book["id"]==book_id))
    if user and book:
        if book["status"]=="Available":
            book['status']=="Checked Out"
            user['borrowed_books'].append(book['title'])
            print(f"\nYou have borrowed \"{book['title']}\".")
        else:
            print(f"\nSorry, the book \"{book['title']}\" is currently checked out.")
    else:
        print("\nInvalid User ID or Book ID.")
def return_books():
    user_id=int(input("Enter User Id:"))
    book_id=int(input("Enter Id of book you want to return :"))

    user=next((user for user in users if user["id"]==user_id))
    book=next((book for book in books if book["id"]==book_id))
    if user and book:
        if book["status"]=="Checked Out":
            book['status']=="Available"
            user['borrowed_books'].remove(book['title'])
            print(f"\nYou have returned \"{book['title']}\".")
        else:
             print("\nInvalid return request.")
def view_all_users():
    print("\n All Users:")
    for user in users:
        borrowed_books = ', '.join(user["borrowed_books"]) if user["borrowed_books"] else "None"
        print(f"User ID: {user['id']}, Name: {user['name']}, Borrowed Books: {borrowed_books}")
def view_available_books():
    print("\n Available Books:")
    availableBooks=[book for book in books if book['status']=="Available"]
    if availableBooks:
        for avb in availableBooks:
            print(f"Book ID: {avb['id']}, Title: {avb['title']}, Author: {avb['author']}")
        else:
            print("No books available.")
def view_checked_out_books():
    print("\n Checked Out Books:")
    checkedOutBooks=[book for book in books if book['status']=="Checked Out"]
    if checkedOutBooks:
        for chb in checkedOutBooks:
            print(f"Book ID: {chb['id']}, Title: {chb['title']}, Author: {chb['author']}")
        else:
            print("No books checked out.")
        
def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("----------------------------------------")
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. View available books")
        print("7. View checked-out books")
        print("8. Exit")
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            view_all_books()
        elif choice==2:
            search_books()
        elif choice==3:
            borrow_books()
        elif choice==4:
            return_books()
        elif choice==5:
            view_all_users()
        elif choice==6:
            view_available_books()
        elif choice==7:
            view_checked_out_books()
        elif choice==8:
            print("Thank you for using the Community Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()