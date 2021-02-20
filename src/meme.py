import os
import random
from pathlib import Path

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel

DOG_IMAGE_DIRECTORY = Path("src/_data/photos/dog")
TMP_IMAGE_DIRECTORY = Path("src/_data/tmp")


def generate_meme(path: Path = None, body: str = None, author: str = None):
    """ Generate a meme given an path and a quote """

    if path is None:
        imgs = list(DOG_IMAGE_DIRECTORY.glob("*.jpg"))
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_file_paths = [
            Path("src/_data/DogQuotes/DogQuotesTXT.txt"),
            Path("src/_data/DogQuotes/DogQuotesDOCX.docx"),
            Path("src/_data/DogQuotes/DogQuotesPDF.pdf"),
            Path("src/_data/DogQuotes/DogQuotesCSV.csv"),
        ]
        quotes = []
        for f in quote_file_paths:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine(TMP_IMAGE_DIRECTORY)
    path = meme.make_meme(img, quote)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    args = None
    print(generate_meme(args.path, args.body, args.author))
