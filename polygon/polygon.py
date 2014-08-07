from __future__ import division
from random import uniform
from random import random

from settings import settings

from pyglet import clock, font
from pyglet.gl import glMatrixMode, glLoadIdentity, gluOrtho2D, glClear
from pyglet.gl import glTranslatef, glRotatef, glScalef
from pyglet.gl import glBegin, glEnd, glColor4f, glVertex2f
from pyglet.gl import GL_PROJECTION, GL_COLOR_BUFFER_BIT, GL_MODELVIEW, GL_TRIANGLES

# ----------------------------------------------------

class App(object):

    def __init__(self, window):
        self.win = window
        self.world = World()
        self.camera = Camera(self.win, zoom=100.0)
        self.hud = Hud(self.win)

        clock.set_fps_limit(settings.WINDOW['framerate'])

    def run(self):
        interval = 1/(settings.WINDOW['framerate']*2.0)
        clock.schedule_interval(self.update, interval)

    def update(self, dt):
    # while not self.win.has_exit:
        self.win.dispatch_events()

        self.world.tick()

        self.camera.worldProjection()
        self.world.draw()

        self.camera.hudProjection()
        self.hud.draw(len(self.world.ents))

        # clock.tick()
        # self.win.flip()
        pass

# ----------------------------------------------------

class Entity(object):

    def __init__(self, id, size, x, y, rot):
        self.id = id
        self.size = size
        self.x = x
        self.y = y
        self.rot = rot
        self.rand_colour1 = random()
        self.rand_colour2 = random()
        self.rand_colour3 = random()

    def draw(self):
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
        glRotatef(self.rot, 0, 0, 1)
        glScalef(self.size, self.size, 1.0)
        glBegin(GL_TRIANGLES)
        glColor4f(self.rand_colour1, self.rand_colour2, self.rand_colour3, 0.0)
        glVertex2f(0.0, 0.5)
        glColor4f(self.rand_colour3, self.rand_colour2, self.rand_colour1, 1.0)
        glVertex2f(0.2, -0.5)
        glColor4f(0.0, 0.0, 1.0, 1.0)
        glVertex2f(-0.2, -0.5)
        glEnd()

# ----------------------------------------------------

class World(object):

    def __init__(self):
        self.ents = {}
        self.nextEntId = 0
        clock.schedule_interval(self.spawnEntity, 0.25)

    def spawnEntity(self, dt):
        size = uniform(1.0, 100.0)
        x = uniform(-100.0, 100.0)
        y = uniform(-100.0, 100.0)
        rot = uniform(0.0, 360.0)
        ent = Entity(self.nextEntId, size, x, y, rot)
        self.ents[ent.id] = ent
        self.nextEntId += 1
        return ent

    def tick(self):
        for ent in self.ents.values():
            ent.rot += 10.0 / ent.size*3

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        for ent in self.ents.values():
            ent.draw()

# ----------------------------------------------------

class Camera(object):

    def __init__(self, win, x=0.0, y=0.0, rot=0.0, zoom=1.0):
        self.win = win
        self.x = x
        self.y = y
        self.rot = rot
        self.zoom = zoom

    def worldProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        widthRatio = self.win.width / self.win.height
        gluOrtho2D(
            -self.zoom * widthRatio,
            self.zoom * widthRatio,
            -self.zoom,
            self.zoom)

    def hudProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.win.width, 0, self.win.height)


# ----------------------------------------------------

class Hud(object):

    def __init__(self, win):
        helv = font.load('Helvetica', win.width / 25.0)
        self.text = font.Text(
            helv,
            'Hello, World!',
            x=win.width-100,
            y=20, #win.height / 2,
            halign=font.Text.CENTER,
            valign=font.Text.CENTER,
            color=(1, 1, 1, 0.5),
        )
        self.fps = clock.ClockDisplay()

    def draw(self, obj_num):
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        self.text.text = "%s objects" % obj_num
        self.text.draw()
        self.fps.draw()
