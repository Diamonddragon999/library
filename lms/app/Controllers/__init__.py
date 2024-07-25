from App import Admin, Books, User
from flask import current_app
class AdminManager():
  def __init__(self, DAO):
    self.admin = Admin(DAO.db.admin)
    self.user = DAO.db.user
    self.dao = self.admin.dao

  def signin(self, email, password):
    admin = self.dao.getByEmail(email)

    if admin is None:
      return False
    if "password" not in admin:
      return False
    admin_pass = admin["password"] # admin pass at 
    if admin_pass != password:
      return False

    return admin
    
  def get(self, id):
    admin = self.dao.getById(id)

    return admin
    
  def getUsersList(self):
    admin = self.user.list()

    return admin

  def signout(self):
    self.admin.signout()
  
  def signup(self, email, password):
    admin = self.dao.getByEmail(email)

    if admin is not None:
      return "already_exists"

    admin_info = {"email": email, "password": password}
    
    admin_user = self.dao.add(admin_info)

    return admin_user

  def user_list(self):
    return self.user.list()

class UserManager():
  def __init__(self, DAO):
    self.user = User(DAO.db.user)
    self.book = DAO.db.book
    self.dao = self.user.dao

  def list(self):
    user_list = self.dao.list()

    return user_list

  def signin(self, email, password):
    user = self.dao.getByEmail(email)

    if user is None:
      return False

    user_pass = user['password'] # user pass at 
    if user_pass != password:
      return False

    return user

  def signout(self):
    self.user.signout()
    
  def get(self, id):
    user = self.dao.getById(id)

    return user

  def signup(self, name, email, password):
    user = self.dao.getByEmail(email)

    if user is not None:
      return "already_exists"

    user_info = {"name": name, "email": email, "password": password}
    
    new_user = self.dao.add(user_info)

    return new_user
    
  def get(self, id):
    user = self.dao.getById(id)

    return user

  def delete(self, id):
    self.dao.delete(id)

  def update(self, name, email, password, bio, id):
    user_info = {"name": name, "email": email, "password": password, "bio":bio}
    current_app.logger.info(user_info)
    user = self.dao.update(user_info, id)

    return user

  def getBooksList(self, id):
    return self.book.getBooksByUser(id)

  def getUsersByBook(self, book_id):
    return self.dao.getUsersByBook(book_id)	

class BookManager():
  def __init__(self, DAO):
    self.misc = Books(DAO.db.book)
    self.dao = self.misc.dao

  def list(self, availability=1,user_id=None):
    if user_id!= None:
      book_list = self.dao.listByUser(user_id)
    else:
      book_list = self.dao.list(availability)

    return book_list

  def getReserverdBooksByUser(self, user_id):
    books = self.dao.getReserverdBooksByUser(user_id)
    return books

  def getBook(self, id):
    books = self.dao.getBook(id)

    return books

  def search(self, keyword, availability=1):
    books = self.dao.search_book(keyword, availability)

    return books

  def reserve(self, user_id, book_id):
    books = self.dao.reserve(user_id, book_id)

    return books

  def getUserBooks(self, user_id):
    books = self.dao.getBooksByUser(user_id)

    return books

  def getUserBooksCount(self, user_id):
    books = self.dao.getBooksCountByUser(user_id)

    return books
  def add(self, book):
    self.dao.add(book)
  def update(self, id, book):
    current_app.logger.info(f"{self.dao.__class__}")
    current_app.logger.info(f"{dir(self.dao)}")
    self.dao.update(id, book)

  def delete(self, id):
    self.dao.delete(id)