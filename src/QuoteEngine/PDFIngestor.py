from typing import List
import subprocess
import tempfile

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        temp = tempfile.NamedTemporaryFile(suffix=".txt")
        p = subprocess.Popen(['pdftotext', '-simple', path, temp.name], stdout=subprocess.PIPE)
        _, err = p.communicate()
        if err:
            raise OSError("Error in call to pdftotext")

        with open(temp.name, "r") as file:

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
