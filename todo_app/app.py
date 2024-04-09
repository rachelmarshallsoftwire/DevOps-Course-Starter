from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import TrelloService
from todo_app.enums import Status

from todo_app.flask_config import Config
from todo_app.models import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    trello_service = TrelloService()

    @app.route('/', methods = ['GET'])
    def index():
        items = trello_service.get_items()
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model, incomplete=Status.INCOMPLETE)

    @app.route('/', methods = ['POST'])
    def add_new_item():
        item = request.form['item']
        trello_service.add_item(item)
        return redirect('/')

    @app.route('/complete/<item_id>', methods=['POST'])
    def complete_item(item_id):
        trello_service.move_to_complete_column(item_id)
        return redirect('/')
    
    return app

app = create_app()
