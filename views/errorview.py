"""Displays error messages."""


def display_wrong_choice_message():
    """Display message the user input an unauthorized number."""
    print("You did not choose a valid number.")


def display_not_an_integer_message():
    """Display message the user not input an integer."""
    print(" You did not choose an integer.")


def display_not_an_integer_or_float_number():
    """Display message the user not input an float."""
    print("You did not choose an integer or decimal number.")


def display_its_blank_message():
    """Display message the user input is blank."""
    print("You did not enter any text.")


def display_not_in_selection_range():
    """Display message the user input out of range number."""
    print("You did not enter a valid selection number.")


def display_not_positive_integer():
    """Display message the user input not an positive number."""
    print("You did not enter a positive integer.")


def display_not_possible_birthday_date():
    """Display message the user input an impossible date."""
    print(
        """You did not enter a possible date.
Days: between 1 and 31.
Months: between 1 and 12.
Year: between 1900 and the current year minus sixteen."""
    )


def display_this_player_is_already_chosen():
    """Display message the user chosen player is already in player list."""
    print("The selected player is already in the list of players")


def display_has_a_number():
    """Display message the user input a number."""
    print("Error: Numbers are not allowed. ")


def display_not_an_even_number():
    """Display message the user not input an even number."""
    print("Error: You did not enter an even number")


def display_you_selected_too_much_player():
    """Display message the user selected too much player."""
    print("Error: You entered more players than there are in the database")


def display_not_enough_player():
    """Display message the user selected not enough player."""
    print("Error: The minimum number of players must be 4. ")
