from user import User
from user_role import Role
from comment import Comment
#from post import Post

class Guest(User):
    def __init__(self, fullName: str, userName: str, password: str):
        super().__init__(fullName, userName, password, Role.GUEST)

    def show_profile(self):
        return f"[GUEST] {self.userName}"

    def comment_on_post(self, post, content: str, author):
        new_comment = Comment(post=post, content=content, author=author)
        post.add_comments(new_comment)
        return new_comment
    