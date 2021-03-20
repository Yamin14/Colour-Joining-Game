import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.clock import Clock
import random

class Game(Widget):
	def __init__(self, **kwargs):
		super(Game, self).__init__(**kwargs)
		self.colours = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
		self.blacklisted = []
		self.xl = [50, 600]
		self.yl = [250, 400, 550, 700, 850, 1000]
		self.c, self.d, self.p, self.q = [""]*6, [""]*6, [""]*6, [""]*6
		self.connected = [False]*6
		self.moving = [False]*6
		self.radius = 50
		
		#background
		with self.canvas:
			Color(rgb=(0.3, 0.3, 0.3))
			Rectangle(size=(800, 1500))
			
		#title
		title = Label(text="Colour Joining", pos=(330, 1170), font_size=100, color=(0.0, 1, 0.75, 1))
		self.add_widget(title)
		
		#win
		self.win = Label(text="", pos=(310, 70), font_size=100, color=(0, 1, 0, 1))
		self.add_widget(self.win)
			
		self.play()
		
	def play(self):
		
		#drawing the circles
		with self.canvas:
			for i in range(6):
				self.c[i] = (self.colours[random.randint(0, 5)])
				self.p[i] = (self.yl[i])
			
				while self.c[i] in self.blacklisted:
					self.c[i] = self.colours[random.randint(0, 5)]
				while self.p[i] in self.blacklisted:
					self.p[i] = self.yl[i]
				
				self.blacklisted.append(self.c[i])
				self.blacklisted.append(self.p[i])
				
				Color(rgb=self.c[i])
				Ellipse(size=(self.radius*2, self.radius*2), pos=(self.xl[0], self.p[i]))
				
			self.blacklisted = []				
			for i in range(6):
				self.d[i] = self.colours[random.randint(0, 5)]
				self.q[i] = self.yl[i]
			
				while self.d[i] in self.blacklisted:
					self.d[i] = self.colours[random.randint(0, 5)]
				while self.q[i] in self.blacklisted:
					self.q[i] = self.yl[i]
				
				self.blacklisted.append(self.d[i])
				self.blacklisted.append(self.q[i])
				
				Color(rgb=self.d[i])
				Ellipse(size=(self.radius*2, self.radius*2), pos=(self.xl[1], self.q[i]))
				
	def on_touch_down(self, touch):
		if touch.pos[0] >= self.xl[0] and touch.pos[0] <= self.xl[0]+(self.radius*2):
			for i in range(6):
				if touch.pos[1] >= self.yl[i] and touch.pos[1] <= self.yl[i]+(self.radius*2) and self.connected[i] == False:
					self.moving[i] = True
					self.const = (self.xl[0]+self.radius, self.yl[i]+self.radius)
					self.col = self.c[i]
					self.flag = True

	def on_touch_move(self, touch):
		for i in range(6):
			if touch.pos[0] >= self.xl[1] and touch.pos[0] <= self.xl[1]+(self.radius*2):
				for j in range(6):
					if touch.pos[1] >= self.q[j] and touch.pos[1] <= self.q[j]+(self.radius*2):
						if self.c[i] == self.d[j]:
							self.connected[i] = True
							self.moving[i] = False
			
			if self.moving[i] == True:	
				with self.canvas:
					Color(rgb=self.col)
					if self.connected[i] == False:
						Line(points=[self.const, (touch.pos[0], touch.pos[1])], width=5)
						
		w = True
		for i in self.connected:
			if i == False:
				w = False

		if w == True:
			self.win.text = "Win!"

	def on_touch_up(self,touch):
		self.moving = [False]*6
		
class MyApp(App):
	def build(self):
		return Game()
		
if __name__ == "__main__":
	MyApp().run()
