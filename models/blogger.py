import uuid
from user import User
from user_role import Role
from datetime import datetime
from post import Post

class Blogger(User):
    def __init__(self, fullName, userName, bio, password):
        super().__init__(fullName, userName, bio, password, Role.BLOGGER)
        self.bio = bio
        self.posts = []

    def showProfile(self):
        return f"[BLOGGER] {self.userName} | Total Post {len(self.posts)}"

    def createPost(self, title, content):
        new_post = Post(post_id=str(uuid.uuid4()), title=title, content=content)

    def deletePost(self, post):
        if post in self.posts:
            self.posts.remove(post)
            return  True
        return False