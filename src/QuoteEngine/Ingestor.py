from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .PDFIngestor import PDFIngestor
from .DOCXIngestor import DocxIngestor
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor


class Ingestor(IngestorInterface):
    ingestors = {
        'csv': CSVIngestor,
        'txt': TXTIngestor,
        'pdf': PDFIngestor,
        'docx': DocxIngestor,
    }

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        ext = path.split('.')[-1]
        if ext not in cls.ingestors.keys():
            raise ValueError(f"Filetype not suported. Extension must be one of {list(cls.ingestors.keys())}")

        return cls.ingestors[ext].parse(path)
