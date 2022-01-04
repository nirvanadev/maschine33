# name=Maschine 33 Script

# This is my custom MIDI script for Maschine MK2 in FLStudio 20.9

import transport
import mixer
import ui
import midi

# Globals
Zoom_Axis = 1

class TSimple():
	def OnMidiMsg(self, event):
		event.handled = True
		global Zoom_Axis
		if event.midiId == midi.MIDI_CONTROLCHANGE:
			if event.midiChan == 0:
				# print(event.data1)
				# print(event.data2)
				#Track Volume (Top Knobs)
				if event.data1 >= 1 and event.data1 <= 32:
					ui.showWindow(midi.widMixer)
					if event.data2 == 127:
						mixer.setTrackVolume(event.data1, mixer.getTrackVolume(event.data1) - 0.003)
					if event.data2 == 1:
						mixer.setTrackVolume(event.data1, mixer.getTrackVolume(event.data1) + 0.003)
				#Track Select (Top Buttons)
				elif event.data1 >= 41 and event.data1 <= 72:
					sel = event.data1 - 40
					ui.showWindow(midi.widMixer)
					mixer.setTrackNumber(sel)
				#Show Playlist
				elif event.data1 == 73:
					ui.showWindow(midi.widPlaylist)
				#Show Channel Rack
				elif event.data1 == 74:
					ui.showWindow(midi.widChannelRack)
				#Show Piano Roll
				elif event.data1 == 75:
					ui.showWindow(midi.widPianoRoll)
				#Show Piano Roll
				elif event.data1 == 76:
					ui.showWindow(midi.widMixer)
				# Toggle the Zoom Axis Global (Click big wheel)
				elif event.data1 == 78:
					if event.data2 == 127:
						Zoom_Axis = 0
					else:
						Zoom_Axis = 1
				# Handle Zoom
				elif event.data1 == 77:
					if event.data2 == 127:
						if Zoom_Axis == 0:
							ui.jog2(-1)
						else:
							ui.horZoom(-1)
					if event.data2 == 1:
						if Zoom_Axis == 0:
							ui.jog2(+1)
						else:
							ui.horZoom(+1)
				#Play/Pause
				elif event.data1 == 93:
					transport.globalTransport(midi.FPT_Play, 1)
				#Stop
				elif event.data1 == 94:
					transport.globalTransport(midi.FPT_Stop, 1)
				#Record
				elif event.data1 == 95:
					transport.globalTransport(midi.FPT_Record, 1)
		else:
			event.handled = False
Simple = TSimple()

def OnMidiMsg(event):
	Simple.OnMidiMsg(event)