import inspect
import io
import json
import sys
from typing import Callable, Optional

import markdown
from pydantic import BaseModel

from nobe import source
from nobe.theme import Theme

theme = Theme()


class Block(BaseModel):
    def to_json(self) -> str:
        return self.model_dump_json()


class Doc(Block):
    filename: str = ""
    source: str = ""
    blocks: list[Block] = []

    def model_post_init(self, __context):
        self.filename = inspect.stack()[-1].filename
        with open(self.filename, "r") as f:
            self.source = f.read()

    def add(self, blk: Block):
        self.blocks.append(blk)

    def to_json(self) -> str:
        return json.dumps([blk.to_json() for blk in self.blocks])

    def to_html(self) -> str:
        head = theme.head
        blocks = "\n".join([blk.to_html() for blk in self.blocks])
        return theme.doc.format(head=head, blocks=blocks)

    def save(self):
        filename = self.filename.replace(".py", ".html")
        with open(filename, "w") as f:
            f.write(self.to_html())


class Text(Block):
    text: str = ""

    def to_html(self) -> str:
        return markdown.markdown(self.text, extensions=["fenced_code"])


def text(doc: Doc, text: str):
    doc.add(Text(text=text))


Doc.text = text


class Code(Block):
    callable: Optional[Callable] = None
    source: str = ""
    stdout: str = ""

    def to_html(self) -> str:
        return theme.code.format(source=self.source, stdout=self.stdout)


def code(doc: Doc, callable: Callable):
    blk = Code(callable=callable)
    blk.source = source.getsource(callable)

    _stdout = sys.stdout
    sys.stdout = io.StringIO()

    blk.callable()

    blk.stdout = sys.stdout.getvalue()
    sys.stdout = _stdout

    doc.add(blk)


Doc.code = code


class Image(Block):
    url: str = ""
    alt: str = ""

    def to_html(self) -> str:
        return theme.image.format(url=self.url, alt=self.alt)


def image(doc: Doc, url: str, alt=""):
    doc.add(Image(url=url, alt=alt))


Doc.image = image


class Html(Block):
    html: str = ""

    def to_html(self) -> str:
        return self.html


def html(doc: Doc, html: str):
    doc.add(Html(html=html))


Doc.html = html
