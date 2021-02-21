import random
from pathlib import Path

import click

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
    out_path = meme.make_meme(img, quote)
    return out_path


@click.command()
@click.option("--path", type=click.Path(exists=True))
@click.option("--body", type=str)
@click.option("--author", type=str)
def main(path, body, author):
    path = Path(path)
    out_path = generate_meme(path, body, author)
    print(out_path)


if __name__ == "__main__":
    out_path = main()
