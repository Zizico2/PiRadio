from gpiozero.pins.mock import MockFactory	
import vlc
from radioplayer import RadioPlayer
from gpiozero import Button
from knob import Knob


Device.pin_factory = MockFactory()

player = RadioPlayer()
RADIOCOMERCIALButton = Button(22) #insert pin
RFMButton = Button(21) #insert pin
volumeKnob = Knob(16,17) # insert pins

RFMButton.when_pressed = player.changeToRFM
RADIOCOMERCIALButton.when_pressed = player.changeToRADIOCOMERCIAL
volumeKnob.on_rotate_left = player.volumeDown
volumeKnob.on_rotate_right = player.volumeUp
#volumeKnob.on_rotate_press player.toggleMute

Device.pin_factory.pin(22).drive_low()



#while True:
#	inp = raw_input()
#
#	if inp == "a": 
#		player.changeToRFM()
#	elif inp == "s": 
#		player.changeToRADIOCOMERCIAL()
#	elif inp == "x": 
#		player.volumeUp()
#	elif inp == "z": 
#		player.volumeDown()
#	else:
#		exit()
#		player.stop()


	

