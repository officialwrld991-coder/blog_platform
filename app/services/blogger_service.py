from app.models.blogger import Blogger
from app.repositories.blogger_repository import BloggerRepository


class BloggerService:

    def __init__(self, session):
        self.repository = BloggerRepository(session)

    def create_blogger(self, blogger_data):
        blogger = Blogger(
            username=blogger_data.username,
            email=blogger_data.email,
            password=blogger_data.password
        )

        return self.repository.save(blogger)

    def find_blogger_by_id(self, blogger_id):
        return self.repository.find_by_id(blogger_id)

    def find_blogger_by_username(self, username):
        return self.repository.find_by_username(username)

    def find_blogger_by_email(self, email):
        return self.repository.find_by_email(email)

    def find_all_bloggers(self):
        return self.repository.find_all()

    def update_blogger(self, blogger):
        return self.repository.update(blogger)