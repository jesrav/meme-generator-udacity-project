from pathlib import Path
from typing import List

import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class to ingest quotes from DOCX-files"""

    allowed_extensions = [".docx"]

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        """Parse DOCX-file with quotes

        :param path: Path to DOCX file
        :return: List of quotes
        """
        if not cls.file_exists(path):
            raise Exception("File does not exists")
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split(" - ")
                body = body.strip('"')
                quotes.append(QuoteModel(author=author, body=body))

        return quotes
