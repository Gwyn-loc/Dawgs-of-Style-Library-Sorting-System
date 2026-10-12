
import os
import turtle
from datetime import datetime

os.system("title Sorting System")

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


def display_catalog():
    print("\n" + "=" * 75)
    print("                  DAWGS OF STYLE LIBRARY CATALOG")
    print("=" * 75)
    print(f"{'CATALOG NO.':<15}{'BOOK TITLE':<38}{'CATEGORY':<22}")
    print("-" * 75)

    for number, book in books.items():
        status = "Available" if book["available"] else "Borrowed"

        print(
            f"{number:<15}"
            f"{book['title'][:36]:<38}"
            f"{book['category']:<22}"
        )
        print(f"{'':<15}Status: {status}")

    print("=" * 75)


def borrow_books():
    borrowed_books = []

    print("\nWelcome to the Library Book Borrowing System!")

    while True:
        name = input("\nEnter the borrower's full name: ").strip()

        if name:
            break

        print("Name cannot be empty. Please try again.")

    while True:
        display_catalog()

        print("\nEnter a catalog number to borrow a book.")
        print("Enter 0 when you have finished selecting books.")

        if borrowed_books:
            print(f"Books selected: {len(borrowed_books)}")

        choice = input("Catalog number: ").strip()

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        catalog_number = int(choice)

        if catalog_number == 0:
            break

        if catalog_number not in books:
            print("That catalog number does not exist.")
            continue

        book = books[catalog_number]

        if not book["available"]:
            print("Sorry, this book is currently unavailable.")
            continue

        if any(
            item["catalog_number"] == catalog_number
            for item in borrowed_books
        ):
            print("You have already selected this book.")
            continue

        borrowed_books.append({
            "catalog_number": catalog_number,
            "title": book["title"],
            "author": book["author"],
            "category": book["category"]
        })

        book["available"] = False

        print(f"\nSuccessfully selected: {book['title']}")

    if not borrowed_books:
        print("\nNo books were selected. Transaction cancelled.")
        return

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

    generate_receipt(name, borrowed_books)


def generate_receipt(name, borrowed_books):
    receipt_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    height = max(600, 330 + len(borrowed_books) * 65)

    screen = turtle.Screen()
    screen.title("Library Borrowing Receipt")
    screen.setup(width=850, height=min(height, 1000))
    screen.bgcolor("#F5F1E8")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    window_height = min(height, 1000)
    top = window_height // 2 - 35

    def write_line(x, y, text, size=12, bold=False, align="left"):
        pen.goto(x, y)
        pen.color("#263238")
        pen.write(
            text,
            align=align,
            font=("Arial", size, "bold" if bold else "normal")
        )

    pen.goto(-370, top)
    pen.pendown()
    pen.pensize(3)
    pen.color("#486581")

    pen.goto(370, top)
    pen.goto(370, -window_height // 2 + 30)
    pen.goto(-370, -window_height // 2 + 30)
    pen.goto(-370, top)

    pen.penup()

    write_line(0, top - 45, "DAWGS OF STYLE LIBRARY", 23, True, "center")
    write_line(0, top - 75, "BOOK BORROWING RECEIPT", 15, True, "center")

    pen.goto(-340, top - 95)
    pen.pendown()
    pen.goto(340, top - 95)
    pen.penup()

    y = top - 125

    write_line(-335, y, f"Borrower: {name}", 13, True)
    y -= 28

    write_line(-335, y, f"Date: {receipt_date}", 11)
    y -= 40

    write_line(-335, y, "BORROWED BOOKS", 13, True)
    y -= 30

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

    pen.goto(-340, y)
    pen.pendown()
    pen.goto(340, y)
    pen.penup()

    y -= 35

    write_line(
        0, y,
        f"TOTAL BOOKS BORROWED: {len(borrowed_books)}",
        14, True, "center"
    )

    y -= 38

    write_line(
        0, y,
        "Thank you for your patronage my guy !",
        12, False, "center"
    )

    y -= 25

    write_line(
        0, y,
        "Please return your books on time my dude.",
        10, False, "center"
    )

    screen.update()
    print("\nReceipt displayed. Close the Turtle window to exit.")

    turtle.done()


def main():
    while True:
        print("\n" + "=" * 45)
        print("            SORTING SYSTEM")
        print("=" * 45)
        print("1. View book catalog and borrow books")
        print("2. Exit")
        print("=" * 45)

        option = input("Select an option: ").strip()

        if option == "1":
            borrow_books()
        elif option == "2":
            print("\nThank you for visiting the library!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
