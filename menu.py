from interface.movie_interface import movie_menu
from interface.user_interface import user_menu
from interface.watchlist_interface import watchlist_menu

def show_main_menu():
    print("\nFilm Management Menu:")
    print("1. User management menu")
    print("2. Movie management menu")
    print("3. Watchlist management menu")
    print("4. Quit")

def main():
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            movie_menu()
        elif choice == "3":
            watchlist_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()