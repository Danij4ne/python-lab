 
# EXERCISE 1 — Safe conversion and division
# Goal: Practice ValueError, ZeroDivisionError, else, finally
# Requirements:
#  - Ask for a number with input and convert it to int.
#  - Divide 100 by that number.
#  - Handle ValueError and ZeroDivisionError with specific except blocks.
#  - In else, print the result if everything is fine.
#  - In finally, print a closing message.
 

try:
    user_number = int(input("Enter a number: "))
    result = 100 / user_number
except ValueError:
    print("Error: the value entered cannot be converted to an integer.")
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
else:
    print(f"Everything went well, the result is {result:.2f}")
finally:
    print("Closing program for exercise 1.")


 
# EXERCISE 2 — List indices and types
# Goal: Practice IndexError, ValueError and generic capture with my_error
# Requirements:
#  - Create a fixed list, for example: data = [10, 20, 30].
#  - Ask for an index with input and show the corresponding element.
#  - Handle:
#       * ValueError when converting the index to int
#       * IndexError if the index does not exist
#       * Exception as a safety net: except Exception as my_error
#  - In else, print “Access OK”.
#  - In finally, print “End of list access”.
 

try:
    data = [10, 20, 30, 59, 90, 5]
    user_index = int(input("Choose an index (0, 1, 2...): "))
    print(f"Element at index {user_index}:", data[user_index])
except ValueError:
    print("Error: index must be an integer.")
except IndexError:
    print("Error: index out of range.")
except Exception as my_error:
    print("Unexpected error type:", type(my_error).__name__)
    print("Error detail:", my_error)
else:
    print("Access OK.")
finally:
    print("End of list access.")


 
# EXERCISE 3 — Files with finally
# Goal: Practice FileNotFoundError, PermissionError and using finally to close resources
# Requirements:
#  - Ask for a filename with input and try to open it in read mode.
#  - Read the first line and show it.
#  - Handle FileNotFoundError and PermissionError with specific except blocks.
#  - In except Exception as my_error capture any other unexpected error and show:
#       * type(my_error).__name__
#       * the error itself
#  - In finally close the file IF and only IF it was opened.
 

file_obj = None

try:
    filename = input("Enter file name: ")
    file_obj = open(filename, "r", encoding="utf-8")
    first_line = file_obj.readline()
    print("First line of the file:")
    print(first_line)
except FileNotFoundError:
    print("Error: file not found.")
except PermissionError:
    print("Error: permission denied when trying to open the file.")
except Exception as my_error:
    print("Unexpected error type:", type(my_error).__name__)
    print("Error detail:", my_error)
finally:
    if file_obj is not None and not file_obj.closed:
        file_obj.close()
        print("File closed correctly.")
    print("Exercise 3 finished.")


 
# EXERCISE 4 — Dictionary and required keys
# Goal: Practice KeyError, else and error logging
# Requirements:
#  - Create a dictionary, e.g.: user = {"name": "Ana", "age": 23}
#  - Ask the user for a key to query ("name", "age", "email"...).
#  - Try to print the value for that key.
#  - Handle KeyError printing “The key X does not exist”.
#  - In else print “Key found correctly”.
#  - In except Exception as my_error store the error in a variable called my_error
#    and show it together with type(my_error).__name__.
#  - In finally print “Lookup finished”.
 

user = {"name": "Ana", "age": 23}

key_to_search = input("Enter the key to look up (e.g. 'name', 'age', 'email'): ")

try:
    value = user[key_to_search]
    print(f"Value for '{key_to_search}': {value}")
except KeyError as my_error:
    print(f"The key '{key_to_search}' does not exist.")
    print("Error type:", type(my_error).__name__)
except Exception as my_error:
    print("Unexpected error type:", type(my_error).__name__)
    print("Error detail:", my_error)
else:
    print("Key found correctly.")
finally:
    print("Lookup finished.")


 
# EXERCISE 5 — Validation with raise + mixed handling
# Goal: Practice raise, custom ValueError, multiple except and finally
# Requirements:
#  - Ask for a number from 1 to 10.
#  - If it is not in range, manually raise:
#       raise ValueError("The number must be between 1 and 10")
#  - If the input cannot be converted to int, capture it with ValueError
#    (using a different message when it is due to range vs conversion).
#  - Add an except Exception as my_error as a safety net that prints:
#       * "Unexpected error", type(my_error).__name__, and my_error
#  - In else print “Valid number: X”.
#  - In finally print “Validation finished”.
 

try:
    raw_value = input("Enter a number between 1 and 10: ")
    try:
        number = int(raw_value)
    except ValueError:
        # Conversion error
        raise ValueError("Conversion error: the input value is not a valid integer.")

    if not 1 <= number <= 10:
        # Range error (custom)
        raise ValueError("The number must be between 1 and 10.")

except ValueError as my_error:
    message = str(my_error)
    if "Conversion error" in message:
        print(message)
    elif "between 1 and 10" in message:
        print(message)
    else:
        print("ValueError:", message)
except Exception as my_error:
    print("Unexpected error")
    print("Type:", type(my_error).__name__)
    print("Detail:", my_error)
else:
    print(f"Valid number: {number}")
finally:
    print("Validation finished.")






























