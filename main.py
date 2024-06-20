try:
    import sys  # Import the 'sys' module, which gives us access to system-related functions.
    import time  # Import the 'time' module, which helps us set a slight delay when trying to exit the program.
    import webbrowser  # Import the 'webbrowser' module, which helps us open links automatically.

    import pyuac  # Import the 'pyuac' module, which helps us check if the user running the program is an admin or not. This is necessary because we don't want the CMD windows to pop up.
    from assets import (
        art,  # Import the 'logo' variable from the 'art.py' file, which is in the assets folder.
    )
    from assets import loader  # Import the 'loader' for loading animations.
    from assets import logger as lg
    from replit import (
        clear,  # Import the 'clear' function from the 'replit' module, so that we can clear the console.
    )
except ImportError:
    main_ready = False

if lg.logger_ready == False or loader.loader_ready == False:
    main_ready = False
else:
    main_ready = True

if main_ready == False:
    lg.calc_logs(message_type="critical", message="Failed to import modules!")
    print("An unknown error occured, please check the logs file.")
    exit()
elif main_ready == True:
    lg.calc_logs(message_type="info", message="Imported 11 modules, successfully.")


# Define functions for basic mathematical operations.
def add(n1, n2):
    return n1 + n2  # Calculate n1 added to n2.


def subtract(n1, n2):
    return n1 - n2  # Calculate n2 subtracted from n2.


def multiply(n1, n2):
    return n1 * n2  # Calculate n1 times n2.


def divide(n1, n2):
    return n1 / n2  # Calculate n1 divide by n2.


def raisePower(n1, n2):
    return n1**n2  # Calculate n1 raised to the power of n2.


def sqrt(n1, n2):
    return n1**0.5  # Calculate the square root of n1.


# Create a dictionary to map operation symbols to their corresponding functions.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": raisePower,
    "sqrt": sqrt,
}

# Create a URL variable for opening in case the program fails to run.
url = "https://www.youtube.com/watch?v=xMHJGd3wwZk/"


