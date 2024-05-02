"""Defines exceptions."""


class EmptyInputException(Exception):
    """Manage exception for empty input."""

    pass


class OutOfRangeException(Exception):
    """Manage exception for out of range input."""

    pass


class NotPositiveIntegerException(Exception):
    """Manage exception for not positive integer input."""

    pass


class ImpossibleBirthdayDateException(Exception):
    """Manage exception for impossible birthday date input."""

    pass


class WrongChosenPlayerException(Exception):
    """Manage exception for already chosen player."""

    pass


class HasNumberException(Exception):
    """Manage exception for number in a list of string."""

    pass


class NotAnEvenNumberException(Exception):
    """Manage exception for not even number."""

    pass


class NotEnoughPlayerInDatabaseException(Exception):
    """Manage exception for bigger number of player selected as player in database.""" # noqa

    pass


class NumberOfPlayerIsTooLow(Exception):
    """Manage exception for number of player is too low."""

    pass
