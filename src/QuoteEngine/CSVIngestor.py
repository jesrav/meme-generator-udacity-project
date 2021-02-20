from pathlib import Path
from typing import List

from pandas import read_csv

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class to ingest quotes from CSV-files"""

    allowed_extensions = [".csv"]

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Parse csv-file with quotes

        :param path: Path to CSV file
        :return: List of quotes
        """
        if not cls.file_exists(path):
            raise Exception("File does not exists")
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        quotes = []
        df = read_csv(path, header=0)

        for index, row in df.iterrows():
            quotes.append(QuoteModel(author=row["author"], body=row["body"]))
        return quotes
