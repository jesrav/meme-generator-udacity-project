from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Interface for ingestors"""

    allowed_extensions = []

    @classmethod
    def file_exists(cls, path: Path) -> bool:
        """Check if file exists

        :param path: Path to file
        :return: Does file exist? True/False
        """
        return path.exists()

    @classmethod
    def can_ingest(cls, path: Path) -> bool:
        """Check if filetype can be ingested

        :param path: Path to file
        :return: Can file be ingested? True/False
        """
        ext = path.suffix
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file with quotes

        :param path: Path to file
        :return: List of quotes
        """
        pass
