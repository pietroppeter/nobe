import nobe
from nobe import Block, Doc, Text
from nobe.theme import Theme
    
slide_default = """
<section>
{blocks}
</section>
"""


class SlidesTheme(Theme):
    head: str = ""
    slide: str = slide_default

class Slide(Block):
    blocks: list[Block] = []

    def add(self, blk: Block):
        self.blocks.append(blk)

    def to_html(self) -> str:
        blocks = "\n".join([blk.to_html() for blk in self.blocks])
        print("here")
        print(
            type(nobe.theme)
        )  # should be SlidesTheme when called from presentation.py but it is not!
        return nobe.theme.slide.format(blocks=blocks)


class Presentation(Doc):
    pass


def slide(doc: Presentation, text: str):
    blk = Text(text=text)
    slide = Slide()
    slide.add(blk)
    doc.add(slide)


Presentation.slide = slide
