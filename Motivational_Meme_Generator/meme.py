"""This is CLI app."""

import os
import random
import argparse

from MemeEngine import MemeEngine
from QuoteEngine import QuoteModel, Ingestor


def generate_meme(path=None, body=None, author=None):
    """Generate meme given path and quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # path - path to image file
    # body - quote to add to image
    # author - quote author to add to image
    parser = argparse.ArgumentParser(description="This is Meme Generator app.")
    parser.add_argument('--path', type=str,
                        default=None, help="path to image file")
    parser.add_argument('--body', type=str,
                        default=None, help="quote to add to image")
    parser.add_argument('--author', type=str,
                        default=None, help="quote author to add to image")

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
