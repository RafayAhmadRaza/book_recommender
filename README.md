# Book Recommender

> A tiny command-line TBR manager that tells me what to read because apparently choosing a book myself is too difficult.

Book Recommender is a simple Python CLI application for managing a personal **To-Be-Read (TBR)** library.

I originally started this project as a way to learn how to work with **JSON files in Python**. It eventually turned into a small book-management system because I wanted an easier way to keep track of my books and, more importantly, remove the decision paralysis of figuring out what to read next.

The entire database is stored locally in a JSON file.

## Features

* Add books to your TBR
* List your books and their status
* Search for books using partial titles
* Update book status
* Track:

  * Not Read
  * Currently Reading
  * Read
  * Did Not Finish
* Track fiction and non-fiction
* Store genres
* Store series names and series numbers
* Display currently reading books
* Display library statistics
* Randomly recommend a book
* Prevent recommending books that have already been read
* Avoid recommending books that are currently being read
* Respect series reading order
* Avoid recommending another book from a series that is already being read

## The Recommender

The main purpose of this project is to remove **decision paralysis**.

Instead of staring at a TBR list wondering what to read, I can simply run:

```bash
python main.py recommend
```

The program randomly selects an eligible book and checks its series information.

For example, if it randomly selects:

```text
The Reckoning of Roku
```

but earlier books in the series have not been read, it will instead recommend the appropriate earlier book.

```text
Please wait recommending book!

The Book recommend is:
The Reckoning of Roku

The Book is number 5 in the series
Please Read:
Avatar, The Last Airbender: The Rise Of Kyoshi
```

If a book from that series is already being read, the recommender avoids recommending another book from the same series.

The goal is basically:

> **Let the computer decide what I read, but don't let the computer make me read book #5 before book #1.**

## Commands

### Add a book

```bash
python main.py add
```

The program asks for:

* Title
* Author
* Series
* Series number
* Genre
* Fiction / Non-Fiction

### List books

```bash
python main.py list
```

Example:

```text
Gideon The Ninth Not Read fantasy
Strange Pictures Not Read horror
NeuroTribes Not Read history, psychology, science
```

### Update a book

```bash
python main.py update
```

You can change a book's status:

```text
R   - Read
CR  - Currently Reading
DNF - Did Not Finish
NR  - Not Read
```

Partial titles are supported, so entering:

```text
Gideon
```

can find:

```text
Gideon The Ninth
```

If multiple books match the search, the program lets you select the correct one.

### Currently Reading

```bash
python main.py current
```

Displays books that are currently being read.

### Statistics

```bash
python main.py stats
```

Example:

```text
Books Stats!

Books in TBR: 21
Currently Reading: 0
Finished: 0
DNF: 0
Fiction: 16
Non-Fiction: 5
Series: 6
Standalone: 8
```

### Recommend

```bash
python main.py recommend
```

Randomly selects an appropriate unread book while taking reading status and series order into account.

## Data Storage

Books are stored in:

```text
books_database.json
```

Each book is represented as a JSON object:

```json
{
    "Title": "Gideon The Ninth",
    "Author": "Tamsyn Muir",
    "Series Name": "The Locked Tomb",
    "Series No": 1,
    "Genres": "fantasy",
    "Book Type": "Fiction",
    "Status": "Not Read"
}
```

This project intentionally uses JSON instead of a database because the main goal was to learn how Python handles structured data and file persistence.

## Project Structure

```text
book_recommender/w
├── main.py
├── book_functions.py
├── books_database.json
└── README.md
```

### `main.py`

Handles the command-line interface and user input.

### `book_functions.py`

Contains the book-management functionality, including adding, updating, listing, statistics, and recommendations.

### `books_database.json`

The local book database.

## Requirements

* Python 3.10+

No external dependencies are required.

## Why I Made This

I had a growing list of books I wanted to read and kept running into the same problem:

> **What the hell do I read next?**

I already had a TBR list, but having a list of 20+ books somehow made choosing one harder rather than easier.

So instead of opening StoryGraph repeatedly and staring at the list, I decided to make a small Python program that could just pick something for me.

It started as a project to learn JSON.

It became a personal librarian.

## What I Learned

This project has been primarily about learning Python rather than building a sophisticated application.

While making it, I practiced:

* Reading and writing files
* JSON serialization and deserialization
* Lists and dictionaries
* Searching and filtering data
* Modifying nested data structures
* Random selection
* Command-line arguments
* Functions and program structure
* Working with persistent application data
* Handling edge cases
* Basic application logic

The series recommendation system in particular became an exercise in thinking about relationships between pieces of data.

## Future Ideas

Possible future improvements:

* Remove books
* Search by author or genre
* Filter recommendations by genre
* Better statistics
* Reading history
* Reading streaks
* More robust series handling
* Unit tests
* Better CLI output

## Disclaimer

This is a small personal learning project.

It is intentionally simple and stores everything locally in a JSON file. It is not intended to replace dedicated book-management applications.

It does, however, have one very important feature:

**It tells me what to read so I don't have to decide.**
