from pyOpenBCI import OpenBCIGanglion
import filterlib as flt
import datetime


mac_adress = 'd2:b4:11:81:48:ad'

def print_raw(sample):
	smp = sample.channels_data[0]
	smp_flted = frt.filterIIR(smp, 0)
	with open("moje_dane.txt", "a") as myfile:
		myfile.write(f'{str(smp_flted)},{datetime.datetime.now().time()}\n')

board = OpenBCIGanglion(mac=mac_adress)

if __name__ == '__main__':
	# filtering in real time object creation
	frt = flt.FltRealTime()
	board.start_stream(print_raw)
