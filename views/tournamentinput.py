"""Define TournamentInput object."""


from models.tournament import Tournament


class InputTournament(Tournament):
    def __init__(
        self,
        name=False,
        location=False,
        date=False,
        time_controller=False,
        number_of_rounds=False,
        description=False,
        duration=False,
    ):
        """Initiate InputTournament object."""
        super().__init__(
            name,
            location,
            date,
            time_controller,
            number_of_rounds,
            description,
        )
        self.duration = duration

    def input_name(self):
        """Input tournament name."""
        self.name = str(input("What is the name of the tournament?: "))

    def input_location(self):
        """Input tournament location."""
        self.location = str(input("Where does the tournament take place?: "))

    def input_mode(self):
        """Display time controller mode and return user choice."""
        print(f"Here are the time management modes: {self.mode}.")
        return int(
            input("Which mode do you choose? (Type a number) ")
        )

    def input_duration(self):
        """Input tournament duration."""
        self.duration = int(
            input("How many days will the tournament " " last?: ")
        )

    def input_number_of_rounds(self):
        """Input number of rounds."""
        self.number_of_rounds = int(input("How many rounds? "))

    def input_description(self):
        """Input description."""
        self.description = input("Your description: ")
