from enum import auto, StrEnum


class AccountType(StrEnum):
    CHECKING = auto()
    SAVINGS = auto()
    CREDIT = auto()
    INVESTMENT = auto()
    MORTGAGE = auto()
    DEBT = auto()
    OTHER = auto()