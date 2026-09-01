import email
from uuid import uuid4
from app.models.blogger import Blogger
from app.repositories.blogger_repository import BloggerRepository


def test_that_i_save_blogger(db_session):
    repository = BloggerRepository(db_session)

    blogger = Blogger(
        username="collete",
        email="collete@gmail.com",
        password="123456"
    )
    saved_blogger = repository.save(blogger)

    assert saved_blogger.id == blogger.id
    assert saved_blogger.username == "collete"
    assert saved_blogger.email == "collete@gmail.com"

def test_that_I_find_blogger_by_id(db_session):
    repository = BloggerRepository(db_session)
    blogger = Blogger(
        username="collete",
        email="colly@gmail.com",
        password ="123456"
    )
    repository.save(blogger)
    found_blogger = repository.find_by_id(blogger.id)

    assert found_blogger is not None
    assert found_blogger.id == blogger.id
    assert found_blogger.username == "collete"
    assert found_blogger.email == "colly@gmail.com"

def test_that_I_return_none_when_blogger_does_not_exist(db_session):
    repository = BloggerRepository(db_session)
    blogger_id = uuid4()
    found_blogger = repository.find_by_id(blogger_id)
    assert found_blogger is None

def test_that_I_find_blogger_by_username(db_session):
    repository = BloggerRepository(db_session)

    blogger = Blogger(
        username="collete",
        email = "colly@gmail.com",
        password = "wes123"
    )

    repository.save(blogger)
    found_blogger = repository.find_by_username("collete")

    assert found_blogger is not None
    assert found_blogger.id == blogger.id
    assert found_blogger.username == "collete"
    assert found_blogger.email == "colly@gmail.com"

def test_that_I_return_none_when_username_does_not_exist(db_session):
    repository = BloggerRepository(db_session)
    found_blogger = repository.find_by_username("User not found")

    assert found_blogger is None

def test_that_I_find_blogger_by_email(db_session):
    repository = BloggerRepository(db_session)
    blogger = Blogger(
        username="collete",
        email="collete@gmail.com",
        password="123456"
    )
    repository.save(blogger)
    found_blogger = repository.find_by_email("collete@gmail.com")
    assert found_blogger is not None
    assert found_blogger.id == blogger.id
    assert found_blogger.username == "collete"
    assert found_blogger.email == "collete@gmail.com"

def test_that_I_return_none_when_email_does_not_exist(db_session):
    repository = BloggerRepository(db_session)
    found_blogger = repository.find_by_email("unknown@gmail.com")
    assert found_blogger is None

def test_that_I_find_all_bloggers(db_session):
    repository = BloggerRepository(db_session)
    blogger_one = Blogger(
        username="collete",
        email="collete@gmail.com",
        password="123456"
    )
    blogger_two = Blogger(
        username="john",
        email="john@gmail.com",
        password="password123"
    )
    repository.save(blogger_one)
    repository.save(blogger_two)
    bloggers = repository.find_all()
    assert len(bloggers) == 2
    assert bloggers[0].username == "collete"
    assert bloggers[1].username == "john"

def test_that_find_all_returns_empty_list_when_no_bloggers_exist(db_session):
    repository = BloggerRepository(db_session)
    bloggers = repository.find_all()
    assert bloggers == []

def test_that_I_update_a_blogger(db_session):
    repository = BloggerRepository(db_session)
    blogger = Blogger(
        username="collete",
        email="collete@gmail.com",
        password="123456"
    )
    repository.save(blogger)
    blogger.username = "colletecolly"
    blogger.email = "colly@gmail.com"
    updated_blogger = repository.update(blogger)

    assert updated_blogger.username == "colletecolly"
    assert updated_blogger.email == "colly@gmail.com"

def test_that_updated_blogger_is_persisted(db_session):
    repository = BloggerRepository(db_session)

    blogger = Blogger(
        username="collete",
        email="collete@gmail.com",
        password="123456"
    )

    repository.save(blogger)
    blogger.username = "new_username"
    blogger.email = "new@gmail.com"

    repository.update(blogger)

    found_blogger = repository.find_by_id(blogger.id)

    assert found_blogger.username == "new_username"
    assert found_blogger.email == "new@gmail.com"