from dataclasses import dataclass


@dataclass
class QuoteModel:
    """Class to represent a quote"""

    author: str
    body: str
