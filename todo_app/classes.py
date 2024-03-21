from todo_app.enums import List_Ids, Status

def map_column_id_to_status(column_id: str):
    match column_id:
        case List_Ids.TO_DO_LIST.value:
            return Status.INCOMPLETE
        case List_Ids.DONE_LIST.value:
            return Status.COMPLETE
        case _:
            return None

class Item:
    def __init__(self, id, name, status = Status.INCOMPLETE):
        self.id = id
        self.name = name
        self.status = status
    
    @classmethod
    def from_trello_card(cls, card):
        return cls(card['id'], card['name'], map_column_id_to_status(card['idList']))