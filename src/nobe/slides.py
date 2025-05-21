from nobe import Block, Doc, Text, theme
from nobe.theme import Theme



class Presentation(Doc):
    pass


slide_html = """
<section>
{blocks}
</section>
"""

class SlidesTheme(Theme):
    slide: str = slide_html


class Slide(Block):
    blocks: list[Block] = []

    def add(self, blk: Block):
        self.blocks.append(blk)

    def to_html(self) -> str:
        blocks = "\n".join([blk.to_html() for blk in self.blocks])
        print("here")
        print(type(theme)) # should be SlidesTheme when called from presentation.py but it is not!
        return theme.slide.format(blocks=blocks)


def slide(doc: Presentation, text: str):
    blk = Text(text=text)
    slide = Slide()
    slide.add(blk)
    doc.add(slide)

Presentation.slide = slide
