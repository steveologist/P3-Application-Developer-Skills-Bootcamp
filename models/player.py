
"""Define player object."""


class Player:

    possible_sexe = {0: "male", 1: "female"}

    def __init__(self, last_name, first_name, birthday, sexe, rank):
        """Initiate player object."""
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sexe = sexe
        self.rank = rank

    def update_player_rank(self, new_rank):
        """Update player rank attribut."""
        self.rank = new_rank


class DictToPlayer(Player):
    def __init__(
        self,
        dict,
        last_name=False,
        first_name=False,
        birthday=False,
        sexe=False,
        rank=False,
    ):
        """Initiate dict to player object."""
        super().__init__(last_name, first_name, birthday, sexe, rank)
        for key in dict:
            setattr(self, key, dict[key])
