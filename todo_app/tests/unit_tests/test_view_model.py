

from todo_app.classes import Item
from todo_app.enums import Status
from todo_app.models import ViewModel


def test_view_model_complete_property():
    # Arrange
    incomplete_item = Item(id='INCOMPLETE', name="Incomplete task", status=Status.INCOMPLETE)
    complete_item = Item(id='COMPLETE', name="Complete task", status=Status.COMPLETE)

    view_model = ViewModel(items=[incomplete_item, complete_item])

    # Act
    complete_items = view_model.complete_items

    # Assert
    assert complete_items == [complete_item]

def test_view_model_incomplete_property():
    # Arrange
    incomplete_item = Item(id='INCOMPLETE', name="Incomplete task", status=Status.INCOMPLETE)
    complete_item = Item(id='COMPLETE', name="Complete task", status=Status.COMPLETE)

    view_model = ViewModel(items=[incomplete_item, complete_item])

    # Act
    incomplete_items = view_model.incomplete_items

    # Assert
    assert incomplete_items == [incomplete_item]