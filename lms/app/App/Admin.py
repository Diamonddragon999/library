from App.Actor import BaseActor

class AdminEntity(BaseActor):
    admin_data = {}
    
    def __init__(self, AdminDAO):
        self.session_key = "admin"
        self.data_access = AdminDAO
        self.route_url = "/admin/"

    def set_session(self, session, g):
        g.admin = session.get(self.session_key)
        if g.admin:
            self.admin_data = self.data_access.get_by_id(g.admin)
            g.admin_data = self.admin_data
        else:
            g.admin_data = None

    def signout(self):
        self.admin_data = {}
        self.session_key = None

    def get_by_email(self, email):
        return self.data_access.get_by_email(email)

    def get_by_id(self, admin_id):
        return self.data_access.get_by_id(admin_id)

    def update(self, name, email, password, bio, admin_id):
        self.data_access.update_admin(name, email, password, bio, admin_id)
