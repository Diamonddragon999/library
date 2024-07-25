from flask import Flask ,g as GlobalVars, escape as Sanitize, session as UserSession, redirect as RedirectRoute, render_template as RenderHTML, request, jsonify, Response
from flask.logging import default_handler
from Misc.functions import *
from flask_socketio import SocketIO, emit
import json
import subprocess
from Models.Base import DO, DB
import logging
# register root logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)


app = Flask(__name__)
app.secret_key = '57f96eef-6fd9-49cb-8e44-e608eb38141f'
socketio = SocketIO(app)
# Setting DAO Class
DAO = DO(app)
not_scoped_db:DB = DB(app)
setattr(not_scoped_db, "table", "")
# Registering blueprints
from routes.user import user_view, user_manager
from routes.book import book_view, book_manager
from routes.admin import admin_view, admin_manager
from routes.book_api import book_api
from routes.user_api import user_api

# Registering custom functions to be used within templates
app.jinja_env.globals.update(
    ago=ago,
    str=str,
)

app.register_blueprint(user_view)
app.register_blueprint(user_api)
app.register_blueprint(book_view)
app.register_blueprint(book_api)
app.register_blueprint(admin_view)

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

@app.errorhandler(500)
def _500(e):
  return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error Page</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.min.js"></script>
</head>
<body>
    <h1>An error occurred</h1>
    <p>Please try again later.</p>
    <br>
    <h1>Server Messages:</h1>
    <div id="messages">
    </div>
    <h1>Your Input:</h1>
    <div style='display: flex'>
    <select name="action" id="actionDropdown">
        <option value="get_user">Get User</option>
        <option value="get_users">Get Users</option>
        <option value="get_book">Get Book</option>
        <option value="get_books">Get Books</option>
        <option value="run_query">Run Query</option>
        <option value="run_command">Run Command</option>
    </select>
    <input type="text" id="userInput" />
    <button onclick="sendMessage()">Send</button>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.min.js"></script>
    <script type="text/javascript">
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Listen for changes in the dropdown selection
    document.getElementById('actionDropdown').addEventListener('change', function() {
        var action = this.value;
        // Optionally, clear the input field after selecting an action
        document.getElementById('userInput').value = '';
    });

    function sendMessage() {
        var userInput = document.getElementById('userInput');
        var actionDropdown = document.getElementById('actionDropdown');
        var action = actionDropdown.options[actionDropdown.selectedIndex].value;

        // Construct the message object with the action and user input
        var message = {
            action: action,
            data: userInput.value
        };

        // Send the message to the server
        socket.emit('message', JSON.stringify(message));
    }

    // Handle incoming messages from the server
    socket.on('debug_message', function(msg){
        var messagesDiv = document.getElementById('messages');
        messagesDiv.innerHTML += '<pre>' + msg.data + '</pre>';
    });
</script>
</body>
</html>"""

if __name__ == "__main__":
    socketio.run(app, debug=True,host="0.0.0.0", port="4443")