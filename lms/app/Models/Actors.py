from flask import current_app
class AdminDAO():
  db = {}
  
  def __init__(self, DAO):
    self.db = DAO
    self.db.table = "admin"

  def getById(self, id):
    q = self.db.query("select * from @table where id='{}'".format(id))
    user = q.fetchone()
    q.close()
    return user

  def getByEmail(self, email):
    q = self.db.query("select * from @table where email LIKE '{}'".format(email))
    user = q.fetchone()
    q.close()
    return user
  
  def add(self, user):
    email = user['email']
    password = user['password']
    q = self.db.query("INSERT INTO @table (id, email, password) VALUES (0, '{}', '{}');".format( email, password))
    q.close()
    return q

class UserDAO():
  def __init__(self, DAO):
    self.db = DAO
    self.db.table = "users"


  def list(self):
    q = self.db.query("SELECT @table.id,@table.name,@table.email,@table.bio,@table.mob,@table.lock,@table.created_at,COALESCE(book_count.books_owned, 0) AS books_owned FROM @table LEFT JOIN (SELECT user_id, COUNT(book_id) AS books_owned FROM reserve GROUP BY user_id) AS book_count ON @table.id = book_count.user_id")
    users= q.fetchall()
    q.close()
    return users

  def getById(self, id):
    q = self.db.query("select * from @table where id='{}'".format(id))

    user = q.fetchone()
    q.close()
    return user
  
  def delete(self, id):
    q = self.db.query("DELETE FROM @table where id={}".format(id))
    q.close()
    return q
  
  def getUsersByBook(self, book_id):
    q = self.db.query("select * from @table LEFT JOIN reserve ON reserve.user_id = @table.id WHERE reserve.book_id={}".format(book_id))

    user = q.fetchall()
    q.close()

    return user

  def getByEmail(self, email):
    q = self.db.query("select * from @table where email='{}'".format(email))
    user = q.fetchone()
    q.close()
    return user

  def add(self, user):
    name = user['name']
    email = user['email']
    password = user['password']
    q = self.db.query("INSERT INTO @table (name, email, password) VALUES('{}', '{}', '{}');".format(name, email, password))
    q.close()
    return q


  def update(self, user, _id):
    name = user['name']
    email = user['email']
    password = user['password']
    bio = user['bio']

    q = self.db.query("UPDATE @table SET name = '{}', email='{}', password='{}', bio='{}' WHERE id={}".format(name, email, password, bio, _id))
    q.close()
    
    return q