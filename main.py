import book_functions
import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print(f"Error Required 1 Arguments Given {len(arguments)}")
    sys.exit()

argument = arguments[0]


if argument == "add":
    title = input("Enter Book's Title: ")
    author = input("Enter Book's Author: ")
    series_name = input("Enter Book's Series Name If Applicable(Type None if not a series): ")
    series_no = 0
    if series_name.lower() != "none":
        series_no = int(input("Enter Book's Series Number If Applicable: "))
    else:
        series_no = 0

    genre = input("Enter Book's Genre: ")
    book_type = input("Enter Book Type (F (Fiction) Or NF (Non Fiction)): ")
    book_functions.add_book(title,author,series_name,series_no,genre,book_type)
elif argument == "list":
    book_functions.list_books()
elif argument == 'update':
    name =  input("Enter Title of the book: ")
    status = input("Enter Status of Book (R-Read CR-Currently Reading, DNF- Did Not Finish, NR- Not Read): ")
    current_status = None
    match status:
        case "R":
            current_status = "Read"
        case "CR":
            current_status = "Currently Reading"
        case "DNF":
            current_status = "Did Not Finish"
        case "NR":
            current_status = "Not Read"

    book_functions.update_book(name,current_status)

else:
    print("Invalid Arguments")
