# QUESTION1
# Make a list of cheeses
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

# This is wrong because it adds each letter of 'Oke' as a separate item
# Result would be: ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']
cheese += 'Oke'

# The correct way to add 'Oke' as one item at the end
cheese.append('Oke')

# To add two cheeses at once, use extend() like this:
cheese.extend(['Brie', 'Gouda'])

