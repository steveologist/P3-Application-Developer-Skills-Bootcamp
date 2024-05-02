"""Display club messages."""


from views import userinput


def validate_creation():
    """Display player creation validation and return user choice."""
    print("Do you confirm thus club?.")

    return userinput.input_choice()


def display_player_summary(self):
    """Display club attributs."""
    print(
        f"""Summary :
    club Name: {self.last_name}
    First Name: {self.first_name}
    Date of Birth: {self.birthday}
    Gender: {self.sexe}
    Ranking: {self.rank}"""
    )


def change_player_rank():
    """Display ask player rank modification and return user choice."""
    print("Do you want to modify the ranking of a player?")

    return userinput.input_choice()


def select_a_player_to_change_his_rank():
    """Display select a player and return user choice number."""
    print("Select a player to modify their ranking.")

    return userinput.input_a_number()


def choice_new_rank():
    """Display enter a rank number and return number."""
    print("Enter a number for the new ranking: ")

    return userinput.input_a_number()


def display_player_rank_is_update(self):
    """Display player last and first name with new rank value."""
    print(
        f"The ranking of {self.last_name} {self.first_name} has been updated({self.rank})." # noqa
    )


def display_added_player_message(self):
    """Display added player message."""
    print(f"{self.last_name} {self.first_name} is added.\n")