def main() -> None:
    """Main function is there to run the app."""
    print(art.logo)  # Display the imported logo.
    print("The calculator is loading")  # Loading message.
    loader.load_anim(2, 5)  # Loader function.

    try:  # Use a 'try...except' block to handle potential errors.
        num1 = float(
            input("What's the first number?\n")
        )  # Get the first number from the user and convert it to a decimal.
        for symbol in operations:
            print(symbol)  # Print the available operation symbols.
        loopState = True  # Initialize a loop state to control the calculation loop.
        operation_symbol = input(
            "Pick an operation from the line above: "
        )  # Get the chosen operation symbol from the user.
        if operation_symbol != "sqrt":
            num2 = float(
                input("What's the second number?\n")
            )  # Get the second number if the operation is not square root.
        else:
            num2 = 0  # Set the second number to 0 for the square root operation.
        calc_fun = operations[
            operation_symbol
        ]  # Get the function associated with the chosen operation symbol.
        first_result = calc_fun(
            num1, num2
        )  # Perform the calculation using the selected function and store the result.

        # Check if the operation symbol is valid.
        if (
            operation_symbol != "+"
            and operation_symbol != "-"
            and operation_symbol != "*"
            and operation_symbol != "/"
            and operation_symbol != "^"
            and operation_symbol != "sqrt"
        ):
            print("Please enter a valid operation!")

        # Print the calculation result based on the chosen operation.
        if (
            operation_symbol == "+"
            or operation_symbol == "-"
            or operation_symbol == "*"
            or operation_symbol == "/"
            or operation_symbol == "^"
        ):
            print(f"{num1} {operation_symbol} {num2} = {first_result}")
        elif operation_symbol == "sqrt":
            print(f"Square root of {num1} = {first_result}")

        # Ask the user if they want to continue calculating.
        first_wants_to_continue = input(
            f"Type 'c' to continue calculating with {first_result}, type 'n' to start a new calculation or type 'e' to exit: "
        ).lower()
        if first_wants_to_continue == "c":
            loopState = True  # Continue the calculation loop.
            clear()  # Clear the console.
            print(f"Last result: {first_result}")  # Printing last result after clear.
            while loopState is True:
                operation_symbol = input(
                    "Pick another operation: "
                )  # Get the next operation symbol.
                if operation_symbol != "sqrt":
                    num3 = float(
                        input("What's the next number?\n")
                    )  # Get the next number if the operation is not square root.
                else:
                    num3 = 0  # Set the next number to 0 for the square root operation.
                calc_fun = operations[
                    operation_symbol
                ]  # Get the function for the new operation.
                second_result = calc_fun(
                    first_result, num3
                )  # Perform the next calculation.

                # Check if the operation symbol is valid.
                if (
                    operation_symbol != "+"
                    and operation_symbol != "-"
                    and operation_symbol != "*"
                    and operation_symbol != "/"
                    and operation_symbol != "^"
                    and operation_symbol != "sqrt"
                ):
                    print("Please enter a valid operation!")

                # Print the calculation result based on the chosen operation.
                if (
                    operation_symbol == "+"
                    or operation_symbol == "-"
                    or operation_symbol == "*"
                    or operation_symbol == "/"
                    or operation_symbol == "^"
                ):
                    print(f"{first_result} {operation_symbol} {num3} = {second_result}")
                elif operation_symbol == "sqrt":
                    print(f"Square root of {first_result} = {second_result}")

                # Ask the user if they want to continue calculating.
                wants_to_continue = input(
                    f"Type 'c' to continue calculating with {second_result}, type 'n' to start a new calculation or type 'e' to exit: "
                ).lower()
                if wants_to_continue == "c":
                    clear()  # Clear the console.
                    print(
                        f"Last result: {second_result}"
                    )  # Printing last result after clear.
                    first_result = (
                        second_result  # Update the result for the next calculation.
                    )
                elif wants_to_continue == "n":
                    loopState = (
                        False  # Stop the calculation loop and restart the program.
                    )
                    clear()  # Clear the console.
                    main()
                elif wants_to_continue == "e":
                    print("Exit in 3 seconds from now!")  # Exit statement printed.
                    print("3")  # Time counter.
                    time.sleep(1)  # Delay of 1 second.
                    print("2")  # Time counter.
                    time.sleep(1)  # Delay of 1 second.
                    print("1")  # Time counter.
                    time.sleep(1)  # Delay of 1 second.
                    print("Goodbye!")  # Saying goodbye before exit.
                    time.sleep(
                        0.2
                    )  # Giving some time for the user to read the Goodbye message.
                    webbrowser.open(url, new=0, autoraise=True)  # Opens rick roll 😂!
                    exit()  # Exit the program.
                else:
                    print(
                        "Continuing to run the app because you didn't provide a valid input!"
                    )
                    main()  # Restart the program.
        elif first_wants_to_continue == "n":
            loopState = False  # Stop the loop and restart the program.
            clear()  # Clear the console.
            main()
        elif first_wants_to_continue == "e":
            print("Exit in 3 seconds from now!")  # Exit statement printed.
            print("3")  # Time counter.
            time.sleep(1)  # Delay of 1 second.
            print("2")  # Time counter.
            time.sleep(1)  # Delay of 1 second.
            print("1")  # Time counter.
            time.sleep(1)  # Delay of 1 second.
            print("Goodbye!")  # Saying goodbye before exit.
            time.sleep(
                0.2
            )  # Giving some time for the user to read the Goodbye message.
            webbrowser.open(url, new=0, autoraise=True)  # Opens rick roll 😂!
            exit()  # Exit the program.
        else:
            print("Continuing to run the app because you didn't provide a valid input!")
            main()  # Restart the program.

    except (
        KeyError
    ):  # Catch a KeyError (usually happens when an invalid operation symbol is entered).
        print("Invalid operation!")  # Error message.
        print("Restarting the program.")  # Restart message.
        loader.load_anim(load_type=2, time=5)  # Loading.
        clear()  # Clear the console.
        main()  # Restart the program.
    except (
        ValueError
    ):  # Catch a ValueError (usually happens when an invalid number is entered).
        print("Invalid numbers entered!")
        print("Restarting the program.")  # Restart message.
        loader.load_anim(load_type=2, time=5)  # Loading.
        clear()  # Clear the console.
        main()  # Restart the program.
    except (
        ZeroDivisionError
    ):  # Catch a ZeroDivisionError (usually happens when zero is the divisor).
        print("Can't divide by zero!")
        print("Restarting the program.")  # Restart message.
        loader.load_anim(load_type=2, time=5)  # Loading.
        clear()  # Clear the console.
        main()  # Restart the program.
    except Exception:  # Catch an unkown error (usually happens due to system issues.)
        print(
            "A critical error occured, please contact the\nowner and share the issue."
        )


# Increase the recursion limit to handle multiple continuous calculations.
sys.setrecursionlimit(2147483647)

# Checking if the user is an admin.
if __name__ == "__main__":
    if not pyuac.isUserAdmin():  # Checking if the user is an admin.
        print("Re-launching as admin!")
        pyuac.runAsAdmin()  # Restarting the program as an admin.
    else:
        main()  # Already an admin here.

# lg.logging.exception("message")

