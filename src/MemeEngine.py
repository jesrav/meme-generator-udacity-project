from pathlib import Path
import uuid

from PIL import Image, ImageDraw, ImageFont

from QuoteEngine.QuoteModel import QuoteModel


FONT_PATH = Path("./fonts/Alviena-Regular.ttf")


class MemeEngine:
    """Class for generating memes"""

    allowed_extensions = [".jpg", ".png"]

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir

    @classmethod
    def load_image(cls, path: Path) -> Image:
        """Load image

        Load image as Pillow image.
        :param path: Path of image file
        :return: Pillow image
        """
        if not path.exists():
            raise ValueError("Image does not exist.")
        if path.suffix not in cls.allowed_extensions:
            raise ValueError(
                f"Image file type not supported. Supported types are: {cls.allowed_extensions}"
            )
        return Image.open(str(path))

    def save_image(self, image: Image) -> Path:
        """Save pillow image

        Saves pillow image with a randomly generated filename
        in the directory set in the output_dir attribute.

        :param image: Pillow image
        :return: Path of saved image
        """
        filename = self.output_dir / Path(str(uuid.uuid4()) + ".jpg")
        image.save(filename)
        return filename

    @staticmethod
    def resize_image(image: Image, max_width: int) -> Image:
        """Resize image

        If the width of the image in pixels is larger than `max_width`,
        the image is resized to have max_width.

        :param image: Pillow image
        :param max_width: Maximum allowed width
        :return: Pillow image
        """
        if image.size[0] > max_width:
            ratio = max_width / float(image.size[0])
            height = int(ratio * float(image.size[1]))
            return image.resize((max_width, height), Image.NEAREST)
        else:
            return image

    @staticmethod
    def add_quote(image: Image, quote: QuoteModel):
        """Add a quote to the image as text

        :param image: Pillow image
        :param quote: QuoteModel object
        :return: Pillow image
        """
        image_width = image.size[0]
        font_size = int(image_width / 12)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(str(FONT_PATH), font_size)
        draw.text((10, 30), quote.body, fill="white", font=font)
        draw.text((21, 30 + font_size), "- " + quote.author, fill="white", font=font)
        return image

    def make_meme(
        self, image_path: Path, quote: QuoteModel, max_width: int = 500
    ) -> Path:
        """Create meme

        :param image_path: Path of image
        :param quote: QuoteModel object
        :param max_width: Maximum width
        :return: Path of output meme image
        """
        image = self.load_image(path=image_path)
        image = self.resize_image(image=image, max_width=max_width)
        image = self.add_quote(image=image, quote=quote)
        image_out_path = self.save_image(image)
        return image_out_path
