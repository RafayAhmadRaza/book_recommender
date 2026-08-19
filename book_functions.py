import json
import os
import random

path = "books_database.json"


def add_book(Title, Author, Series_Name, Series_No, Genre, Book_Type):
    if Series_Name == "None":
        Series_Name = None
        Series_No = 0

        book_dict = {
            "Title": Title,
            "Author": Author,
            "Series Name": Series_Name,
            "Series No": Series_No,
            "Genres": Genre,
            "Book Type": "Fiction" if Book_Type.upper() == "F" else "Non-Fiction",
            "Status": "Not Read",
        }

        if os.path.exists(path):
            with open(path, "r") as f:
                books = json.load(f)
        else:
            books = []

        books.append(book_dict)
        with open(path, "w") as f:
            json.dump(books, f, indent=4)

    else:
        book_dict = {
            "Title": Title,
            "Author": Author,
            "Series Name": Series_Name,
            "Series No": Series_No,
            "Genres": Genre,
            "Book Type": "Fiction" if Book_Type.upper() == "F" else "Non-Fiction",
            "Status": "Not Read",
        }

        if os.path.exists(path):
            with open(path, "r") as f:
                books = json.load(f)
        else:
            books = []

        books.append(book_dict)

        with open(path, "w") as f:
            json.dump(books, f, indent=4)


def list_books():
    if os.path.exists(path):
        with open(path, "r") as f:
            books = json.load(f)
            books = sorted(books,key=lambda book: book['Title'])
            for i in books:
                print(i["Title"] + " " + i["Status"] + " " + i["Genres"])
    else:
        print("Error .json database does not exist.")


def update_book(Name, status):
    if os.path.exists(path):
        book_to_update_list = []
        with open(path, "r") as f:
            books = json.load(f)
            for i in books:
                if i["Title"][: len(Name)] == Name:
                    book_to_update_list.append(i)
                else:
                    continue

            if len(book_to_update_list) == 0:
                print("Error Book Does Not Exist")
            else:
                if len(book_to_update_list) == 1:
                    book_to_update_list[0]["Status"] = status
                    print(book_to_update_list)
                    for i in range(len(books)):
                        if books[i]["Title"] == book_to_update_list[0]["Title"]:
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
                        if books[i]["Title"] == book_to_be_update["Title"]:
                            books[i] = book_to_be_update
                            break
                        else:
                            continue

        with open(path, "w") as f:
            json.dump(books, f, indent=4)

    else:
        print("Error .json database does not exist")


def recommend_book():
    with open(path, "r") as f:
        books_list = json.load(f)
        books = []
        for i in range(len(books_list)):
            if (
                books_list[i]["Status"] == "Read"
                or books_list[i]["Status"] == "Currently Reading"
                or books_list[i]["Status"] == "Did Not Finish"
            ):
                continue
            else:
                books.append(books_list[i])

        book = random.choice(books)

        if book["Series Name"] != None:
            series_book = []
            for i in range(len(books)):
                if book["Series Name"] == books[i]["Series Name"]:
                    series_book.append(books[i])
                else:
                    continue
            if len(series_book) == 1:
                print(
                    "This Books is part of a series! Do add the other books in the series!"
                )
                print(book["Title"])
            else:
                for i in range(len(series_book)):
                    if book["Series No"] > series_book[i]["Series No"]:
                        if series_book[i]["Status"] == "Not Read":
                            print(f"The Book recommend is: \n{book['Title']}")
                            print(
                                f"The Book is number {book['Series No']} in the series"
                            )
                            print(f"Please Read {series_book[i]['Title']}")
                            break

                        if series_book[i]["Status"] == "Currently Reading":
                            print(
                                "You are already reading a book from this series! Recommending another book"
                            )
                            series_name = series_book[0]["Series Name"]
                            filtered_book_list = []

                            for i in range(len(books)):
                                if books[i]["Series Name"] == series_name:
                                    continue
                                else:
                                    if books[i]["Status"] == "Not Read":
                                        filtered_book_list.append(books[i])

                            new_book = random.choice(filtered_book_list)

                            print("New book is!")
                            print(f"{new_book['Title']}")
                            break
                    else:
                        print(book["Title"])
                        break
        else:
            print(book["Title"])


def currently_reading():
    with open(path, "r") as f:
        books = json.load(f)

        for i in range(len(books)):
            if books[i]["Status"] == "Currently Reading":
                print(books[i]["Title"])


def stats():
    with open(path, "r") as f:
        books = json.load(f)
        currently_reading_counter = 0
        Finished_counter = 0
        DNF_counter = 0
        Fiction_counter = 0
        Non_Fiction_Counter = 0
        Series_Counter = 0
        Standalone_Counter = 0
        book_series_list = []

        for i in range(len(books)):
            if books[i]["Status"] == "Currently Reading":
                currently_reading_counter += 1
            if books[i]["Status"] == "Did Not Finish":
                DNF_counter += 1
            if books[i]["Status"] == "Read":
                Finished_counter += 1

            if books[i]["Book Type"] == "Fiction":
                Fiction_counter += 1
            else:
                Non_Fiction_Counter += 1

            if books[i]["Series Name"] == None:
                Standalone_Counter += 1
            else:
                if len(book_series_list) == 0:
                    book_series_list.append(books[i]["Series Name"])
                    Series_Counter += 1
                else:
                    if books[i]["Series Name"] in book_series_list:
                        continue
                    else:
                        book_series_list.append(books[i]["Series Name"])
                        Series_Counter += 1
        print(
            "Books in TBR: ",
            (len(books) - (currently_reading_counter + DNF_counter + Finished_counter)),
        )
        print("Currently Reading: ", currently_reading_counter)
        print("Finished: ", Finished_counter)
        print("DNF: ", DNF_counter)
        print("Fiction: ", Fiction_counter)
        print("Non-Fiction: ", Non_Fiction_Counter)
        print("Series: ", Series_Counter)
        print("Standalone: ", Standalone_Counter)
