"""Define round object."""


class Round:
    def __init__(self, name, beginning_date, ending_date):
        """Initate round object."""
        self.name = name
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.match_list = []


class DictToRound(Round):
    def __init__(
        self, dict, name=False, beginning_date=False, ending_date=False
    ):
        """Initiate dict to round object."""
        super().__init__(name, beginning_date, ending_date)
        for key in dict:
            setattr(self, key, dict[key])
