# Python-Multimeter-SCPI-Instruments
Communication and gathering info from NI Standard Instruments using SCPI scripts.

## Install
1. Install PyVisa, PyVisa-Py and PyUSB
2. For Windows, install NI Drivers (ni-visa_19.5_online_repach.exe)

## Test

import pyvisa

rm = pyvisa.ResourceManager()
print(rm.list_resources()) # Identify connected SCPI NI 

