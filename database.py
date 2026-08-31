# from sqlmodel import SQLModel, create_engine, Session
#
# # Clean database setup using local SQLite file mapping
# DATABASE_URL = "sqlite:///blog_platform.db"
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
#
#
# # Function required by main.py to create your blog tables
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)
#
#
# # Session helper function
# def get_session():
#     with Session(engine) as session:
#         yield session

from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///blog.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
