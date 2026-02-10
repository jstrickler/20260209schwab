"""
This is the doc string for the module/script.
"""
import sys

# other imports  (standard library, third-party, local)

# constants (AKA global variables -- keep these to a minimum)

# main function
def main(args):   # could be named "fandango"
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    function1()

# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """
    print("this is function1()")

print(f"{__name__ = }")


if __name__ == '__main__':
    # if not imported as a module
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
