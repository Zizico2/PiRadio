from gpiozero import Button
from sys import exit



class Knob(object):
	right = None
	left = None
	button = None

	def __init__(self, 
		pin_right = None, pin_left = None, pin_button = None, 
		right_pull_up = True, left_pull_up = True, button_pull_up = True, 
		pin_fact = None):
		if pin_right == None and pin_left == None:
			exit("A knob must either rotate left or right (or both)! Please use a button instead.")
		if not pin_right == None:
			self.right = Button(pin_right, right_pull_up, pin_factory=pin_fact)
		if not pin_left == None:
			self.left = Button(pin_left, left_pull_up, pin_factory=pin_fact)
		if not pin_button == None:
			self.button = Button(pin_button)

	def on_rotate_left(self, func):
		self.left.when_pressed = func

	def on_rotate_right(self, func):
		self.right.when_pressed = func

	def on_press(self, func):
		self.button.when_pressed = func