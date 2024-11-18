class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.active = True

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def update_email(self, new_email):
        if "@" not in new_email:
            raise ValueError("Invalid email address")
        self.email = new_email

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, email):
        if any(user.username == username for user in self.users):
            raise ValueError("Username already exists")
        self.users.append(User(username, email))

    def remove_user(self, username):
        self.users = [user for user in self.users if user.username != username]

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def deactivate_user(self, username):
        user = self.find_user(username)
        if not user:
            raise ValueError("User not found")
        user.deactivate()
