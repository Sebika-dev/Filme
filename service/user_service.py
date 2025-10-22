from domain.user_domain import User
from repository.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.UserRepository = user_repo

    def add_user(self, name: str, age: int):
        for user in self.UserRepository.get_all():
            if user.name == name and user.age == age:
                raise ValueError("Utilizatorul exista deja!")
        idnou = self.UserRepository.gen_id_user()
        usernou = User(idnou, name, age)
        self.UserRepository.add(usernou)

    def remove_user(self, iduser):
        self.UserRepository.delete(iduser)

    def update_user(self, iduser):
        self.UserRepository.update(iduser)

    def get_users(self):
        return self.UserRepository.get_all()