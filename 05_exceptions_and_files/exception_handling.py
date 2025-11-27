
# Exception handling → try, except, else, finally

"""
try:    → put here the code that might fail.

except: → defines what to do if an error happens.

else:   → runs only if no error occurs inside try.
"""

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:  # User typed something that is not a valid integer.
    print("Error: you did not enter a valid number.")
except ZeroDivisionError:  # User entered 0, division by zero.
    print("Error: division by zero is not allowed.")
else:  # Runs only if no exception was raised in try.
    print("Everything went well, the result is:", result)
finally:  # Runs always, whether there was an error or not.
    print("Program finished. Closing calculator.")


# COMMON ERROR TYPES IN PYTHON

# Syntax errors (before running the program)
# SyntaxError        → invalid Python syntax (missing parenthesis, etc.).
# IndentationError   → wrong indentation (spaces / tabs).

# Runtime errors (while the program is running)

# Numeric errors
# ZeroDivisionError  → division by zero.
# OverflowError      → numeric result too large.
# FloatingPointError → floating point operation error.

# Type and conversion errors
# TypeError          → incompatible types (for example, number + string).
# ValueError         → value is invalid for the expected type (for example, int("hello")).
# IndexError         → index out of range in list or tuple.
# KeyError           → access to a non-existing key in a dictionary.
# AttributeError     → attribute or method does not exist in the object.
# NameError          → variable not defined.
# UnboundLocalError  → local variable used before being assigned.
# NotImplementedError → method or function not yet implemented.

# File and system errors
# FileNotFoundError  → file does not exist.
# IOError            → general input/output error.
# PermissionError    → no permission to access file or directory.
# IsADirectoryError  → trying to use a directory as a file.
# EOFError           → unexpected end of file when reading.

# Import and module errors
# ImportError        → error importing a module or object.
# ModuleNotFoundError → imported module does not exist.

# Iteration errors
# StopIteration      → iterator has no more elements.
# RecursionError     → too many recursive calls.

# Other errors
# AssertionError     → raised when an assert fails.
# RuntimeError       → general runtime error.
# SystemError        → internal Python error (rare in normal code).
# KeyboardInterrupt  → program interrupted manually (Ctrl + C).
# MemoryError        → out of memory.
# OSError            → general operating system error.
# TimeoutError       → operation exceeded allowed time.

# Note:
# You can catch all of them with: except Exception as e:
# Or catch a specific one, for example: except ValueError:


try:
    number = int(input("Enter a number: "))
    result = 10 / number
except Exception as my_error:  # Catches any kind of exception and stores it in my_error.
    print("An error occurred:", my_error)
    print("Error type:", type(my_error).__name__)  # __name__ returns the error type as text.
else:
    print("Everything went well, the result is:", result)
finally:
    print("End of program.")
































































