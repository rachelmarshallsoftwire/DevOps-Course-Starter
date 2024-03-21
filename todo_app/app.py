from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import get_items, add_item, move_to_complete_column
from todo_app.enums import Status

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods = ['GET'])
def index():
    items = get_items()
    return render_template('index.html', items = items, incomplete=Status.INCOMPLETE)

@app.route('/', methods = ['POST'])
def add_new_item():
    item = request.form['item']
    add_item(item)
    return redirect('/')

@app.route('/complete/<item_id>', methods=['POST'])
def complete_item(item_id):
    move_to_complete_column(item_id)
    return redirect('/')