# nobe

Nobe (short for [nota bene](https://en.wikipedia.org/wiki/Nota_bene))
is a literate programming tool to publish html documents from python code.

Install it (`pip install` or `uv add`) as [nobe-literate](https://pypi.org/project/nobe-literate/), import it as `nobe`.

You put your code in a file like [docs/example.py](docs/example.py),
you run it like a normal python script (e.g. `uv run python example.py`)
and you get out [example.html](https://pietroppeter.github.io/nobe/example.html).

One way to try this out is:

```
curl -O https://raw.githubusercontent.com/pietroppeter/nobe/refs/heads/main/docs/example.py
uv run --with nobe-literate example.py
open example.html
```

## slides

Thanks to [reveal.js] you can also use nobe to produce slides: here is an example [presentation](https://pietroppeter.github.io/nobe/presentation.html).
Check the source in [docs/presentation.py](docs/presentation.py) to understand how to acquire this power

## origin

It starts as [nimib.py] without [nim] but the goal is to experiment freely with a [nimib]-like python api.

[nimib]: https://github.com/pietroppeter/nimib
[nimib.py]: https://github.com/nimib-land/nimib.py
[nim]: https://nim-lang.org/
[reveal.js]: https://revealjs.com/
