from flask import Flask, render_template, request, jsonify
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        items = get_items()
        return render_template('index.html', items = items)
    
    elif request.method == 'POST':
        item = request.form['item']
        add_item(item)
        items = get_items()
        return render_template('index.html', items = items)

    else:
        return jsonify({"message":"error"})
