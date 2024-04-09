import os
from todo_app.enums import Status

def map_column_id_to_status(column_id: str):
    if column_id == os.getenv('TO_DO_LIST_ID'):
        return Status.INCOMPLETE
    if column_id == os.getenv('DONE_LIST_ID'):
        return Status.COMPLETE
    return None

class Item:
    def __init__(self, id, name, status = Status.INCOMPLETE):
        self.id = id
        self.name = name
        self.status = status
    
    @classmethod
    def from_trello_card(cls, card):
        return cls(card['id'], card['name'], map_column_id_to_status(card['idList']))