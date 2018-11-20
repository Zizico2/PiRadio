import vlc
import sys
import atexit
from enum import Enum
#import knob


class Station(Enum):
	NONE = vlc.Media("")
	RADIOCOMERCIAL = vlc.Media("http://mcrscast.mcr.iol.pt/comercial.mp3") #RADIO COMERCIAL
	RFM = vlc.Media("http://19613.live.streamtheworld.com:3690/RFMAAC_SC?DIST=TuneIn&TGT=TuneIn&maxServers=2") #RFM

def main():
	nextStation = initNextStation()
	player = initPlayer()
	while True:
		name = input()
		if name == "a":
			nextStation = Station.RADIOCOMERCIAL.value
		elif name == "s":
			nextStation = Station.RFM.value
		#else:
		#	nextStation = Station.NONE.value
		
		if name == "x":
			changeVolume(player, 1)
		elif name == "z":
			changeVolume(player, -1)
		elif name == "l":
			sys.exit()	
		
		if shouldChangeStation(player.get_media(), nextStation): 
			changeStation(player, nextStation)
		
	
def changeStation(player, nextStation):
	volume = player.audio_get_volume()
	player.set_media(nextStation)
	player.play()
	player.audio_set_volume(volume)

def changeVolume(player, i):
	player.audio_set_volume(player.audio_get_volume() + i)

def shouldChangeStation(currentStation, nextStation):
	return (currentStation == None or not currentStation.get_mrl() == nextStation.get_mrl())

def clearPlayer():
	main.player.stop()

def initPlayer():
	player = vlc.MediaPlayer()
	player.audio_set_volume(50)
	player.play()
	return player

def initNextStation():
	return Station.NONE.value
	

if __name__== "__main__":
	main()
	atexit.register(clearPlayers)



	

