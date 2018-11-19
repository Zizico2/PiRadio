import vlc
import sys
import atexit
def main():
	radiostation = vlc.Media("http://mcrscast.mcr.iol.pt/comercial.mp3")
	radiostation2 = vlc.Media("http://19613.live.streamtheworld.com:3690/RFMAAC_SC?DIST=TuneIn&TGT=TuneIn&maxServers=2")
	nextStation = ""
	player = vlc.MediaPlayer()
	player.audio_set_volume(50)
	while True:
		if shouldChangeStation(player.get_media(), nextStation): 
			changeStation(player, nextStation)
		name = raw_input()
		if name == "a":
			nextStation = radiostation
		elif name =="s":
			nextStation = radiostation2
		elif name == "p":
			player.audio_set_volume(100)
		elif name == "l":
			sys.exit()	
		
	
def changeStation(player, nextStation):
	player.set_media(nextStation)
	player.play()

def shouldChangeStation(currentStation, nextStation):
	return not nextStation == "" and (currentStation == None or not currentStation.get_mrl() == nextStation.get_mrl())

def clearPlayers():
	main.player.stop()

if __name__== "__main__":
	main()
	atexit.register(clearPlayers)

	

