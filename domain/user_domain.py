class User:
    def __init__(self, user_id, name, age):
        self.id = user_id
        self.name = name
        self.age = age

    def get_user_id(self):
        return self.id
    def set_user_id(self, value):
        self.id = value
    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value
    def get_age(self):
        return self.age
    def set_age(self, value):
        self.age = value

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"