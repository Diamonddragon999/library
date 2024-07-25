from flask import Blueprint,current_app,  g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO
from Misc.functions import *
from Controllers import AdminManager, BookManager, UserManager

admin_view = Blueprint('admin_routes', __name__, template_folder='../templates/admin/', url_prefix='/admin')

book_manager = BookManager(DAO)
user_manager = UserManager(DAO)
admin_manager = AdminManager(DAO)


@admin_view.route('/', methods=['GET'])
@admin_manager.admin.login_required
def home():
  admin_manager.admin.set_session(session, g)

  return render_template('admin/home.html', g=g)


@admin_view.route('/signin/', methods=['GET', 'POST'])
@admin_manager.admin.redirect_if_login
def signin():
  g.bg = 1  
  
  if request.method == 'POST':
    _form = request.form
    email = str(_form["email"])
    password = str(_form["password"])

    if len(email)<1 or len(password)<1:
      return render_template('admin/signin.html', error="Email and password are required")

    d = admin_manager.signin(email, hash(password))

    if d and len(d)>0:
      session['admin'] = int(d["id"])

      return redirect("/admin")

    return render_template('admin/signin.html', error="Email or password incorrect")

  return render_template('admin/signin.html')

@admin_view.route('/signup', methods=['GET', 'POST'])
@admin_manager.admin.redirect_if_login
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    if len(email)<1 or len(password)<1:
      return render_template('admin/signup.html', error="All fields are required")

    new_user = admin_manager.signup(email, hash(password))
    if new_user == "already_exists":
      return render_template('admin/signup.html', error="User already exists with this email")


    return render_template('admin/signup.html', msg = "You've been registered!")


  return render_template('admin/signup.html')

@admin_view.route('/signout/', methods=['GET'])
@admin_manager.admin.login_required
def signout():
  admin_manager.signout()

  return redirect("/admin/", code=302)


@admin_view.route('/books/', methods=['GET'])
@admin_manager.admin.login_required
def books():
  admin_manager.admin.set_session(session, g)

  id = int(admin_manager.admin.uid())
  admin = admin_manager.get(id)
  mybooks = book_manager.list(availability=0)

  return render_template('admin/books/views.html', g=g, books=mybooks, admin=admin)

@admin_view.route('/books/<int:id>')
@admin_manager.admin.login_required
def view_book(id):
  admin_manager.admin.set_session(session, g)

  if id != None:
    b = book_manager.getBook(id)
    users = user_manager.getUsersByBook(id)
    if b and len(b) <1:
      return render_template('admin/books/book_view.html', error="No book found!")
    return render_template("admin/books/book_view.html", books=b, books_owners=users, g=g)


@admin_view.route('/books/add', methods=['GET', 'POST'])
@admin_manager.admin.login_required
def book_add():
  admin_manager.admin.set_session(session, g)
  if request.method == 'POST':
    _form = request.form
    current_app.logger.info(f"{request.form}")
    name = str(_form["title"])
    current_app.logger.info("title")
    desc = str(_form["description"])
    current_app.logger.info("description")
    available = bool(_form["available"])
    current_app.logger.info("available")
    author = str(_form["author"])
    current_app.logger.info("author")
    edition = str(_form["edition"])
    current_app.logger.info("edition")
    count = int(_form["qty"])
    current_app.logger.info("qty")
    book = {
      "name": name,
      "description": desc,
      "availability": available,
      "author": author,
      "edition": edition,
      "count": count
    }
    current_app.logger.info(f"{book}")
    book_manager.add(book)
    return redirect("/admin/books")
  return render_template('admin/books/add.html', g=g)


