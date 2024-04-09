import requests
import os

from todo_app.classes import Item

class TrelloService():

    def __init__(self):
        self.TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
        self.TRELLO_API_TOKEN = os.getenv('TRELLO_API_TOKEN')
        self.TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')
        self.TO_DO_LIST_ID = os.getenv('TO_DO_LIST_ID')
        self.DONE_LIST_ID = os.getenv('DONE_LIST_ID')

    def get_items(self):
        get_items_url = f'https://api.trello.com/1/boards/{self.TRELLO_BOARD_ID}/lists?cards=open&key={self.TRELLO_API_KEY}&token={self.TRELLO_API_TOKEN}'

        response = requests.request("GET", get_items_url)
        cards = []
        for list in response.json():
            cards = cards + [Item.from_trello_card(card) for card in list['cards']]
        return cards

    def add_item(self, title):
        post_item_url = f'https://api.trello.com/1/cards?idList={self.TO_DO_LIST_ID}&key={self.TRELLO_API_KEY}&token={self.TRELLO_API_TOKEN}'
        requests.request("POST", post_item_url, params={'name': title})

    def move_to_complete_column(self, id):
        save_item_url = f'https://api.trello.com/1/cards/{id}?key={self.TRELLO_API_KEY}&token={self.TRELLO_API_TOKEN}'
        requests.request("PUT", save_item_url, params={'idList': self.DONE_LIST_ID})
