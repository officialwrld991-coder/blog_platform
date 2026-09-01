from app.models.blogger import Blogger, CreateBlogger
from app.services.blogger_service import BloggerService


def test_that_i_can_create_a_blogger(db_session):
    service = BloggerService(db_session)
    blogger_data = CreateBlogger(
        username="colly",
        email="colly@gmail.com",
        password="wes123"
    )
    blogger = service.create_blogger(blogger_data)

    assert blogger.username == "colly"
    assert blogger.email == "colly@gmail.com"
    assert blogger.password == "wes123"

def test_that_i_can_find_a_blogger_by_id(db_session):
    service = BloggerService(db_session)

    blogger = Blogger(
        username="colly",
        email="colly@gmail.com",
        password="wes123"
    )

    db_session.add(blogger)
    db_session.commit()
    db_session.refresh(blogger)

    found_blogger = service.find_blogger_by_id(blogger.id)

    assert found_blogger is not None
    assert found_blogger.id == blogger.id
    assert found_blogger.username == "colly"
    assert found_blogger.email == "colly@gmail.com"

def test_that_i_can_find_a_blogger_by_username(db_session):
    service = BloggerService(db_session)

    blogger = Blogger(
        username="collete",
        email="colly@gmail.com",
        password="wes123"
    )

    db_session.add(blogger)
    db_session.commit()
    db_session.refresh(blogger)

    found_blogger = service.find_blogger_by_username("collete")

    assert found_blogger is not None
    assert found_blogger.id == blogger.id
    assert found_blogger.username == "collete"
    assert found_blogger.email == "colly@gmail.com"

def test_that_i_can_find_a_blogger_by_email(db_session):
    service = BloggerService(db_session)

    blogger = Blogger(
        username="collete",
        email="colly@gmail.com",
        password="wes123"
    )

    db_session.add(blogger)
    db_session.commit()
    db_session.refresh(blogger)

    found_blogger = service.find_blogger_by_email("colly@gmail.com")

    assert found_blogger is not None
    assert found_blogger.id == blogger.id
    assert found_blogger.username == "collete"
    assert found_blogger.email == "colly@gmail.com"

def test_that_I_return_none_when_email_does_not_exist(db_session):
    service = BloggerService(db_session)

    found_blogger = service.find_blogger_by_email("unknown@gmail.com")

    assert found_blogger is None

def test_that_I_can_find_all_bloggers(db_session):
    service = BloggerService(db_session)

    blogger1 = Blogger(
        username="colly",
        email="colly@gmail.com",
        password="wes123"
    )

    blogger2 = Blogger(
        username="john",
        email="john@gmail.com",
        password="abc123"
    )

    db_session.add(blogger1)
    db_session.add(blogger2)
    db_session.commit()

    bloggers = service.find_all_bloggers()

    assert len(bloggers) == 2
    assert bloggers[0].username == "colly"
    assert bloggers[1].username == "john"

def test_that_I_can_update_a_blogger(db_session):
    service = BloggerService(db_session)

    blogger = Blogger(
        username="colly",
        email="colly@gmail.com",
        password="wes123"
    )

    db_session.add(blogger)
    db_session.commit()
    db_session.refresh(blogger)

    blogger.username = "collete"
    blogger.email = "collete@gmail.com"

    updated_blogger = service.update_blogger(blogger)

    assert updated_blogger.username == "collete"
    assert updated_blogger.email == "collete@gmail.com"