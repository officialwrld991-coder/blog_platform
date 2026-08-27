import uuid

from comment import Comment
from blogger import Blogger
from datetime import datetime

class Post():
    def __init__(self, title: str, content: str, author: Blogger):
        self.title = title
        self.post_id = str(uuid.uuid4())
        self.content = content
        self.author = author
        self.comments = []
        self.created_at = datetime.now()
        self.is_published = False

    def publish(self):
        self.is_published = True

    def add_comments(self, comments: Comment):
        self.comments.append(comments)
