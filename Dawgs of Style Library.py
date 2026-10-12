
import os
import turtle
from datetime import datetime

# Set the Command Prompt window title
os.system("title Sorting System")

# Store the library books and their information
books = {
    101: {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "category": "Fantasy",
        "available": True
    },
    102: {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "category": "Fantasy",
        "available": True
    },
    103: {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "category": "Fiction",
        "available": True
    },
    104: {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "Classic Literature",
        "available": True
    },
    105: {
        "title": "A Brief History of Time",
        "author": "Stephen Hawking",
        "category": "Science",
        "available": True
    },
    106: {
        "title": "The Art of War",
        "author": "Sun Tzu",
        "category": "Philosophy",
        "available": True
    },
    107: {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "category": "Programming",
        "available": True
    },
    108: {
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupery",
        "category": "Fiction",
        "available": True
    },
    109: {
        "title": "Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "category": "Mystery",
        "available": True
    },
    110: {
        "title": "The Diary of a Young Girl",
        "author": "Anne Frank",
        "category": "Biography",
        "available": True
    }
}


# Display all books and their availability
def display_catalog():
    print("\n" + "=" * 75)
    print("                  DAWGS OF STYLE LIBRARY CATALOG")
    print("=" * 75)
    print(f"{'CATALOG NO.':<15}{'BOOK TITLE':<38}{'CATEGORY':<22}")
    print("-" * 75)

    # Go through each book in the catalog
    for number, book in books.items():
        status = "Available" if book["available"] else "Borrowed"

        print(
            f"{number:<15}"
            f"{book['title'][:36]:<38}"
            f"{book['category']:<22}"
        )
        print(f"{'':<15}Status: {status}")

    print("=" * 75)


# Ask the borrower for their name and selected books
def borrow_books():
    borrowed_books = []

    print("\nWelcome to the Library Book Borrowing System!")

    # Make sure the borrower enters a name
    while True:
        name = input("\nEnter the borrower's full name: ").strip()

        if name:
            break

        print("Name cannot be empty. Please try again.")

    # Allow the borrower to select books by catalog number
    while True:
        display_catalog()

        print("\nEnter a catalog number to borrow a book.")
        print("Enter 0 when you have finished selecting books.")

        if borrowed_books:
            print(f"Books selected: {len(borrowed_books)}")

        choice = input("Catalog number: ").strip()

        # Check whether the input contains only digits
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        catalog_number = int(choice)

        # Stop selecting books when the borrower enters 0
        if catalog_number == 0:
            break

        # Check whether the catalog number exists
        if catalog_number not in books:
            print("That catalog number does not exist.")
            continue

        book = books[catalog_number]

        # Prevent borrowing a book that is unavailable
        if not book["available"]:
            print("Sorry, this book is currently unavailable.")
            continue

        # Prevent selecting the same book more than once
        if any(
            item["catalog_number"] == catalog_number
            for item in borrowed_books
        ):
            print("You have already selected this book.")
            continue

        # Add the selected book to the borrowing list
        borrowed_books.append({
            "catalog_number": catalog_number,
            "title": book["title"],
            "author": book["author"],
            "category": book["category"]
        })

        # Mark the selected book as unavailable
        book["available"] = False

        print(f"\nSuccessfully selected: {book['title']}")

    # Cancel the transaction if no books were selected
    if not borrowed_books:
        print("\nNo books were selected. Transaction cancelled.")
        return

    # Display the borrowing summary in the terminal
    print("\n" + "=" * 50)
    print("             BORROWING SUMMARY")
    print("=" * 50)
    print(f"Borrower: {name}")
    print(f"Number of books: {len(borrowed_books)}")

    for item in borrowed_books:
        print(
            f"{item['catalog_number']} - "
            f"{item['title']} ({item['category']})"
        )

    print("=" * 50)
    print("\nGenerating your Turtle receipt...")

    # Open the graphical receipt
    generate_receipt(name, borrowed_books)


# Create a graphical receipt using Python Turtle
def generate_receipt(name, borrowed_books):
    # Get the current date and time
    receipt_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Increase the receipt height for additional books
    height = max(650, 390 + len(borrowed_books) * 105)

    screen = turtle.Screen()
    screen.title("Library Borrowing Receipt")
    screen.setup(width=850, height=height)
    screen.bgcolor("#F5F1E8")
    screen.tracer(0)

    # Create the turtle used to draw and write the receipt
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    # Calculate the receipt's top position
    window_height = height
    top = window_height // 2 - 35

    # Write text at a specified position on the receipt
    def write_line(x, y, text, size=12, bold=False, align="left"):
        pen.goto(x, y)
        pen.color("#263238")
        pen.write(
            text,
            align=align,
            font=("Arial", size, "bold" if bold else "normal")
        )

    # Draw the outer border of the receipt
    pen.goto(-370, top)
    pen.pendown()
    pen.pensize(3)
    pen.color("#486581")

    pen.goto(370, top)
    pen.goto(370, -window_height // 2 + 30)
    pen.goto(-370, -window_height // 2 + 30)
    pen.goto(-370, top)

    pen.penup()

    # Write the receipt heading
    write_line(0, top - 45, "DAWGS OF STYLE LIBRARY", 23, True, "center")
    write_line(0, top - 75, "BOOK BORROWING RECEIPT", 15, True, "center")

    # Draw a line beneath the heading
    pen.goto(-340, top - 95)
    pen.pendown()
    pen.goto(340, top - 95)
    pen.penup()

    # Display the borrower's information
    y = top - 125

    write_line(-335, y, f"Borrower: {name}", 13, True)
    y -= 28

    write_line(-335, y, f"Date: {receipt_date}", 11)
    y -= 40

    write_line(-335, y, "BORROWED BOOKS", 13, True)
    y -= 30

    # List each borrowed book and its details
    for index, item in enumerate(borrowed_books, start=1):
        write_line(
            -335, y,
            f"{index}. {item['title'][:48]}",
            12, True
        )
        y -= 22

        write_line(
            -315, y,
            f"Catalog No.: {item['catalog_number']}",
            10
        )
        y -= 19

        write_line(
            -315, y,
            f"Category: {item['category']}",
            10
        )
        y -= 32

    # Draw a line above the borrowing total
    pen.goto(-340, y)
    pen.pendown()
    pen.goto(340, y)
    pen.penup()

    y -= 35

    # Display the total number of books borrowed
    write_line(
        0, y,
        f"TOTAL BOOKS BORROWED: {len(borrowed_books)}",
        14, True, "center"
    )

    y -= 38

    # Add a thank-you message at the bottom
    write_line(
        0, y,
        "Thank you for your patronage my guy!",
        12, False, "center"
    )

    y -= 25

    write_line(
        0, y,
        "Please return your books on time my dude.",
        10, False, "center"
    )

    # Display the completed receipt
    screen.update()
    print("\nReceipt displayed. Close the Turtle window to exit.")

    turtle.done()


# Display the main menu and handle the user's choice
def main():
    while True:
        print("\n" + "=" * 45)
        print("            SORTING SYSTEM")
        print("=" * 45)
        print("1. View book catalog and borrow books")
        print("2. Exit")
        print("=" * 45)

        option = input("Select an option: ").strip()

        # Open the borrowing system
        if option == "1":
            borrow_books()

        # Exit the program
        elif option == "2":
            print("\nThank you for visiting the library!")
            break

        # Handle invalid menu selections
        else:
            print("Invalid option. Please choose 1 or 2.")


# Start the program
if __name__ == "__main__":
    main()
