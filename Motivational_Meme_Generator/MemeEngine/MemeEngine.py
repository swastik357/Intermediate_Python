"""Takes an output path, selects a random image and quote, processes them\
and saves the generated meme to the output path and returns\
the path to meme."""

import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """This class takes in output path, makes meme and returns path to meme."""

    def __init__(self, output_path):
        """Initialize instance of class."""
        self.output_path = output_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create meme with provided text and author."""
        try:
            image = Image.open(img_path)
        except Exception as e:
            print(f'Exception raised: {e}')
        else:
            if width:
                height = int(width*float(image.size[1])/float(image.size[0]))
                image = image.resize((width, height), Image.NEAREST)

            if text and author:
                img_txt = f'{text}\n- {author}'
                draw = ImageDraw.Draw(image)
                imh = int(height/20)
                font = ImageFont.truetype('./font/LilitaOne-Regular.ttf', imh)
                draw.text((10, 10), img_txt, font=font, fill='white')

            op = f'{self.output_path}/{author}{random.randint(0, 10000)}.jpeg'

            image.save(op)
            print(f"Meme saved to {op}")
            return op
