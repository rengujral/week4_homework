# create a tuple (telltale sign = ',')
names_tuple = "Rod", "Jane", "Freddy"

# the try statement lets you test a block of code for errors
try:
    print("############ TRY ################")
    print("The TRY block attempts to run")
    # the f strings allows you to embed the expression inside strings
    print(f"Original Tuple: {names_tuple}")
    # the sorted function allows for better readability and sorts them in alphabetical order
    names_sorted_as_list = sorted(names_tuple)
    print(names_sorted_as_list)
    # .append method adds a single item to the end of an existing list
    names_sorted_as_list.append("Bungle")
    print("Added Bungle:", names_sorted_as_list)
    print("Attempt to manipulate the tuple...")
    # this part of the code does not print as tuples don't support item assignment because they are immutable
    names_tuple[0] = "Zippy"
    print("Is this code reached?")
# the except block lets you handle the error
# FileNotFoundError block doesn't run as the code is not handling files
# print statements in this block are ignored
except FileNotFoundError as error:
    print("############ EXCEPT: FileNotFoundError #########")
    print("The EXCEPT/ CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")
# TypeError block runs as this is tuple error
# print statements in this block run
except TypeError as error:
    print("########## EXCEPT: TypeError ###########")
    print("Oh dear, that is not allowed on that type")
    # this print statement produces the error message of the error found in the try block
    print(error)
# the exception block deals with all errors not previously caught
# print statements in this block are ignored
except Exception as error:
    print("########## EXCEPT: Exception ############")
    print("Generic catch-all except / catch block")
    print(error)
# the finally block lets you execute code, regardless of the result of the try and except blocks
# print statements from this block runs
finally:
    #Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    # tuples are immutable, this if statement does nothing
    if names_tuple:
        names_tuple = None

print("After exception handling is finished...the program can continue")



