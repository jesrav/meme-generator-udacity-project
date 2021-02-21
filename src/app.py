import random
import os
import requests
from pathlib import Path
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine(Path("./static"))


def setup():
    """ Load all resources """

    quote_file_paths = [
        Path("./_data/DogQuotes/DogQuotesTXT.txt"),
        Path("./_data/DogQuotes/DogQuotesDOCX.docx"),
        Path("./_data/DogQuotes/DogQuotesPDF.pdf"),
        Path("./_data/DogQuotes/DogQuotesCSV.csv"),
    ]

    quotes = []
    for f in quote_file_paths:
        quotes.extend(Ingestor.parse(f))

    images_path = Path("./_data/photos/dog/")
    images = list(images_path.glob("*.jpg"))

    return quotes, images


quotes, images = setup()


@app.route("/")
def meme_rand():
    """ Generate a random meme """

    img = quote = random.choice(images)
    quote = quote = random.choice(quotes)
    path = meme.make_meme(img, quote)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """ User input for meme information """
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
