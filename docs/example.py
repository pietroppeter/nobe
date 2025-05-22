import nobe

nb = nobe.Doc()

nb.text("# Example document\nmade with [nobe](https://github.com/pietroppeter/nobe)🐳")

nb.text("## Capture output")
nb.text(
    "Output of commands is captured (two ways to declare a code block, check in source code)"
)

nb.code(lambda: print("hi"))


@nb.code
def _():
    print("hello")


nb.text("## Accessing variables in blocks")

nb.text("Declare a variable in one block")


@nb.code
def _():
    global x
    x = 0


nb.text("change it in another block and print it")


@nb.code
def _():
    global x
    x += 1
    print(x)


nb.text("do it 3 times (look for the loop in source code)")

for _ in range(3):

    @nb.code
    def _():
        global x
        x += 1
        print(x)


nb.text(
    "You have to know Python scoping in functions and use global keyword to do the above"
)

nb.text("## Image")

nb.code(
    lambda: nb.image(
        url="https://images.unsplash.com/photo-1565374587194-89003eaebb5b?q=80&w=3271&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        alt="Mountain background in the dolomites with a small hut and two out of focus cyclists climbing on a road",
    )
)

nb.text(
    "Photo from [unsplash](https://unsplash.com/it/foto/casa-sullerba-verde-vicino-a-brown-mountain-88Pbp37FjSs)."
)

nb.text("## Latex")

nb.text(
    r"""
Latex support is available thanks to [katex](https://katex.org/)
with single `$` delimiting inline latex and double `$$` delimit formulas in display mode.
        
As an example of inline mode, the [Euler's formula](https://en.wikipedia.org/wiki/Euler%27s_formula)
is given by $e^{i \pi} + 1 = 0$ where $e$ is the base of the natural logarithm and $i$ is the imaginary unit.

As an example of display mode, here is a convergent [geometric series](https://en.wikipedia.org/wiki/Geometric_series):

$$
1 + \\frac{1}{2} + \\frac{1}{4} + \cdots = \sum_{k=0}^{+\infty} \\frac{1}{2^k} = 2
$$        
"""
    # note that I have to use a double back slash to avoid typing the "form feed" escape character
    # also I am using the raw string literal or \p would be marked as invalid escape sequence
)

nb.text("## Pyscript")

nb.text("Pyscript can be used. The default version loaded is:")
nb.html("""
<mpy-script>
import sys
from pyscript import display

display(sys.version)
</mpy-script>        
""")

nb.text("Here is an example of a button adding emojis:")
nb.html("""
<mpy-script>
from pyscript import document

def add_emoji(event):
    output = document.createElement("span")
    output.innerHTML = "🐳"
    container = document.querySelector("div#emoji-container")
    container.appendChild(output)

</mpy-script>        
""")

nb.html('<button mpy-click="add_emoji">More emojis!</button><br/>')
nb.html('<div id="emoji-container"></div>')

nb.text(f"""## Source code

This is the source code for this document:
        
```py
{nb.source.replace("```", "````")}
```
                
""")

nb.save()

# nb.dump_json() # broken
