from flask import Flask, g as GlobalVars, escape as Sanitize, session as UserSession, redirect as RedirectRoute, render_template as RenderHTML, request, jsonify, Response
from Misc.functions import *
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
import json
import subprocess

from Models.Base import DB
from routes.user import user_view, user_manager
from routes.book import book_view, book_manager
from routes.admin import admin_view, admin_manager

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.secret_key = '1234567890'
    # Setting DAO Class

    app.jinja_env.globals.update(
        ago=ago,
        str=str,
    )

    # Registering blueprints
    app.register_blueprint(user_view)
    app.register_blueprint(book_view)
    app.register_blueprint(admin_view)
    
    db.create_all()
    return app

not_scoped_db = None
def create_socket_app(app):
  global not_scoped_db
  socketio = SocketIO(app)
  not_scoped_db = DB(app)
  setattr(not_scoped_db, "table", "")
  @socketio.on('message')
  def handleMessage(msg):
      message_data = json.loads(msg)
      action = message_data.get('action')
      data = str(message_data.get('data'))
      # Determine the target based on the action
      if action == 'get_user':
          data = data.split(" ")[0]
          if not data.isdecimal():
              emit('debug_message', {'data': f'{action}: Error... Integer value required'})
              return
          data = user_manager.get(data)
          emit('debug_message', {'data': f'{action}: {data}'})
      elif action == 'get_users':
          data = admin_manager.user_list()
          emit('debug_message', {'data': f'{action}: {data}'})
      elif action == 'get_book':
          data = data.split(" ")[0]
          if not data.isdecimal():
              emit('debug_message', {'data': f'{action}: Error... Integer value required'})
              return
          data = book_manager.getBook(data)
          emit('debug_message', {'data': f'{action}: {data}'})
      elif action == 'get_books':
          data = book_manager.list()
          emit('debug_message', {'data': f'{action}: {data}'})
      elif action == 'run_query':
          data = not_scoped_db.query(data).fetchall()
          emit('debug_message', {'data': f'{action}: {data}'})
      elif action == 'run_command':
          r = subprocess.run(data.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          data = {
              "stdout": r.stdout.decode(),
              "stderr": r.stderr.decode()
          }
          emit('debug_message', {'data': f'{action}: {data}'})
      else:
          emit('debug_message', {'data': f'Action not found'})
  return socketio
