from settings import settings

from pyglet import window, app

from slideshow import App as Slideshow
from polygon import App as Polygon

# ----------------------------------------------------

if __name__ == '__main__':
    win = window.Window(
        width=settings.WINDOW['width'],
        height=settings.WINDOW['height'],
        fullscreen=settings.WINDOW['fullscreen'],
        vsync=settings.WINDOW['vsync']
    )
    win.clear()

    slideshow = Slideshow(win)
    slideshow.run()

    polygon = Polygon(win)
    polygon.run()

    app.run()