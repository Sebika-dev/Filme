from domain.user_domain import User

class UserRepository:
    def __init__(self, filename):
        self.filename = filename
        self.users=[]
        self.load()

    def load(self):
        users = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    user_id, name, age = line.strip().split(',')
                    users.append(User(int(user_id), name, int(age)))
        except FileNotFoundError:
            pass
        self.users = users

    def save(self):
        with open(self.filename, "w") as file:
            for user in self.get_all():
                file.write(f"{user.id},{user.name},{user.age}\n")

    def get_all(self):
        return self.users

    def gen_id_user(self):
        return max([e.id for e in self.users], default=0) + 1

    def update(self, userupdated: User):
        pos = self.find(userupdated.get_user_id())
        if pos == -1:
            raise ValueError("The user with the given id doesn't exist!")
        self.users[pos] = userupdated
        self.save()

    def find(self, user_id):
        result = list(filter(lambda user: user.get_user_id() == user_id, self.users))
        if not result:
            return -1
        return self.users.index(result[0])

    def add(self, user: User):
        if self.find(user.get_user_id()) != -1:
            raise ValueError("This user exists already!")
        self.users.append(user)
        self.save()

    def delete(self, iduser: int):
        pos = self.find(iduser)
        if pos == -1:
            raise ValueError("The user with the given id doesn't exist!")
        del self.users[pos]
        self.save()