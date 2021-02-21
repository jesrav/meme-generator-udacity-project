import random
from pathlib import Path
from typing import Union

import click

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel

DOG_IMAGE_DIRECTORY = Path("./_data/photos/dog")
TMP_IMAGE_DIRECTORY = Path("./_data/tmp")


def generate_meme(
    path: Union[Path, None] = None,
    body: Union[str, None] = None,
    author: Union[str, None] = None,
) -> Path:
    """ Generate a meme given an path and a quote """

    if path is None:
        images = list(DOG_IMAGE_DIRECTORY.glob("*.jpg"))
        image = random.choice(images)
    else:
        image = path

    if body is None:
        quote_file_paths = [
            Path("./_data/DogQuotes/DogQuotesTXT.txt"),
            Path("./_data/DogQuotes/DogQuotesDOCX.docx"),
            Path("./_data/DogQuotes/DogQuotesPDF.pdf"),
            Path("./_data/DogQuotes/DogQuotesCSV.csv"),
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
    out_path = meme.make_meme(image, quote)
    return out_path


@click.command()
@click.option("--path", type=click.Path(exists=True))
@click.option("--body", type=str)
@click.option("--author", type=str)
def main(path, body, author):
    if path:
        path = Path(path)
    meme_path = generate_meme(path, body, author)
    print(meme_path)


if __name__ == "__main__":
    main()
