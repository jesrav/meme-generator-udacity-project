from typing import List

import docx

from src.QuoteEngine.IngestorInterface import IngestorInterface
from src.QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split(' - ')
                body = body.strip('"')
                quotes.append(
                    QuoteModel(author=author, body=body)
                )

        return quotes


