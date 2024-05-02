"""Display menus texts."""


from views import userinput


def display_main_menu():
    """Display main menu and return a user choice."""
    print(
        """Main Menu :
        1. Tournament ->
        2. Players ->
        3. Reports ->
        4. Quit.
        """
    )

    return userinput.input_a_number()


def display_tournament_menu():
    """Display tournament menu and return a user choice."""
    print(
        """Tournament Menu:
            1. Start a tournament ->
            2. Back <-"
        """
    )

    return userinput.input_a_number()


def display_player_menu():
    """Display player menu and return a user choice."""
    print(
        """Player Menu:
        1. Add a new player to the database ->
        2. Back <-"
        """
    )

    return userinput.input_a_number()


def display_report_menu():
    """Display report menu and return a user choice."""
    print(
        """Report Menu:
        1. Display a report ->
        2. Back <-
        """
    )

    return userinput.input_a_number()
