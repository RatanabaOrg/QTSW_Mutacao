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