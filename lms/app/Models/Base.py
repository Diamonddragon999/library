from Models.Actors import UserDAO, AdminDAO
from Models.Books import BookDAO
import MySQLdb
from MySQLdb.cursors import DictCursor
from copy import copy

class DB(object):
  """Initialize mysql database """
  db_host = "database"
  db_user = "lms_user"
  db_port = 3306
  db_password = "password"
  db_database = "lms_main_database"

  def __init__(self, app):
    pass

  def cur(self):
    self.mysql = MySQLdb.connect(host=self.db_host, port=self.db_port,password=self.db_password, user=self.db_user, database=self.db_database, cursorclass=DictCursor)
    return self.mysql.cursor()

  def query(self, q) -> DictCursor:
    h = self.cur()
    if (len(self.table)>0):
      q = q.replace("@table", self.table)
    h.execute(q)
    res = copy(h)
    h.execute("COMMIT;")
    return res

  def commit(self):
    q = self.query("COMMIT;")
    q.close()

class DBDAO(DB):
  def __init__(self, app):
    super().__init__(app)

    self.book = BookDAO(copy(self))
    self.user = UserDAO(copy(self))
    self.admin = AdminDAO(copy(self))


class DO:
  def __init__(self, app):
    self.db = DBDAO(app)