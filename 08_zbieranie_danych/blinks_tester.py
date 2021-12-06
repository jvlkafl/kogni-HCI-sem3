from pyOpenBCI import OpenBCIGanglion
import filterlib as flt
import time
import os


mac_adress = 'd2:b4:11:81:48:ad'

def print_raw(sample):
	smp = sample.channels_data[0]
	smp_flted = frt.filterIIR(smp, 0)
	if smp_flted < -40000:
		print("BLINK")
		time.sleep(0.1)
		os.system('cls' if os.name == 'nt' else 'clear')
		
board = OpenBCIGanglion(mac=mac_adress)

if __name__ == '__main__':
	# filtering in real time object creation
	os.system('cls' if os.name == 'nt' else 'clear')
	frt = flt.FltRealTime()
	board.start_stream(print_raw)
