#Exercise 1
#Question 1
cheese = ["Cheddar","Stilton","Cornish Yarg"]
# cheese += "Oke"
#Q. What is wrong with this?
#Guess: There is no position for the "oke" to be added. It needs a position in order to be placed in the list.
#Answer: The += operator would create a new list. Concatenating a mutable list creates a new list.
#However, appending to a list modifies the existing list.

#Guess: To add new cheese to the list with a single command you would append them to the list and use a comma in between each listed item.
#Answer: You must use the Extend method to add multiple items to the list. This must be in square brackets in the method.
cheese.extend(["Oke", "Red Leicester"])
print(cheese)

#Question 2
tup = "Hello"
print(len(tup))

tup = "Hello",
print(len(tup))
#Q: What is going on here? can you explain the output?
#Answer: The initial tup variable has stored the string Hello which has five letters. The length function in this case checks the
# number of characters there is within the string which is 5. In the second tup variable the same string Hello is stated however
# a comma proceeds it, which therefore turns the string into a tuple data type. the length function then checks the number
# of elements in the tuple there is, which in this case iis one.


