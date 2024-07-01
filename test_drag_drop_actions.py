""""
Test drag and drop action chain inside a iframe
"""


from drag_drop_actions import Droppable
import pytest


url="https://jqueryui.com/droppable/"
droppable=Droppable(url)

def test_get_url():
    assert droppable.get_url() == True
    print("Success: Automation of webpage has started")


def test_iframe():
    assert droppable.iframe() == True
    print("Success")


def test_drag_drop():
    assert  droppable.drag_drop() == None
    print("Success:Drag and Drop has performed")


