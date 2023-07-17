"""Ingestor class realizes IngestorInterface abstract base class and \
encapsulates helper classes."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Logic to select helper for a file based on filetype."""

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method to parse file at given path and type."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
