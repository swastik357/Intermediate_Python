"""Text file parser returning list of quote model objects."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Class to parse txt files and return list of quote model objects."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file at given path and return list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Not a txt file")

        infile = open(path, "r")
        list_quotes = []

        for line in infile.readlines():
            line = line.strip('\n\r').strip()
            length_line = len(line)
            if length_line > 0:
                parsed_line = line.split(' - ')
                quote_model = QuoteModel(parsed_line[0], parsed_line[1])
                list_quotes.append(quote_model)

        infile.close()
        return list_quotes
