import pytest

from sqlmodel import SQLModel, Session, create_engine


@pytest.fixture
def db_session():
    engine = create_engine(
        "sqlite://", connect_args=
        {"check_same_thread": False}
                           )

    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

        SQLModel.metadata.drop_all(engine)