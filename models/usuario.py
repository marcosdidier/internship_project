class User:
    _id_counter = 1

    def __init__(self, name: str, email: str):
        self.id = User._id_counter
        self.name = name
        self.email = email
        User._id_counter += 1

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.name} | Email: {self.email}"
    