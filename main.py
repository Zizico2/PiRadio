#from gpiozero.pins.mock import MockFactory	
import os
os.environ['GPIOZERO_PIN_FACTORY'] = os.environ.get('GPIOZERO_PIN_FACTORY', 'mock')
import gpiozero
import vlc
from radioplayer import RadioPlayer
from gpiozero import Button, Device
from knob import Knob


#Device.pin_factory = MockFactory()

player = RadioPlayer()
RADIOCOMERCIALButton = Button(22) #insert pin
RFMButton = Button(21) #insert pin
volumeKnob = Knob(16,17,pin_button=7) # insert pins

RFMButton.when_pressed = player.changeToRFM
RFMButton.when_released = player.stopRFM
RADIOCOMERCIALButton.when_pressed = player.changeToRADIOCOMERCIAL
RADIOCOMERCIALButton.when_released = player.stopRADIOCOMERCIAL
volumeKnob.on_rotate_left(player.volumeDown)
volumeKnob.on_rotate_right(player.volumeUp)
volumeKnob.on_press(player.toggleMute)

#Device.pin_factory.pin(16).drive_low()
#Device.pin_factory.pin(16).drive_high()
#Device.pin_factory.pin(16).drive_low()
#Device.pin_factory.pin(16).drive_high()
#evice.pin_factory.pin(17).drive_low()
#Device.pin_factory.pin(17).drive_high()
#Device.pin_factory.pin(17).drive_low()
#Device.pin_factory.pin(17).drive_high()


#while(True):
	#pass


while True:
	inp = raw_input()

	if inp == "a": 
		player.changeToRFM()
	elif inp == "s": 
		player.changeToRADIOCOMERCIAL()
	elif inp == "x": 
		player.volumeUp()
	elif inp == "z": 
		player.volumeDown()
	elif inp == "<":
		player.toggleMute()
	else:
		player.stop()
		exit()
		


	

