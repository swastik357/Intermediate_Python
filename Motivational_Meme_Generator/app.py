"""This is the main app to be served via flask."""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for file in quote_files:
        if Ingestor.parse(file):
            quotes.append(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = []
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    list_quotes = random.choice(quotes)
    quote = random.choice(list_quotes)
    if quote and img:
        path = meme.make_meme(img, quote.body, quote.author)
        return render_template('meme.html', path=path)
    else:
        path = meme.make_meme('./_data/photos/dog/xander_1.jpg', "-", "-")
        return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body, author = request.form['body'], request.form['author']
    image = requests.get(image_url)
    path = None
    try:
        image_file = f'tmp/{random.randint(0, 10000)}.jpg'
        open(image_file, 'wb').write(image.content)
    except e:
        print("Image could not be loaded")
        path = meme.make_meme('./_data/photos/dog/xander_1.jpg', "-", "-")
    else:
        path = meme.make_meme(image_file, body, author)
        os.remove(image_file)
    finally:
        return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
