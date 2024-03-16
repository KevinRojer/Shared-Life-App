import logging
from datetime import datetime


def log_message(logging, message, level="infor"):
    """"
    Logs a message to the log file and console.

    Args:
        message: str
            The message to log
        level: str
            The logging level ('info', 'warning', 'error').
    """
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    else:
        raise ValueError("Logging level not appropriate.")
    
    print(message)


def show_message(message):
    """
    Display a message to the user.

    Args:
        message: str
            The message to display.
    """
    print(f"{message}")


def show_error(messgae):
    """
    Displays an error message to the user and logs the error.

    Args:
        message: str
            The error message to display.
    """
    log_message(message, "error")
    print(f"Error: {messgae}")


def input_with_prompt(prompt):
    """
    Displays a prompt to the user and returns the input.

    Args:
        prompt (str): The prompt message to display.

    Returns:
        str: The user input.
    """
    return input(prompt)