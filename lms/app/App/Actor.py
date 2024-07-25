from functools import wraps
from flask import g as GlobalVars, request as HttpRequest, redirect as RouteRedirect, session as UserSession

class BaseActor():
    session_key = ""
    route_url = "/"

    def uid(self):
        if self.is_logged_in():
            return UserSession[self.session_key]
        return "err"

    def set_session(self, session, g):
        GlobalVars.user = 0
        if self.is_logged_in():
            GlobalVars.user = session[self.session_key]

    def is_logged_in(self):
        if self.session_key in UserSession and UserSession[self.session_key] and UserSession[self.session_key] > 0:
            return True
        return False

    def login_required(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not self.is_logged_in():
                return RouteRedirect(self.route_url)
            return f(*args, **kwargs)
        return decorated_function

    def redirect_if_login(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if self.is_logged_in():
                return RouteRedirect(self.route_url)
            return f(*args, **kwargs)
        return decorated_function

