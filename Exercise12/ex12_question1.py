# create new list called cheese
cheese = ['cheddar', 'stilton', 'cornish yarg']
print(cheese)

# add a new list item
# cheese += 'oke'
    # problem with this is that 'oke' is iterable (a string) and adds each character
    # would not work as it does not have the square brackets
# this would be the correct format to add a new list item
# to add two items, you would separate each of them by a comma and place them in individual quotes.
cheese += ['oke','mozzarella']
print(cheese)