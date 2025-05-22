import nobe
from nobe import Block, Doc, Text
from nobe.theme import Theme

slide_default = """
<section>
{blocks}
</section>
"""

reveal_version = "5.0.4"

head_default = """
<head>
  <meta content="text/html; charset=utf-8" http-equiv="content-type">

    <!-- reveal CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{reveal_version}/reveal.min.css" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{reveal_version}/theme/{reveal_theme}.min.css" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{reveal_version}/plugin/highlight/monokai.min.css" crossorigin="anonymous" referrerpolicy="no-referrer" />

</head>

"""

doc_default = """
<!DOCTYPE html>
<html>
{head}
<body>
<div class="reveal">
  <div class="slides">
    {blocks}
  </div>
</div>

<!-- reveal JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{reveal_version}/reveal.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{reveal_version}/plugin/highlight/highlight.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{reveal_version}/plugin/notes/notes.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{reveal_version}/plugin/math/math.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script>
  Reveal.initialize({{
    plugins: [ 
      RevealHighlight,
      RevealNotes,
      RevealMath.KaTeX,
    ],
  }});
</script>
</body>
</html>
"""


class Presentation(Doc):
    reveal_theme: str = "simple"

    def to_html(self) -> str:
        head = nobe.theme.head.format(
            reveal_version=reveal_version, reveal_theme=self.reveal_theme
        )
        blocks = "\n".join([blk.to_html() for blk in self.blocks])
        doc = nobe.theme.doc.format(
            head=head, blocks=blocks, reveal_version=reveal_version
        )
        return doc


class SlidesTheme(Theme):
    doc: str = doc_default
    head: str = head_default
    slide: str = slide_default


class Slide(Block):
    blocks: list[Block] = []

    def add(self, blk: Block):
        self.blocks.append(blk)

    def to_html(self) -> str:
        blocks = "\n".join([blk.to_html() for blk in self.blocks])
        return nobe.theme.slide.format(blocks=blocks)


def slide(doc: Presentation, text: str):
    blk = Text(text=text)
    slide = Slide()
    slide.add(blk)
    doc.add(slide)


Presentation.slide = slide
