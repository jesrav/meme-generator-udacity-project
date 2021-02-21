import random
import os
import uuid
from typing import Union, List

import requests
from pathlib import Path
from flask import Flask, render_template, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel


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


def download_image_from_url(url: str) -> Path:
    """Download image from url"""

    response = requests.get(url)
    out_path = Path("./static") / Path(str(uuid.uuid4()) + ".jpg")
    with open(out_path, "wb") as file:
        file.write(response.content)
    return out_path


def generate_meme(
    default_images: List[Path],
    default_quotes: List[QuoteModel],
    image_url: Union[str, None] = None,
    author: Union[str, None] = None,
    body: Union[str, None] = None,
) -> Path:
    """Generate meme

    If No image url is passed, a random image is selected from default_images.
    If No quote is passed, a random image is selected from default_quotes.

    :param default_images: List of default images
    :param default_quotes: List of default quotes
    :param image_url: Image url
    :param author: Author name
    :param body: Body of quote
    :return: Path of generated meme
    """
    if image_url:
        image_path = download_image_from_url(image_url)
    else:
        image_path = random.choice(default_images)

    if author and body:
        quote = QuoteModel(author=author, body=body)
    else:
        quote = random.choice(default_quotes)
    path = meme.make_meme(image_path, quote)
    if image_url:
        os.remove(image_path)
    return path


quotes, images = setup()


@app.route("/")
def meme_rand():
    """ Generate a random meme """
    path = generate_meme(
        default_images=images,
        default_quotes=quotes,
    )
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """ User input for meme information """
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get("image_url")
    body = request.form.get("body")
    author = request.form.get("author")

    path = generate_meme(
        default_images=images,
        default_quotes=quotes,
        image_url=image_url,
        author=author,
        body=body,
    )
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
