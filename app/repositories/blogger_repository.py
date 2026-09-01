from app.models.blogger import Blogger
from sqlmodel import select


class BloggerRepository:

    def __init__(self, session):
        self.session = session

    def save(self, blogger):
        self.session.add(blogger)
        self.session.commit()
        self.session.refresh(blogger)

        return blogger

    def find_by_id(self, blogger_id):
        return self.session.get(Blogger, blogger_id)

    def find_by_username(self, username):
        statement = select(Blogger).where(Blogger.username == username)
        return self.session.exec(statement).first()

    def find_by_email(self, email):
        statement = select(Blogger).where(Blogger.email == email)
        return self.session.exec(statement).first()

    def find_all(self):
        statement = select(Blogger)
        return self.session.exec(statement).all()

    def update(self, blogger):
        self.session.add(blogger)
        self.session.commit()
        self.session.refresh(blogger)

        return blogger