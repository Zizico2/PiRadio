import vlc
from enum import Enum
from sys import exit

class _Station(Enum):
	RADIOCOMERCIAL = vlc.Media("http://mcrscast.mcr.iol.pt/comercial.mp3") #RADIO COMERCIAL
	RFM = vlc.Media("http://19593.live.streamtheworld.com:3690/RFMAAC_SC?DIST=TuneIn&TGT=TuneIn&maxServers=2") #RFM

class RadioPlayer():
	player  = vlc.MediaPlayer("")
	player.audio_set_volume(50)

	def _shouldChangeStation(self, nextStation):
		currentStation = self.player.get_media()
		return (currentStation == None or not currentStation.get_mrl() == nextStation.get_mrl())

	def _changeStation(self, nextStation):
		player = self.player
		if self._shouldChangeStation(nextStation):
			volume = player.audio_get_volume()
			player.set_media(nextStation)
			player.audio_set_volume(volume)	
			player.play()

	def _changeVolume(self, i):
		player = self.player
		if player.audio_get_volume() + i < 100 and player.audio_get_volume() + i > 0:
			player.audio_set_volume(player.audio_get_volume() + i)
		print(self.player.audio_get_volume())

	def volumeUp(self):
		self._changeVolume(1)
		

	def volumeDown(self):
		self._changeVolume(-1)

	def toggleMute(self):
		self.player.audio_toggle_mute()
		print(self.player.audio_get_volume())

	def changeToRADIOCOMERCIAL(self):
		#self._changeStation(_Station.RADIOCOMERCIAL)
		self._changeStation(_Station.RADIOCOMERCIAL.value)


	def changeToRFM(self):
		#self._changeStation(_Station.RFM)
		self._changeStation(_Station.RFM.value)

	def stopRADIOCOMERCIAL(self):
		player = self.player
		#if player.get_media().get_mrl == self._changeStation(_Station.RADIOCOMERCIAL)
		if player.get_media().get_mrl == self._changeStation(_Station.RADIOCOMERCIAL.value)
			player.stop()	

	def stopRFM(self):
		player = self.player
		#if player.get_media().get_mrl == self._changeStation(_Station.RFM)
		if player.get_media().get_mrl == self._changeStation(_Station.RFM.value)
			player.stop()

	def pause(self):
		self.player.pause()

	def stop(self):
		self.player.stop()
		exit()






































player = vlc.MediaPlayer()