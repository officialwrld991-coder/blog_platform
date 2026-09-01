from sqlmodel import SQLModel, create_engine, Session
from urllib.parse import quote_plus

engine = create_engine(f"mysql+pymysql://user1:"
                       f"{quote_plus('password')}"
                       f"@localhost:3306/blog_platform")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session