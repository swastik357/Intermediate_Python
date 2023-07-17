"""Abstract base class for parsing files and returning list \
of quotemodel objects."""

from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """Abstract base class for parsing files and returning list of \
quotemodel objects."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if current file can be parsed."""
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse the ingestible file and return list of \
quotemodel objects."""
        pass
