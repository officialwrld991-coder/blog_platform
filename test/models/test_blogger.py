from models.blogger import Blogger
from models.user_role import Role


def test_create_blogger():
    blogger = Blogger(
        username="collete",
        email="collete@example.com",
        password="password123"
    )

    assert blogger.username == "collete"
    assert blogger.email == "collete@example.com"
    assert blogger.password == "password123"
    assert blogger.role == Role.BLOGGER