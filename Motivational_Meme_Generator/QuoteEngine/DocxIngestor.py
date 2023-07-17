"""Docx file parser returning list of quote model objects."""

import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class to parse docx files and return list of quote model objects."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file at given path and return list of quote model objects."""
        if not cls.can_ingest(path):
            raise Exception("Not a docx file")

        infile = docx.Document(path)
        list_quotes = []
        for para in infile.paragraphs:
            if para.text != "":
                text = para.text.split(' - ')
                quote_model = QuoteModel(text[0], text[1])
                list_quotes.append(quote_model)

        return list_quotes
