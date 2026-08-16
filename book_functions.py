import json
import os

path = "books_database.json"

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
 
        if os.path.exists(path):
            with open(path,"r") as f:
                books = json.load(f)
        else:
            books= []

        books.append(book_dict)
        with open(path,"w") as f:
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

        if os.path.exists(path):
            with open(path,"r") as f:
                books = json.load(f)
        else:
            books= []

        books.append(book_dict)

        with open(path,"w") as f:
            json.dump(books,f,indent=4)

def list_books():
    if os.path.exists(path):
        with open(path,'r') as f:
            books = json.load(f)
            for i in books:
                print(i['Title'] +" " +i['Status'])
    else:
        print("Error .json database does not exist.")

def update_book(Name):
    pass