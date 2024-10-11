import json

# Movie database dictionary
movies = {}

# Function to add a new movie
def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ")
    director = input("Enter movie director: ")
    year = input("Enter release year: ")
    actors = input("Enter actors (comma-separated): ").split(',')

    movies[title] = {
        "year": year,
        "genre": genre,
        "director": director,
        "actors": actors
    }
    print(f"Movie '{title}' added successfully!\n")

# Function to edit an existing movie
def edit_movie():
    title = input("Enter the title of the movie to edit: ")
    if title in movies:
        print(f"Editing movie: {title}")
        genre = input("Enter new genre (leave blank to keep current): ")
        director = input("Enter new director (leave blank to keep current): ")
        year = input("Enter new release year (leave blank to keep current): ")
        actors = input("Enter new actors (comma-separated, leave blank to keep current): ")

        if genre:
            movies[title]["genre"] = genre
        if director:
            movies[title]["director"] = director
        if year:
            movies[title]["year"] = year
        if actors:
            movies[title]["actors"] = actors.split(',')

        print(f"Movie '{title}' updated successfully!\n")
    else:
        print(f"Movie '{title}' not found.\n")

# Function to delete a movie
def delete_movie():
    title = input("Enter the title of the movie to delete: ")
    if title in movies:
        del movies[title]
        print(f"Movie '{title}' deleted successfully!\n")
    else:
        print(f"Movie '{title}' not found.\n")

# Function to view all movies
def view_movies():
    if movies:
        for title, info in movies.items():
            print(f"Title: {title}")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
            print()
    else:
        print("No movies in the database.\n")

# Function to search for a movie by title, director, or genre
def search_movie():
    search_type = input("Search by (1) Title, (2) Director, (3) Genre: ")
    query = input("Enter your search query: ")

    found = False
    for title, info in movies.items():
        if (search_type == '1' and title.lower() == query.lower()) or \
           (search_type == '2' and info['director'].lower() == query.lower()) or \
           (search_type == '3' and info['genre'].lower() == query.lower()):
            print(f"Title: {title}")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
            print()
            found = True

    if not found:
        print(f"No movie found matching your query '{query}'.\n")

# Function to save the database to a file
def save_movies():
    with open('movies.json', 'w') as f:
        json.dump(movies, f)
    print("Movies saved to file successfully!\n")

# Function to load the database from a file
def load_movies():
    global movies
    try:
        with open('movies.json', 'r') as f:
            movies = json.load(f)
        print("Movies loaded from file successfully!\n")
    except FileNotFoundError:
        print("No saved movie database found.\n")

# Main menu
def main_menu():
    while True:
        print("Movie Database Management System")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. View All Movies")
        print("5. Search Movie")
        print("6. Save Movies")
        print("7. Load Movies")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            edit_movie()
        elif choice == '3':
            delete_movie()
        elif choice == '4':
            view_movies()
        elif choice == '5':
            search_movie()
        elif choice == '6':
            save_movies()
        elif choice == '7':
            load_movies()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Load any existing data and run the program
load_movies()
main_menu()
