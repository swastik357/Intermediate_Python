"""Encapsulates body and author."""


class QuoteModel():
    """Encapsulates body and author."""

    def __init__(self, body, author):
        """Initialize QuoteModel instance."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return descriptive string for QuoteModel instance."""
        return f"{self.body} - {self.author}"
