# Python-Multimeter-SCPI-Instruments

Communication and gathering info from NI Standard Instruments using SCPI scripts.

## Install

1. Install PyVisa, PyVisa-Py and PyUSB
2. For Windows, install NI Drivers (ni-visa_19.5_online_repach.exe)

## Test

import pyvisa

rm = pyvisa.ResourceManager()
print(rm.list_resources()) # Identify connected SCPI NI 


## Files & Folders

1. **SCPI.py** : Connects to the instrument (Keithley DAQ6510 in this case) and sends commands from the .txt SCPI Scripts
1. **SCPI_Script.txt** : Creates a Voltage Scan for Ch 101-105
1. **SCPI_ALLScript.txt** : Reads all rear channels
1. **SCPI_FrontScript.txt** : Reads Front channel
1. **SCPI_CurrScript.txt** : Reads rear current channel

## Notes

