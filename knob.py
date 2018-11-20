from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Button, LED
from time import sleep
from sys import exit
Device.pin_factory = MockFactory()

class _Knob(object):
	RIGHT = None
	LEFT = None

	def __init__(self, 
		pin_right = None, pin_left = None, pin_button = None, 
		on_rotate_right = empty_func, on_rotate_left = empty_func, on_click = empty_func,
		right_pull_up = True, left_pull_up = True, button_pull_up = True, 
		pin_factory = None):
		print("hi")
		if pin_right == 2 and pin_left == None:
			exit("A knob must either rotate left or right (or both)! Please use a button instead.")
			
#def knob

def empty_func():
	pass