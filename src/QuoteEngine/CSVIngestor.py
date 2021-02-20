from typing import List

from pandas import read_csv

from src.QuoteEngine.IngestorInterface import IngestorInterface
from src.QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        df = read_csv(path, header=0)

        for index, row in df.iterrows():
            quotes.append(
                QuoteModel(author=row['author'], body=row['body'])
            )
        return quotes


