import nobe
from nobe.slides import Presentation, SlidesTheme

nb = Presentation()
nobe.theme = SlidesTheme()
hey = SlidesTheme()
nb.slide("""
# title
         
content
""")

nb.save()
