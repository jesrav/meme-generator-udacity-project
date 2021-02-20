from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from QuoteEngine.QuoteModel import QuoteModel


class MemeEngine:

    allowed_extensions = ['.jpg', '.png']

    def __init__(self, output_dir):
        self.output_dir = output_dir

    @classmethod
    def load_image(cls, path: Path) -> Image:
        if not path.exists():
            raise ValueError("Image does not exist.")
        if path.suffix not in cls.allowed_extensions:
            raise ValueError(
                f"Image file type not supported. Supported types are: {cls.allowed_extensions}"
            )
        return Image.open(str(path))

    @classmethod
    def save_image(cls, image: Image) -> Path:
        pass

    @staticmethod
    def resize_image(image: Image, max_width: int) -> Image:
        if image.size[0] > max_width:
            ratio = max_width / float(image.size[0])
            height = int(ratio * float(image.size[1]))
            return image.resize((max_width, height), Image.NEAREST)
        else:
            return image

    @staticmethod
    def add_quote(image: Image, quote: QuoteModel):
        image_width = image.size[0]
        font_size = int(image_width/5)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("src/fonts/Alviena-Regular.ttf", font_size)
        draw.text((10, 30), quote.body, fill='white', font=font)
        draw.text((21, 30 + font_size), "- " + quote.author, fill='white', font=font)
        return image

    def make_meme(
            self,
            image_path: Path,
            quote: QuoteModel,
            max_width: int = 500
    ) -> Path:
        image = self.load_image(path=image_path)
        image = self.resize_image(image=image, max_width=max_width)
        image = self.add_quote(image=image, quote=quote)
        return image


meme = MemeEngine("src/lol")
im = meme.make_meme(
    image_path=Path("src/_data/photos/dog/xander_1.jpg"),
    quote=QuoteModel(author="Jes", body="Bab af!!!"),
    max_width=200
)

im.save("test.jpg")