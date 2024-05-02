"""Display round messages."""


from views import userinput


def start_round(self):
    """Display start round number and return user choice."""
    print(f"Start the round {self+1} ?")

    return userinput.input_choice()


def display_round_name(self):
    """Display round name attribute."""
    print(self.name)


def end_round(self):
    """Display end round number and return user choice."""
    print(f"End the round{self+1} ?")

    return userinput.input_choice()


def display_first_round_versus(i, top_players, low_players):
    """Display first round versus."""
    print(
        f"Match #{i+1} : "
        f"{top_players[i].first_name} {top_players[i].last_name} {top_players[i].rank} vs " # noqa
        f"{low_players[i].first_name} {low_players[i].last_name} {low_players[i].rank} (plays as white)." # noqa
    )


def display_other_round_versus(
    i, players_matchmaking_for_view, players_and_scores_for_view
):
    """Display other round versus."""
    print(
        f"Match #{i+1} : "
        f"{players_matchmaking_for_view[i].first_name} {players_matchmaking_for_view[i].last_name} " # noqa
        f"({players_and_scores_for_view[players_matchmaking_for_view[i]]}) vs "
        f"{players_matchmaking_for_view[i+1].first_name} {players_matchmaking_for_view[i+1].last_name} " # noqa
        f"({players_and_scores_for_view[players_matchmaking_for_view[i+1]]}) (plays as white)." # noqa
    )


def display_players_already_played_together(player_one, player_two):
    """Display players already play together."""
    print(f"{player_one.last_name} Has already played with {player_two.last_name}.")
