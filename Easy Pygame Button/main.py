import pygame as py
scrw, scrh = 1280, 720
scrsize = (scrw, scrh)
title = 'Button'
fps = 60
font = 'roboto.ttf'

py.init()
scr = py.display.set_mode(scrsize)
py.display.set_caption(title)
clock = py.time.Clock()
ft30 = py.freetype.Font(font, 30)
ft34 = py.freetype.Font(font, 34)

class Button:
	def __init__(self, surf, msg, coords, align='center'):
		self.surf = surf
		self.msg = msg
		self.x, self.y = coords
		self.align = align

		self.over = False

		if self.align == 'center': self.button = ft30.render_to(self.surf, (self.x-9*len(self.msg), self.y-20), self.msg, white)
		elif self.align == 'top': self.button = ft30.render_to(self.surf, (self.x-9*len(self.msg), self.y), self.msg, white)
		elif self.align == 'bottom': self.button = ft30.render_to(self.surf, (self.x-9*len(self.msg), self.y-40), self.msg, white)
		elif self.align == 'left': self.button = ft30.render_to(self.surf, (self.x, self.y-20), self.msg, white)
		elif self.align == 'right': self.button = ft30.render_to(self.surf, (self.x-18*len(self.msg), self.y-20), self.msg, white)
		elif self.align == 'topleft': self.button = ft30.render_to(self.surf, (self.x, self.y), self.msg, white)
		elif self.align == 'topright': self.button = ft30.render_to(self.surf, (self.x-18*len(self.msg), self.y), self.msg, white)
		elif self.align == 'bottomleft': self.button = ft30.render_to(self.surf, (self.x, self.y-40), self.msg, white)
		elif self.align == 'bottomright': self.button = ft30.render_to(self.surf, (self.x-18*len(self.msg), self.y-40), self.msg, white)

	def update(self):
		if self.button.collidepoint(py.mouse.get_pos()): self.over = True
		else: self.over = False
		if self.over and py.mouse.get_pressed()[0]: return True

	def draw(self):
		if self.align == 'center':
			if self.over: self.button = ft34.render_to(self.surf, (self.x-10*len(self.msg), self.y-22.5), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x-9*len(self.msg), self.y-20), self.msg, white)
		if self.align == 'top':
			if self.over: self.button = ft34.render_to(self.surf, (self.x-10*len(self.msg), self.y), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x-9*len(self.msg), self.y), self.msg, white)
		if self.align == 'bottom':
			if self.over: self.button = ft34.render_to(self.surf, (self.x-10*len(self.msg), self.y-45), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x-9*len(self.msg), self.y-40), self.msg, white)
		if self.align == 'left':
			if self.over: self.button = ft34.render_to(self.surf, (self.x, self.y-45), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x, self.y-40), self.msg, white)
		if self.align == 'right':
			if self.over: self.button = ft34.render_to(self.surf, (self.x-20*len(self.msg), self.y-45), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x-18*len(self.msg), self.y-40), self.msg, white)
		if self.align == 'topleft':
			if self.over: self.button = ft34.render_to(self.surf, (self.x, self.y), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x, self.y), self.msg, white)
		if self.align == 'topright':
			if self.over: self.button = ft34.render_to(self.surf, (self.x-20*len(self.msg), self.y), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x-18*len(self.msg), self.y), self.msg, white)
		if self.align == 'bottomleft':
			if self.over: self.button = ft34.render_to(self.surf, (self.x, self.y-45), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x, self.y-40), self.msg, white)
		if self.align == 'bottomright':
			if self.over: self.button = ft34.render_to(self.surf, (self.x-20*len(self.msg), self.y-45), self.msg, white)
			else: self.button = ft30.render_to(self.surf, (self.x-18*len(self.msg), self.y-40), self.msg, white)

white = (255,255,255)
black = (0,0,0)

exit = Button(scr, 'Exit', (scrw/2, scrh/2))
while not py.event.get(py.QUIT):
	scr.fill(black)
	if exit.update(): break
	exit.draw()
	py.display.flip()
	clock.tick(fps)
py.quit()
sys.exit()
