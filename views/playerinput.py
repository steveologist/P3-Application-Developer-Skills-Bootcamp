"""Define InputPlayer object."""


from models.player import Player


class PlayerInput(Player):
    def __init__(
        self,
        last_name=False,
        first_name=False,
        birthday=False,
        sexe=False,
        rank=False,
    ):
        """Initiate PlyayerInput object."""
        super().__init__(last_name, first_name, birthday, sexe, rank)

    def input_last_name(self):
        """Input player last name."""
        self.last_name = str(input("What is the player's last name? : "))

    def input_first_name(self):
        """Input player first name."""
        self.first_name = str(input("What is the player's first name? "))

    def input_birthday_day(self):
        """Input player birthday day."""
        return int(input("Day of birth: "))

    def input_birthday_month(self):
        """Input player birthday month."""
        return int(input("Month of birth"))

    def input_birthday_year(self):
        """Input player birthday year."""
        return int(input("Year of birth: "))

    def input_sexe(self):
        """Input player sexe."""
        print(f"Gender : {self.possible_sexe}.")
        return int(
            input("which gender do you prefer? (type #) : ")
        )

    def input_rank(self):
        """Input player rank."""
        self.rank = int(input("Players rank "))
