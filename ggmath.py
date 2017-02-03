# ggmath - ggame extensions for geometry and mathematics in the browser

from ggame import Color, LineStyle, LineAsset, Sprite, App

ls = LineStyle(3, Color(0x000000, 1))
la = LineAsset(100, 100, ls)
sp = Sprite(la, (100,100))

ap = App()
ap.run()