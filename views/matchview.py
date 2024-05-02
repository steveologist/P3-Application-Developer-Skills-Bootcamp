"""Display match messages."""


from views import userinput


def display_match_to_note(i, players):
    """Display match to note."""
    print(
        f"\nNotation match #{i} : "
        f"{players[0].first_name} {players[0].last_name} vs "
        f"{players[1].first_name} {players[1].last_name}"
    )


def note_the_match(self):
    """Display player name and surname and return his result."""
    print(
        f"Results of {self[0].first_name} {self[0].last_name} "
        "(1 for win, 0 for loss, 0.5 for draw) : "
    )

    return userinput.input_a_float()


def validate_match_result():
    """Display message and return user input."""
    print("Do you validate the scores?")

    return userinput.input_choice()
