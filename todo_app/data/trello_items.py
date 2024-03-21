import requests
import os

from todo_app.classes import Item

TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_API_TOKEN = os.getenv('TRELLO_API_TOKEN')
TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')
TO_DO_LIST_ID = os.getenv('TO_DO_LIST_ID')
DONE_LIST_ID = os.getenv('DONE_LIST_ID')

def get_items():
    get_items_url = f'https://api.trello.com/1/boards/{TRELLO_BOARD_ID}/lists?cards=open&key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}'

    response = requests.request("GET", get_items_url)
    cards = []
    for list in response.json():
        cards = cards + [Item.from_trello_card(card) for card in list['cards']]
    return cards

def add_item(title):
    post_item_url = f'https://api.trello.com/1/cards?idList={TO_DO_LIST_ID}&key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}'
    requests.request("POST", post_item_url, params={'name': title})

def move_to_complete_column(id):
    save_item_url = f'https://api.trello.com/1/cards/{id}?key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}'
    requests.request("PUT", save_item_url, params={'idList': DONE_LIST_ID})
