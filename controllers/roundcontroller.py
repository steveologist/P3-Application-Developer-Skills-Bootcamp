"""Manage the running of a round."""


import time
from models.round import Round
from views import roundview


def create_round(i):
    """Create round attributs and return a round object."""
    name = f"Round {i+1}"
    beginning_date = "{}".format(time.strftime("%Y-%m-%d_%Hh"))
    ending_date = ""
    round = Round(name, beginning_date, ending_date)

    return round


def create_ending_round_date(self):
    """Create ending date and update ending date round object attribut."""
    self.ending_date = "{}".format(time.strftime("%Y-%m-%d_%Hh"))


def split_list(self):
    """Divide a list by two and return two lists."""
    half = len(self) // 2
    return self[:half], self[half:]


def run_matchmaking(round, tournament, last_round=False):
    """Check the round number and call matchmaking functions according."""
    if round.name == "Round 1":
        return create_matchmaking_for_first_round(tournament)

    else:
        return create_matchmaking_for_others_round(tournament, last_round)


def create_matchmaking_for_first_round(tournament):
    """Create matchmaking for first round and return a sorted player list."""
    players_matchmaking = []
    sorted_list = sorted(
        tournament.players_list, key=lambda player: player.rank, reverse=True
    )
    top_players, low_players = split_list(sorted_list)

    for i in range(len(top_players)):
        roundview.display_first_round_versus(i, top_players, low_players)
        players_matchmaking.append(top_players[i])
        players_matchmaking.append(low_players[i])

    return players_matchmaking


def create_matchmaking_for_others_round(tournament, last_round):
    """Create matchmaking and return a sorted player list."""
    players_and_scores = create_players_and_scores_dict(tournament)
    players_matchmaking = create_player_matchmaking_list(players_and_scores)

    if last_round is True:
        return players_matchmaking, players_and_scores

    else:
        players_matchmaking = arrange_list_if_player_already_played_together(
            tournament, players_matchmaking
        )
        format_and_display_versus_message(
            players_matchmaking, players_and_scores
        )

        return players_matchmaking


def create_players_and_scores_dict(tournament):
    """Create a dict with players object and them score and return it."""
    players_and_scores = {}

    for i in range(len(tournament.players_list)):
        players_and_scores[tournament.players_list[i]] = 0

    for i in range(len(tournament.rounds_list)):
        for j in range(len(tournament.rounds_list[i].match_list)):
            player_one = tournament.rounds_list[i].match_list[j][0][0]
            player_two = tournament.rounds_list[i].match_list[j][1][0]
            score_one = tournament.rounds_list[i].match_list[j][0][1]
            score_two = tournament.rounds_list[i].match_list[j][1][1]
            players_and_scores[player_one] += score_one
            players_and_scores[player_two] += score_two

    players_and_scores = dict(
        sorted(
            players_and_scores.items(), key=lambda item: item[1], reverse=True
        )
    )

    return players_and_scores


def create_player_matchmaking_list(players_and_scores):
    """Create a list of player and return it."""
    players_matchmaking = []
    players_and_scores_to_empty = dict(players_and_scores)
    players_list = list(players_and_scores)

    while players_and_scores_to_empty != {}:
        temp_player_list = []
        try:
            temp_player_list.append(players_list[0])
        except IndexError:
            break
        for player in players_list:
            if (
                players_and_scores_to_empty[temp_player_list[0]]
                == players_and_scores_to_empty[player]
            ):
                if player in temp_player_list:
                    continue
                else:
                    temp_player_list.append(player)

                del players_and_scores_to_empty[player]

        temp_player_list = sorted(
            temp_player_list, key=lambda player: player.rank, reverse=True
        )

        for player in temp_player_list:
            players_matchmaking.append(player)
            players_list.remove(player)

    return players_matchmaking


def arrange_list_if_player_already_played_together(
    tournament, players_matchmaking
):
    """Arrange matchmaking player list and return player list according."""
    for i in range(len(tournament.rounds_list)):
        for j in range(len(tournament.rounds_list[i].match_list)):
            player_one = tournament.rounds_list[i].match_list[j][0][0]
            player_two = tournament.rounds_list[i].match_list[j][1][0]

            if (
                player_one == players_matchmaking[0]
                and player_two == players_matchmaking[1]
            ):
                roundview.display_players_already_played_together(
                    player_one, player_two
                )
                players_matchmaking[1], players_matchmaking[2] = (
                    players_matchmaking[2],
                    players_matchmaking[1],
                )

    return players_matchmaking


def format_and_display_versus_message(players_matchmaking, players_and_scores):
    """Prepare arguments to display versus message."""
    players_matchmaking_for_view = players_matchmaking
    players_and_scores_for_view = players_and_scores

    for i in range(len(players_matchmaking_for_view) // 2):
        roundview.display_other_round_versus(
            i, players_matchmaking_for_view, players_and_scores_for_view
        )
        players_matchmaking_for_view = players_matchmaking_for_view[1:]
