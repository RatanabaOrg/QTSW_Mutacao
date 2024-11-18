import pytest
from user import User

@pytest.fixture
def user():
    return User("test_user", "test@example.com")

def test_activate(user):
    user.deactivate()
    assert not user.active
    user.activate()
    assert user.active

def test_deactivate(user):
    user.deactivate()
    assert not user.active

def test_update_email(user):
    user.update_email("new_email@example.com")
    assert user.email == "new_email@example.com"

def test_update_email_invalid(user):
    with pytest.raises(ValueError):
        user.update_email("invalid_email")

def test_update_email_edge_case(user):
    user.update_email("test@domain.com")
    assert user.email == "test@domain.com"

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
