import vlc
from radioplayer import RadioPlayer
from gpiozero import Button
from knob import Knob

player = RadioPlayer()
RADIOCOMERCIALButton = Button() #insert pin
RFMButton = Button() #insert pin
volumeKnob = Knob() # insert pins

RFMButton.when_pressed = player.changeToRFM
RADIOCOMERCIALButton.when_pressed = player.changeToRADIOCOMERCIAL
volumeKnob.on_rotate_left = player.volumeDown
volumeKnob.on_rotate_right = player.volumeUp
#volumeKnob.on_rotate_press player.toggleMute


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


	

