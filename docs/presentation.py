import nobe
from nobe.slides import Presentation, SlidesTheme

nb = Presentation()
nobe.theme = SlidesTheme()
nb.slide("""
# title
         
content
""")

nb.slide("""
another slide with code
         
```python
print("hello")
```
""")

nb.save()
