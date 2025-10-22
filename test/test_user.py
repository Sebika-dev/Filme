from domain.user_domain import User
from repository.user_repository import UserRepository
from service.user_service import UserService


def test_add_user():
    test_file_path = "test_users.txt"
    repo = UserRepository(test_file_path)
    service = UserService(repo)

    service.add_user("Andrei", 30)
    all_users = repo.get_all()

    assert len(all_users) == 1
    assert all_users[0].name == "Andrei"
    assert all_users[0].age == 30

    cleanup(test_file_path)


def test_get_all_users():
    test_file_path = "test_users.txt"
    repo = UserRepository(test_file_path)
    service = UserService(repo)

    service.add_user("Andrei", 30)
    service.add_user("Misu", 25)
    all_users = repo.get_all()

    assert len(all_users) == 2
    assert all_users[0].name == "Andrei"
    assert all_users[1].name == "Misu"

    cleanup(test_file_path)


def test_remove_user():
    test_file_path = "test_users.txt"
    repo = UserRepository(test_file_path)
    service = UserService(repo)

    service.add_user("Andrei", 30)
    service.add_user("Misu", 25)
    all_users = repo.get_all()

    assert len(all_users) == 2

    service.remove_user(all_users[0].id)
    all_users = repo.get_all()

    assert len(all_users) == 1
    assert all_users[0].name == "Misu"

    cleanup(test_file_path)


def test_update_user():
    test_file_path = "test_users.txt"
    repo = UserRepository(test_file_path)
    service = UserService(repo)

    service.add_user("Andrei", 30)
    all_users = repo.get_all()
    user_to_update = all_users[0]

    updated_user = User(user_to_update.id, "Andrei Updated", 35)
    repo.update(updated_user)
    all_users = repo.get_all()

    assert len(all_users) == 1
    assert all_users[0].name == "Andrei Updated"
    assert all_users[0].age == 35
    cleanup(test_file_path)


def cleanup(file_path):
    import os
    if os.path.exists(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    test_add_user()
    print("test_add_user passed")
    test_get_all_users()
    print("test_get_all_users passed")
    test_remove_user()
    print("test_remove_user passed")
    test_update_user()
    print("test_update_user passed")