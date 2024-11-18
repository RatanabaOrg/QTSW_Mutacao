import pytest
from user import UserManager

@pytest.fixture
def manager():
    manager = UserManager()
    manager.add_user("user1", "user1@example.com")
    manager.add_user("user2", "user2@example.com")
    return manager

def test_add_user(manager):
    manager.add_user("user3", "user3@example.com")
    user = manager.find_user("user3")
    assert user is not None
    assert user.email == "user3@example.com"

def test_add_user_duplicate(manager):
    with pytest.raises(ValueError): 
        manager.add_user("user1", "new_email@example.com")

def test_remove_user(manager):
    manager.remove_user("user1")
    user = manager.find_user("user1")
    assert user is None

def test_find_user(manager):
    user = manager.find_user("user2")
    assert user is not None
    assert user.username == "user2"

def test_deactivate_user(manager):
    manager.deactivate_user("user2")
    user = manager.find_user("user2")
    assert not user.active

def test_deactivate_user_not_found(manager):
    with pytest.raises(ValueError):  
        manager.deactivate_user("non_existent_user")
