"""Display tournament messages."""


from views import userinput


def change_the_number_of_rounds():
    """Display number of rounds modification and return user choice."""
    print(
        "The default number of rounds is 4. Would you like to modify it?"
    )

    return userinput.input_choice()


def add_a_description():
    """Display add a description and return user choice."""
    print("Add a description?")

    return userinput.input_choice()


def how_many_player_will_play():
    """Display how many player will player and return a number."""
    print(
        "How many players will participate in the tournament? (enter an even number and minimum 4): " # noqa 
    )

    return userinput.input_a_number()


def wich_player_will_play():
    """Display select a player by number and return a number."""
    print("Select a player to add to the tournament by their number. ")

    return userinput.input_a_number()


def validate_chosen_players():
    """Display validate chosen player and return user choice."""
    print("Do you confirm this player selection and start the tournament?")

    return userinput.input_choice()


def validate_creation():
    """Display validation tournament creation and return user choice."""
    print("Do you confirm the creation of the tournament? If not, return to the tournament menu.")

    return userinput.input_choice()


def display_tournament_summary(self):
    """Display tournament attributes."""
    print(
        f"""Summary:
Tournament Name: {self.name}
Location: {self.location}
Game Mode: {self.time_controller}
Tournament Duration: {self.duration} days
Number of Rounds: {self.number_of_rounds}
Description: {self.description}"""
    )


def display_start_tournament():
    """Display start tournament."""
    print("The tournament starts!")


def return_in_tournament():
    """Display return in tournament message and return user choice."""
    print("Return to the tournament?")

    return userinput.input_choice()


def display_standings(player_matchmaking, classement, i):
    """Display standings of the tournament."""
    print(
        f"{i+1}# with {classement[player_matchmaking[i]]} points: "
        f"{player_matchmaking[i].first_name} {player_matchmaking[i].last_name}"
    )


def display_player_in_tournament(self):
    """Display each player object in tournament players list attribut."""
    print("The following players are participating in the tournament:")
    for player in self.players_list:
        print(
            f"{self.players_list.index(player)}. {player.last_name} {player.first_name} ({player.rank})" # noqa
        )


def tournament_is_not_over(self):
    """Display tournament name isn't over with rounds remaining and ask to continue.""" # noqa 
    print(
        f"The tournament'{self['name']}' is not finished  "
        f"(There are still{self['number_of_rounds'] - len(self['rounds_list'])} rounds left to play). " # noqa
        "Continue this tournament?"
    )

    return userinput.input_choice()
