import vlc
from mediaplayer import RadioPlayer
from sys import exit

player = RadioPlayer()

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
	else:
		exit()
		player.stop()


	

