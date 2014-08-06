
# ----------------------------------------------------

from pyglet import clock
dt = clock.tick()
print dt
print 'FPS is %f' % clock.get_fps()

# ----------------------------------------------------

import pyglet

window = pyglet.window.Window(visible=False)
window.set_visible()

# ----------------------------------------------------

# print all events to console
window.push_handlers(pyglet.window.event.WindowEventLogger())

# ----------------------------------------------------

image = pyglet.resource.image('background1.jpg') # same resource/local
image_x = (image.width/2)
image_y = (image.height/2)

@window.event
def on_draw():
    window.clear()
    image = pyglet.resource.image("Say_Fromage.jpg")
    image.blit(0, 0)

@window.event
def on_show():
    print "SHOW!"

@window.event
def on_hide():
    print "HIDE!"

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

# NOT SURE ABOUT THIS ONE:

event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_window_close(window):
    print 'pp'
    event_loop.exit()

# http://www.pyglet.org/doc/api/frames.html?page=http://www.pyglet.org/doc/api/pyglet.gl.Config-class.html

# ----------------------------------------------------

# http://tareqalam.com/2013/12/14/importerror-entry-point-console_scripts-easy_install-not-found/
# http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html#uninstalling-py2app-0-2-x-or-earlier

# sudo /Library/Frameworks/Python.framework/Versions/2.7/bin/py2applet --make-setup bob.py -i lib/
# python setup.py py2app -A

# ----------------------------------------------------