@admin_view.route('/books/edit/<int:id>', methods=['GET', 'POST'])
@admin_manager.admin.login_required
def book_edit(id):
  admin_manager.admin.set_session(session, g)
  b = book_manager.getBook(id)
  current_app.logger.info(f"{b}")
  if b and len(b) <1:
    return render_template('admin/books/edit.html', error="No book found!")
  current_app.logger.info("My log")
  current_app.logger.info(f"{id}::::{request.method}")
  if request.method == 'POST':
    _form = request.form
    current_app.logger.info(f"{request.form}")
    name = str(_form["title"])
    current_app.logger.info("title")
    desc = str(_form["description"])
    current_app.logger.info("description")
    available = int(_form["available"])
    current_app.logger.info("available")
    author = str(_form["author"])
    current_app.logger.info("author")
    edition = str(_form["edition"])
    current_app.logger.info("edition")
    count = int(_form["qty"])
    current_app.logger.info("qty")
    book = {
      "id": id,
      "name": name,
      "description": desc,
      "availability": available,
      "author": author,
      "edition": edition,
      "count": count
    }
    current_app.logger.info(f"{book}")
    book_manager.update(id,book)

    return render_template("admin/books/edit.html", book=b, g=g)
  else:
    return render_template("admin/books/edit.html", book=b, g=g)
  # return redirect('/books')

@admin_view.route('/books/delete/<int:id>', methods=['GET'])
@admin_manager.admin.login_required
def book_delete(id):
  id = int(id)

  if id is not None:
    book_manager.delete(id)
  
  return redirect('/admin/books/')


@admin_view.route('/books/search', methods=['GET'])
def search():
  admin_manager.admin.set_session(session, g)

  if "keyword" not in request.args:
    return render_template("admin/books/view.html")

  keyword = request.args["keyword"]

  if len(keyword)<1:
    return redirect('/admin/books')

  id = admin_manager.admin.uid()
  if id == "err":
    return redirect("/admin/signin")

  admin = admin_manager.get(id)

  d=book_manager.search(keyword, 0)
  current_app.logger.info(d)
  if len(d) >0:
    return render_template("admin/books/views.html", search=True, books=d, count=len(d), keyword=escape(keyword), g=g, admin=admin)

  return render_template('admin/books/views.html', error="No books found!", keyword=escape(keyword))

@admin_view.route('/users', methods=['GET'])
@admin_manager.admin.login_required
def users_view():
  admin_manager.admin.set_session(session, g)

  id = int(admin_manager.admin.uid())
  admin = admin_manager.get(id)
  myusers = admin_manager.getUsersList()

  return render_template('admin/users.html', g=g, admin=admin, users=myusers)

@admin_view.route('/users/add', methods=['GET', 'POST'])
@admin_manager.admin.login_required
def user_add():
  admin_manager.admin.set_session(session, g)
  if request.method == 'POST':
    _form = request.form
    current_app.logger.info(f"{request.form}")
    name = str(_form["name"])
    current_app.logger.info("name")
    desc = str(_form["description"])
    current_app.logger.info("description")
    email = str(_form["email"])
    current_app.logger.info("email")
    password = str(_form["password"])
    current_app.logger.info("password")
    som = user_manager.signup(name, email, hash(password))
    if type(som) is not str and som is not None:
      current_app.logger.info(f"{som.__dict__}")
      user_manager.update(name, email, hash(password), desc, som.__dict__["lastrowid"])
    return redirect("/admin/users")
  return render_template('admin/users/add.html', g=g)

@admin_view.route('/users/edit/<id>', methods=['GET', 'POST'])
@admin_manager.admin.login_required
def user_edit(id):
  admin_manager.admin.set_session(session, g)
  if request.method == 'POST':
    _form = request.form
    current_app.logger.info(f"{request.form}")
    name = str(_form["name"])
    current_app.logger.info("name")
    desc = str(_form["description"])
    current_app.logger.info("description")
    email = str(_form["email"])
    current_app.logger.info("email")
    password = str(_form["password"])
    current_app.logger.info("password")
    user_manager.signup(name, email, hash(password))
    user_manager.update(name, email, hash(password), desc)
  user = user_manager.get(id)
  if not user:
    return redirect("/admin/users/add")
  return render_template('admin/users/edit.html', g=g, user=user)

@admin_view.route('/users/delete/<id>', methods=['POST'])
@admin_manager.admin.login_required
def user_delete(id):
  user = user_manager.get(id)
  if user is not None or type(user) == str:
    user_manager.delete(user["id"])
  return redirect("/admin/users")