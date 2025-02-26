# Functions for adding and removing inventory items

def add_to_inventory(item, quantity=1):
    if item in current_character["inventory"]:
        current_character["inventory"][item] += quantity
    else:
        current_character["inventory"][item] = quantity

def remove_from_inventory(item, quantity=1):
    if item in current_character["inventory"]:
        current_character["inventory"][item] -= quantity
        if current_character["inventory"][item] <= 0:
            del current_character["inventory"][item]