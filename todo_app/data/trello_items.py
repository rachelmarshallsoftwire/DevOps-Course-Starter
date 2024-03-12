import requests
import os

TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_API_TOKEN = os.getenv('TRELLO_API_TOKEN')
TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')
TO_DO_LIST_ID = os.getenv('TO_DO_LIST_ID')

def get_items():
    reqUrl = f'https://api.trello.com/1/boards/{TRELLO_BOARD_ID}/lists?cards=open&key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}'

    response = requests.request("GET", reqUrl)
    cards = []
    for list in response.json():
        cards = cards + [card['name'] for card in list['cards']]
    return cards

def add_item(title):
    post_item_url = f'https://api.trello.com/1/cards?idList={TO_DO_LIST_ID}&key={TRELLO_API_KEY}&token={TRELLO_API_TOKEN}'
    requests.request("POST", post_item_url, params={'name': title})

