import json
import os

def add_book(Title,Author,Series_Name,Series_No,Genre,Book_Type):



    if(Series_Name == "None"):
        Series_Name = None
        Series_No = 0

        book_dict = {
            "Title":Title,
            "Author":Author,
            "Series Name": Series_Name,
            "Series No": Series_No,
            "Genres": Genre,
            "Book Type": "Fiction" if Book_Type.upper() =="F" else "Non-Fiction",
            "Status": "Not Read"
            }
        book_json = (json.dumps(book_dict))

        if os.path.exists("books_database_json"):
            with open('books_database.json',"r") as f:
                books = json.load(f)
        else:
            books= []

        books.append(book_dict)

        with open("books_database.json","w") as f:
            json.dump(books,f,indent=4)

    else:    

        book_dict = {
            "Title":Title,
            "Author":Author,
            "Series Name": Series_Name,
            "Series No": Series_No,
            "Genres": Genre,
            "Book Type": "Fiction" if Book_Type.upper() =="F" else "Non-Fiction",
            "Status":"Not Read"
            }

        if os.path.exists("books_database_json"):
            with open('books_database.json',"r") as f:
                books = json.load(f)
        else:
            books= []

        books.append(book_dict)

        with open("books_database.json","w") as f:
            json.dump(books,f,indent=4)
