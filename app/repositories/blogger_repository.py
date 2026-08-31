
class BloggerRepository:

    def __init__(self, session):
        self.session = session

    def save(self, blogger):
        self.session.add(blogger)
        self.session.commit()
        self.session.refresh(blogger)

        return blogger