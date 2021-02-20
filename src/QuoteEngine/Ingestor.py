from pathlib import Path
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .PDFIngestor import PDFIngestor
from .DOCXIngestor import DocxIngestor
from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor


class Ingestor(IngestorInterface):
    ingestors = {
        ".csv": CSVIngestor,
        ".txt": TextIngestor,
        ".pdf": PDFIngestor,
        ".docx": DocxIngestor,
    }

    @classmethod
    def parse(cls, path: Path) -> List[QuoteModel]:
        ext = path.suffix
        print(ext)
        if ext not in cls.ingestors.keys():
            raise ValueError(
                f"Filetype not supported. Extension must be one of {list(cls.ingestors.keys())}"
            )

        return cls.ingestors[ext].parse(path)
