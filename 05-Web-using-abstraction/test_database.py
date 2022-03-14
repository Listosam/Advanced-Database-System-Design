# tests for database abstraction layer
import database

def test_shopping_list():
    shopping_list = database.get_shopping_list()
    assert type(shopping_list) is list
    assert len(shopping_list) > 0, "The shopping list has no items in it"
    for item in shopping_list:
        assert type(item) is dict
        assert "id" in item
        assert "desc" in item

import string, random

def test_add_item():
    new_item = ''.join(random.choices(string.ascii_letters,k=14))
    shopping_list = database.get_shopping_list()
    for item in shopping_list:
        assert item['desc'] != new_item
    database.add_item(new_item)
    shopping_list = database.get_shopping_list()
    for item in shopping_list:
        if item['desc'] == new_item:
            # clean_up
            return 
    assert False, "The item was not apparently added to shopping list"

def test_delete_item():
    new_item = ''.join(random.choices(string.ascii_letters,k=14))
    database.add_item(new_item)
    shopping_list = database.get_shopping_list()
    id = None
    
    for item in shopping_list:
        if item['desc'] == new_item:
            id = item['id']
            #clean up
            return
    assert id != None, "id of new item not found"
    database.delete_item(id)

    shopping_list = database.get_shopping_list()
    for item in shopping_list:
        assert item['id'] != id, "id of deleted item still found in database"
        assert item['desc'] != new_item, "deleted item still found in database"


def test_update_item():
    new_item = ''.join(random.choices(string.ascii_letters,k=14))
    database.add_item(new_item)
    shopping_list = database.get_shopping_list()
    id = None
    
    for item in shopping_list:
        if item['desc'] == new_item:
            id = item['id']
            #clean up
            return
    assert id != None, "id of new item not found"

    new_name = ''.join(random.choices(string.ascii_letters,k=14))
    database.update_item(id, new_name)
    update_item(id, description)

    shopping_list = database.get_shopping_list()
    for item in shopping_list:
        if item['id'] == id:
            assert item['id'] == new_name, "id was not updated with new_name"
    


if __name__ == "__main__":
    test_get_shopping_list()

