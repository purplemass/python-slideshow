# ----------------------------------------------------
# CONFIG

photos_folder = "//sayfromage/photos_animated_366x549/"
# photo = "Say_Fromage-76.jpg"
photo_id = 1

# ----------------------------------------------------

import sys
sys.path.insert(0, './lib')

import pyglet

# ----------------------------------------------------

pyglet.resource.path = [photos_folder]
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
foreground_image = pyglet.image.load('//sayfromage/themes/background4.jpg')
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

"""

# ----------------------------------------------------

from pyglet import clock
dt = clock.tick()
print dt
print 'FPS is %f' % clock.get_fps()

# ----------------------------------------------------

window = pyglet.window.Window(visible=False)
window.set_visible()

# ----------------------------------------------------

# print all events to console
window.push_handlers(pyglet.window.event.WindowEventLogger())

# ----------------------------------------------------

from pyglet.window import mouse

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        msg = "LEFT"
    elif button == mouse.RIGHT:
        msg = "RIGHT"
    else:
        msg = ""
    print 'The %s mouse button was pressed at (%s, %s)' % (msg, x, y)

# ----------------------------------------------------

from pyglet.window import key

@window.event
def on_key_press(symbol, modifiers):
    print 'A key was pressed'
    if symbol == key.A:
        print 'The "A" key was pressed.'
    elif symbol == key.LEFT:
        print 'The left arrow key was pressed.'
    elif symbol == key.ENTER:
        print 'The enter key was pressed.'

# ----------------------------------------------------

NOT SURE ABOUT THIS ONE:

event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_window_close(window):
    print 'pp'
    event_loop.exit()

http://www.pyglet.org/doc/api/frames.html?page=http://www.pyglet.org/doc/api/pyglet.gl.Config-class.html

# ----------------------------------------------------

http://tareqalam.com/2013/12/14/importerror-entry-point-console_scripts-easy_install-not-found/
http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html#uninstalling-py2app-0-2-x-or-earlier

sudo /Library/Frameworks/Python.framework/Versions/2.7/bin/py2applet --make-setup bob.py -i lib/
python setup.py py2app -A

# ----------------------------------------------------

"""