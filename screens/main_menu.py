from commands import ExitCmd, NoopCmd

from .base_screen import BaseScreen


class MainMenu(BaseScreen):
    """Main menu screen"""

    def __init__(self, clubs):
        self.clubs = clubs

    def display(self):
        for idx, club in enumerate(self.clubs, 1):
            print(idx, club.name)

    def get_command(self):
        while True:
            print("Type C to create a club or a club number to view/edit it.")
            print("Type T to view current tournaments or create a new tournament.")
            print("Type X to exit.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.clubs) + 1):
                    return NoopCmd("club-view", club=self.clubs[value - 1])
            elif value.upper() == "C":
                return NoopCmd("club-create")
            elif value.upper() == "T":
                return NoopCmd("tournament-menu")
            elif value.upper() == "X":
                return ExitCmd()
