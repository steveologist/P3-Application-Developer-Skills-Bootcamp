"""Define tournament object."""


class Tournament:

    mode = {0: "bullet", 1: "blitz", 2: "rapide"}

    def __init__(
        self,
        name,
        location,
        date,
        time_controller,
        number_of_rounds,
        description,
    ):
        """Initiate tournament object."""
        self.name = name
        self.location = location
        self.date = date
        self.time_controller = time_controller
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.rounds_list = []
        self.players_list = []

    def add_player_in_players_list(self, player):
        """Add player object in tournament players list attribut."""
        self.players_list.append(player)

    def add_round_in_rounds_list(self, round):
        """Add round object in tournament rounds list attribut."""
        self.rounds_list.append(round)


class DictToTournament(Tournament):
    def __init__(
        self,
        dict,
        name=False,
        location=False,
        date=False,
        time_controller=False,
        number_of_rounds=False,
        description=False,
    ):
        """Initiate dict to tournament object."""
        super().__init__(
            name,
            location,
            date,
            time_controller,
            number_of_rounds,
            description,
        )
        for key in dict:
            setattr(self, key, dict[key])
