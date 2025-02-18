# QUESTION1
# Make a list of cheeses
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese)

# This is wrong because it adds each letter of 'Oke' as a separate item
# Result would be: ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']
# would not work as it does not have the square brackets

# cheese += 'Oke'

# alt method
# cheese += ['oke','mozzarella']
# print(cheese)

# The correct way to add 'Oke' as one item at the end
# .append method adds a single item to the end of an existing list
cheese.append('Oke')
print(cheese)

# To add two cheeses at once, use extend() like this:
# .extend method still only adds one argument to the end of an existing list
# adding the square brackets allows for it to add multiple arguments to the end of an existing list
cheese.extend(['Brie', 'Gouda'])
print(cheese)