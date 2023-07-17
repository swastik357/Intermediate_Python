"""CSV file parser returning list of quote model objects."""

import pandas as pd
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class to parse csv files and return list of quote model objects."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse csv file at path and return list of quote model objects."""
        if not cls.can_ingest(path):
            raise Exception("Not a csv file")

        list_quotes = []
        df = pd.read_csv(path, header=0, sep=',')
        for _, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            list_quotes.append(quote)

        return list_quotes
