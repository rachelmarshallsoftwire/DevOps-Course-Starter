from flask import Flask, redirect, render_template, request, jsonify
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods = ['GET'])
def index():
    items = get_items()
    return render_template('index.html', items = items)

@app.route('/', methods = ['POST'])
def add_new_item():
    item = request.form['item']
    add_item(item)
    return redirect('/')
