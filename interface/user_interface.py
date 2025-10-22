from domain.user_domain import User
from repository.user_repository import UserRepository
from service.user_service import UserService

def show_menu():
    print("\nUser Management Menu:")
    print("1. Show all users")
    print("2. Add a user")
    print("3. Remove a user")
    print("4. Update a user")
    print("5. Exit")

def show_all_users(user_service):
    users = user_service.get_users()
    if not users:
        print("No users available.")
    else:
        for user in users:
            print(f"ID:{user.get_user_id()}, {user.get_name()}, {user.get_age()}")

def add_user(user_service):
    try:
        name = input("Enter user name: ")
        age = int(input("Enter user age: "))
        user_service.add_user(name, age)
        print("User added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def remove_user(user_service):
    try:
        user_id = int(input("Enter user ID to remove: "))
        user_service.remove_user(user_id)
        print("User removed successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def update_user(user_service):
    try:
        user_id = int(input("Enter user ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        updated_user = User(user_id, name, age)
        user_service.update_user(updated_user)
        print("User updated successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def user_menu():
    file_path = "../users.txt"
    user_repository = UserRepository(file_path)
    user_service = UserService(user_repository)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_users(user_service)
        elif choice == "2":
            add_user(user_service)
        elif choice == "3":
            remove_user(user_service)
        elif choice == "4":
            update_user(user_service)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")