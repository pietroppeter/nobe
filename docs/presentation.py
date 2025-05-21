from nobe import theme
from nobe.slides import Presentation, SlidesTheme

nb = Presentation()
theme = SlidesTheme()
print(type(theme))

nb.slide("""
# title
         
content
""")

nb.save()
