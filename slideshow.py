from settings import settings

import pyglet

# ----------------------------------------------------

class App(object):

    photo_id = 1

    xpos = 0
    xspeed = 10

    def __init__(self):
        pyglet.resource.path = [settings.PHOTOS_FOLDER]
        pyglet.resource.reindex()

        self.win = pyglet.window.Window(
            settings.WINDOW['width'],
            settings.WINDOW['height']
        )
        self.win.set_fullscreen(
            settings.WINDOW['fullscreen']
        )
        self.win.clear()
        self.fps_display = pyglet.clock.ClockDisplay()

        self.label = pyglet.text.Label(
            "Say_Fromage-%s.jpg" % self.photo_id,
            font_name='Helvetica',
            font_size=15,
            color=(255, 255, 0, 255),
            x=self.win.width/2,
            y=20,
            anchor_x='center',
            anchor_y='center'
        )

        self.foreground_image = pyglet.image.load('//sayfromage/themes/background4.jpg')
        self.background_image = pyglet.resource.image("Say_Fromage-%s.jpg" % self.photo_id)

        self.win.on_show = self.on_show
        self.win.on_hide = self.on_hide
        self.win.draw = self.draw

    def run(self):
        interval = 1/120.0
        pyglet.clock.schedule_interval(self.update, interval)
        pyglet.clock.schedule_interval(self.draw, interval)
        pyglet.app.run()

    def on_show(self):
        print "SHOW!"

    def on_hide(self):
        print "HIDE!"

    def draw(self, dt):
        self.background_image = pyglet.resource.image("Say_Fromage-%s.jpg" % self.photo_id)
        self.background_image.blit(0, 0)
        self.label.draw()
        self.foreground_image.blit(self.xpos, 0)
        self.fps_display.draw()

    def update(self, dt):
        self.xpos = self.xpos + self.xspeed
        if self.xpos > (self.win.width+self.win.width/5):
            self.xspeed = -1 * self.xspeed
        elif self.xpos < 0:
            self.xspeed = -1 * self.xspeed
            self.photo_id = self.photo_id + 1
            self.label.text = "Say_Fromage-%s.jpg" % self.photo_id
