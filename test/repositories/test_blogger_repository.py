# import pytest
#
# from models.blogger import Blogger
# from models.user_role import Role
# from sqlmodel import SQLModel, Session, create_engine
#
#
# engine = create_engine(
#     "sqlite://",
#     connect_args={"check_same_thread": False},
# )
#
#
# class TestBloggerRepository:
#
#     @pytest.fixture
#     def session(self):
#         SQLModel.metadata.create_all(engine)
#
#         with Session(engine) as session:
#             yield session
#
#         SQLModel.metadata.drop_all(engine)
#
#     def test_create_blogger(self, session):
#
#         blogger = Blogger(
#             username="colly",
#             email="colly@gmail.com",
#             password="meg123",
#         )
#
#         assert blogger.username == "colly"
#         assert blogger.email == "colly@gmail.com"
#         assert blogger.password == "meg123"
#         assert blogger.role == Role.BLOGGER
import pytest

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
