import book_functions


title = input("Enter Book's Title: ")
author = input("Enter Book's Author: ")
series_name = input("Enter Book's Series If Applicable(Type None if not a series): ")
series_no = 0
if series_name.lower() != "none":
    series_no = int(input("Enter Book's Series Number If Applicable: "))
else:
    series_no = 0

genre = input("Enter Book's Genre: ")
book_type = input("Enter Book Type (F (Fiction) Or NF (Non Fiction)): ")
book_functions.add_book(title,author,series_name,series_no,genre,book_type)