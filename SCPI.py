import time
import visa
import pyvisa
import sys

rm = pyvisa.ResourceManager()
#print(rm.list_resources())

oscilloscope = rm.open_resource('USB0::0x05E6::0x6510::04407440::INSTR')

print(str(sys.argv))

if sys.argv[1] == 'all':
	f = open("SCPI_ALLScript.txt", "r")
elif sys.argv[1] == 'current':
	f = open("SCPI_CurrScript.txt", "r")
elif sys.argv[1] == 'front':
	f = open("SCPI_FrontScript.txt", "r")
elif sys.argv[1] == 'z':
	f = open("SCPI_Script.txt", "r")

oscilloscope.timeout = 10000;

lines = f.readlines()
for a in lines :
		oscilloscope.write(a)
		time.sleep(0.1)

time.sleep(0.2)
#print oscilloscope.query('READ? "defbuffer1"')

if sys.argv[1] == 'all':
	r =  oscilloscope.query('TRAC:DATA? 1, 22, "defbuffer1", CHAN,FORM,CHAN')
elif sys.argv[1] == 'current':
	r =  oscilloscope.query('TRAC:DATA? 1, 2, "defbuffer1", CHAN,FORM,CHAN')
elif sys.argv[1] == 'front':
	r =  oscilloscope.query('TRAC:DATA? 1, 22, "defbuffer1", CHAN,FORM,CHAN')
elif sys.argv[1] == 'z':
	r =  oscilloscope.query('TRAC:DATA? 1, 5, "defbuffer1", CHAN,FORM,CHAN')



print '@' + r
oscilloscope.close()