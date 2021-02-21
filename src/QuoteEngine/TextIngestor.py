from pathlib import Path
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Class to ingest quotes from TXT-files"""

    allowed_extensions = [".txt"]

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Parse text files with quotes

        :param path: Path to text file
        :return: List of quotes
        """
        if not cls.file_exists(path):
            raise Exception("File does not exists")
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest Exception")

        with open(path, "r", encoding='utf-8-sig') as file:
            quotes = []
            for line in file:
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    body, author = line.split(" - ")
                    body = body.strip('"')
                    quotes.append(QuoteModel(author=author, body=body))

        return quotes
