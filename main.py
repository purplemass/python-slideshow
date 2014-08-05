# ----------------------------------------------------

from settings import settings
import pyglet

# ----------------------------------------------------

photo_id = 1

# ----------------------------------------------------

pyglet.resource.path = [settings.PHOTOS_FOLDER]
pyglet.resource.reindex()

# window = pyglet.window.Window()
window = pyglet.window.Window(366, 549)
fps_display = pyglet.clock.ClockDisplay()
# window.set_fullscreen(True)

label = pyglet.text.Label(
    "Say_Fromage-%s.jpg" % photo_id,
    font_name='Helvetica',
    font_size=15,
    color=(255, 255, 0, 255),
    x=window.width/2,
    y=20, #(window.height/2) + 20,
    anchor_x='center',
    anchor_y='center'
)

# image = pyglet.resource.image('background1.jpg') # same resource/local
foreground_image = pyglet.image.load(settings.FOREGROUND_IMAGE)
background_image = pyglet.resource.image("Say_Fromage-%s.jpg" % photo_id)

# background_image.anchor_x = (background_image.width/2)
# background_image.anchor_y = (background_image.height/2)
# print dir(label)

# ----------------------------------------------------

@window.event
def on_show():
    print "SHOW!"

@window.event
def on_hide():
    print "HIDE!"

x = 0
speed = 20
@window.event
def on_draw():
    global x

    window.clear()
    background_image = pyglet.resource.image("Say_Fromage-%s.jpg" % photo_id)
    background_image.blit(0, 0)
    label.draw()
    foreground_image.blit(x, 0)


    fps_display.draw()

def update(dt):
    global x, speed, photo_id

    x = x + speed
    if x > (window.width+window.width/5):
        speed = -1 * speed
    elif x < 0:
        speed = -1 * speed
        photo_id = photo_id + 1
        label.text = "Say_Fromage-%s.jpg" % photo_id

# ----------------------------------------------------

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()

# ----------------------------------------------------
