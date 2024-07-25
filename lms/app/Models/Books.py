from flask import current_app
class BookDAO():
  def __init__(self, DAO):
    self.db = DAO
    self.db.table = "books"
  def update(self, id, book: dict):
    query = "UPDATE @table SET "+", ".join([f"{key}='{value}'" if type(value) != bool else f"{key}='{int(value)}'" for key,value in book.items() if key != "id"])+f" where id={id}"
    current_app.logger.info(query)
    q = self.db.query(query)
    current_app.logger.info(q)
    q.close()
    return q

  def add(self, book:dict):
    query = f"INSERT INTO `books` (`name`, `description`, `author`, `availability`, `edition`, `count`) VALUES ("+f"'{book['name']}', '{book['description']}', '{book['author']}', {book['availability']}, '{book['edition']}', {book['count']}"+")"
    current_app.logger.info(query)
    q = self.db.query(query)
    current_app.logger.info(q)
    q.close()
    return q

  def delete(self, id):
    q = self.db.query("DELETE FROM @table where id={}".format(id))
    q.close()

    return q

  def reserve(self, user_id, book_id):
    if not self.available(book_id):
      return "err_out"

    q = self.db.query("INSERT INTO reserve (user_id, book_id) VALUES('{}', '{}');".format(user_id, book_id))
    
    self.db.query("UPDATE @table set count=count-1 where id={};".format(book_id))
    q.close()
    return q

  def getBooksByUser(self, user_id):
    q = self.db.query("select * from @table left join reserve on reserve.book_id = @table.id where reserve.user_id={}".format(user_id))

    books = q.fetchall()
    q.close()
    return books

  def getBooksCountByUser(self, user_id):
    q = self.db.query("select count(reserve.book_id) as books_count from @table left join reserve on reserve.book_id = @table.id where reserve.user_id={}".format(user_id))

    books = q.fetchall()
    q.close()
    return books

  def getBook(self, id):
    q = self.db.query("select * from @table where id={}".format(id))

    book = q.fetchone()
    q.close()
    return book

  def available(self, id):
    book = self.getById(id)
    count = book['count']

    if count < 1:
      return False

    return True

  def getById(self, id):
    q = self.db.query("select * from @table where id='{}'".format(id))
    book = q.fetchone()
    q.close()
    return book

  def list(self, availability=1):
    query="select * from @table"
    # Usually when no-admin user query for book
    if availability==1: query= query+"  WHERE availability={}".format(availability)
    
    q = self.db.query(query)
    
    books = q.fetchall()
    q.close()


    return books

  def getReserverdBooksByUser(self, user_id):
    query="select concat(book_id,',') as user_books from reserve WHERE user_id={}".format(user_id)
    
    q = self.db.query(query)
    
    books = q.fetchone()
    q.close()


    return books

  def search_book(self, name, availability=1):
    query="select * from @table where name LIKE '%{}%'".format(name)

    # Usually when no-admin user query for book
    if availability==1: query= query+" AND availability={}".format(availability)

    q = self.db.query(query)
    books = q.fetchall()
    q.close()

    return books