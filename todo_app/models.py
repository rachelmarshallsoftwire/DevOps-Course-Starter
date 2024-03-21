from pytest import Item

from todo_app.enums import Status


class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def incomplete_items(self):
        incomplete_items: list[Item] = []
        for item in self._items:
            if item.status == Status.INCOMPLETE:
                incomplete_items.append(item)
        return incomplete_items
    
    @property
    def complete_items(self):
        complete_items: list[Item] = []
        for item in self._items:
            if item.status == Status.COMPLETE:
                complete_items.append(item)
        return complete_items