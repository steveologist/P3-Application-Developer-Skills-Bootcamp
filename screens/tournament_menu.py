from commands import ExitCmd, NoopCmd
from .base_screen import BaseScreen


class TournamentMenu(BaseScreen):
    """Tournament Menu Screen"""

    def __init__(self) -> None:
        print("Tournament Menu")
        pass

    def get_command(self):
        while True:
            # view all tournament
            # create a new tournament
            # ask user for input
            print("Type C to create a tournaments or create a new tournament.")
            print("Type B to go back.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.clubs) + 1):
                    return NoopCmd("club-view", club=self.clubs[value - 1])
            elif value.upper() == "C":
                return NoopCmd("tournament-menu")
            elif value.upper() == "X":
                return ExitCmd()
        pass
