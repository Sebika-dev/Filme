from repository.watchlist_repository import WatchlistRepository
from repository.movie_repository import MovieRepository
from service.watchlist_service import ServiceWatchlists

def show_watchlist_menu():
    print("\nWatchlist Management Menu:")
    print("1. Add a movie to a watchlist")
    print("2. Edit a watchlist")
    print("3. Filter movies by actor")
    print("4. Filter movies by IMDb rating")
    print("5. Count movies by actor")
    print("6. Calculate average IMDb rating for an actor")
    print("7. Exit")

def add_movie_to_watchlist(service_watchlist):
    try:
        watchlist_id = int(input("Enter watchlist ID: "))
        movie_id = int(input("Enter movie ID to add: "))
        service_watchlist.add_movie_to_watchlist(watchlist_id, movie_id)
        print("Movie added to watchlist successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def edit_watchlist(service_watchlist):
    try:
        watchlist_id = int(input("Enter watchlist ID to edit: "))
        movie_ids = list(map(int, input("Enter new movie IDs (comma-separated): ").split(",")))
        service_watchlist.edit_watchlist(watchlist_id, movie_ids)
        print("Watchlist updated successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def filter_movies_by_actor(service_watchlist):
    actor_name = input("Enter actor name to filter by: ")
    movies = service_watchlist.filter_movies_by_actor(actor_name)
    if movies:
        print(f"Movies with actor {actor_name}:")
        for movie in movies:
            print(movie)
    else:
        print(f"No movies found for actor: {actor_name}")

def filter_movies_by_imdb(service_watchlist):
    try:
        min_rating = float(input("Enter minimum IMDb rating to filter by: "))
        movies = service_watchlist.filter_movies_by_imdb(min_rating)
        if movies:
            print("Movies with IMDb rating above specified value:")
            for movie in movies:
                print(movie)
        else:
            print(f"No movies found with IMDb rating above {min_rating}")
    except ValueError as e:
        print(f"Error: {e}")

def count_movies_by_actor(service_watchlist):
    actor_name = input("Enter actor name to count movies: ")
    count = service_watchlist.count_movies_with_actor(actor_name)
    print(f"Number of movies with actor {actor_name}: {count}")

def calculate_average_imdb_for_actor(service_watchlist):
    actor_name = input("Enter actor name to calculate average IMDb rating: ")
    average_rating = service_watchlist.average_imdb_for_actor(actor_name)
    print(f"Average IMDb rating for actor {actor_name}: {average_rating:.2f}")

def watchlist_menu():
    file_path = "../watchlists.txt"
    movie_path = "../movies.txt"
    watchlist_repository = WatchlistRepository(file_path)
    movie_repository = MovieRepository(movie_path)
    service_watchlist = ServiceWatchlists(watchlist_repository, movie_repository)

    while True:
        show_watchlist_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie_to_watchlist(service_watchlist)
        elif choice == "2":
            edit_watchlist(service_watchlist)
        elif choice == "3":
            filter_movies_by_actor(service_watchlist)
        elif choice == "4":
            filter_movies_by_imdb(service_watchlist)
        elif choice == "5":
            count_movies_by_actor(service_watchlist)
        elif choice == "6":
            calculate_average_imdb_for_actor(service_watchlist)
        elif choice == "7":
            print("Exiting watchlist management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")