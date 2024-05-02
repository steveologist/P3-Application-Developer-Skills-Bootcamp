"""Manage system function."""


from views import systemview


def exit_application():
    """Choice to quit the application."""
    choice = systemview.display_exit_message()
    if choice.upper() == "Q":
        exit()


def choice_verification(choice):
    """Check choice and return True according."""
    if choice.upper() == "O":
        return True
