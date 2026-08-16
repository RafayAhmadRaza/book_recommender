import json
import os
import random

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

def update_book(Name,status):
    if os.path.exists(path):
        book_to_update_list = []
        with open(path,"r") as f:
            books = json.load(f)
            for i in books:
                if i['Title'][:len(Name)] == Name:
                    book_to_update_list.append(i)
                    print("Book")
                else:
                    continue

            if len(book_to_update_list) == 0:
                print("Error Book Does Not Exist")
            else:
                if len(book_to_update_list) == 1:
                    book_to_update_list[0]['Status'] = status
                    print(book_to_update_list)
                    for i in range(len(books)):
                        if books[i]['Title'] == book_to_update_list[0]["Title"]:
                            books[i] = book_to_update_list
                            break
                        else:
                            continue

                    print(books)

                else:
                    for i in range(len(book_to_update_list)):
                        print(f"{i} - {book_to_update_list[i]}")

                    book_number = int(input("Enter The Book Number: "))
                    book_to_be_update = book_to_update_list[book_number]
                    book_to_be_update["Status"] = status
                    print(book_to_be_update)

                    for i in range(len(books)):
                        if books[i]['Title'] == book_to_be_update['Title']:
                            books[i] = book_to_be_update
                            break
                        else:
                            continue
                    print(books)

        with open(path,'w') as f:
            json.dump(books,f,indent=4)


    else:
        print("Error .json database does not exist")

def recommend_book():
    with open(path,"r") as f:
        books = json.dump(f)
        random.choice(books)