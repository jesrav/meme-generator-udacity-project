from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        with open(path, "r") as file:
            quotes = []
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    body, author = line.split(' - ')
                    body = body.strip('"')
                    quotes.append(
                        QuoteModel(author=author, body=body)
                    )

        return quotes
