from App.Actor import BaseActor

class UserEntity(BaseActor):
    id = 0
    name = ""
    lock = False

    user_data = {}

    def __init__(self, UserDAO):
        super().__init__(UserDAO)
        self.data_access = UserDAO
        self.session_key = "user"  # session key

    def set_session(self, session, g):
        g.user = session.get(self.session_key)
        if g.user:
            self.user_data = self.data_access.get_by_id(g.user)
            g.user_data = self.user_data
        else:
            g.user_data = None

    def signout(self):
        self.user_data = {}
        self.session_key = None

    def get_by_email(self, email):
        return self.data_access.get_by_email(email)

    def get_by_id(self, user_id):
        return self.data_access.get_by_id(user_id)

    def update(self, name, email, password, bio, user_id):
        self.data_access.update_user(name, email, password, bio, user_id)
