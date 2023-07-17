"""PDF file parser returning list of quote model objects."""

import os
import subprocess
import random
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse pdf files and return list of quote model objects."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file at given path and return list of QuoteModel objects."""
        list_quotes = []
        if not cls.can_ingest(path):
            raise Exception("Not a pdf file")

        temp = f'./tmp/{random.randint(0, 10000)}.txt'
        try:
            call = subprocess.call(['pdftotext', path, temp])
            with open(temp, 'r') as file:
                file_lines = file.readlines()
        except FileNotFoundError as filenotfounderror:
            print(f'Error: {filenotfounderror}')
            return list_quotes

        for line in file_lines:
            line = line.strip('\n\r').strip()
            length_line = len(line)
            if length_line > 0:
                parsed_line = line.split(' - ')
                quote_model = QuoteModel(parsed_line[0], parsed_line[1])
                list_quotes.append(quote_model)

        file.close()
        os.remove(temp)
        return list_quotes
