import book_functions
import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print(f"Error Required 1 Arguments Given {len(arguments)}")
    print("" \
    "add - Add A New Book\n" \
    "update - Update Status Of Any Existing Book\n" \
    "list - List All Book Title with Current Status\n" \
    "stats - Lists Stats Of Books\n" \
    "current - Shows Books with stauts of 'Currently Reading'" \
    "")
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
elif argument == 'recommend':
    print("Please wait recommending book!")
    book_functions.recommend_book()
elif argument == 'current':
    print("Currently Reading:")
    book_functions.currently_reading()
elif argument == 'stats':
    print("Books Stats!")
    book_functions.stats()

else:
    print("Invalid Arguments")
