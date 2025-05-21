#from pydantic import BaseModel
from dataclasses import dataclass

head = """
<head>
  <meta content="text/html; charset=utf-8" http-equiv="content-type">
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta content="nobe-literate" name="generator">

  <title>a nobe document</title>
  
  <!-- favicon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2280%22>🐳</text></svg>">

  <!-- base styling -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/light.min.css">

  <!-- code higlighting -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script>hljs.highlightAll();</script>

  <!-- style for code higlighting -->
  <link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/pietroppeter/nimib/assets/atom-one-light.css'>

  <!-- latex  with katex -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.css" integrity="sha384-AfEj0r4/OFrOo5t7NnNe46zW/tFgW6x/bCJG8FqQCEo3+Aro6EYUG4+cU+KJWu/X" crossorigin="anonymous">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.js" integrity="sha384-g7c+Jr9ZivxKLnZTDUhnkOnsh30B4H0rpLUpJ4jAIKs4fnJI+sEnkvrMWph2EDg4" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/contrib/auto-render.min.js" integrity="sha384-mll67QQFJfxn0IYznZYonOWZ644AWYC+Pt2cHqMaRhXVrursRwvLnLaebdGIlYNa" crossorigin="anonymous" onload="renderMathInElement(document.body,{delimiters:[{left: '$$', right: '$$', display: true},{left: '$', right: '$', display: false}]});"></script>

  <!-- pyscript -->
  <link rel="stylesheet" href="https://pyscript.net/releases/2025.3.1/core.css">
  <script type="module" src="https://pyscript.net/releases/2025.3.1/core.js"></script>
  
</head>
"""

doc = """
<!DOCTYPE html>
<html lang="en-us">
{head}
<body>
<main>
{blocks}
</main>
</body>
</html>
"""

code = """
<pre><code class="python">{source}</code></pre>
<pre>{stdout}</pre>
"""

image = """
<img src="{url}", alt="{alt}">
"""


#class Theme(BaseModel):
@dataclass
class Theme:
    doc: str = doc
    head: str = head
    code: str = code
    image: str = image
