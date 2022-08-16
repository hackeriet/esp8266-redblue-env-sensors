upload_main:
	env AMPY_PORT=/dev/ttyUSB0 ampy put main.py main.py

upload: upload_main
	env AMPY_PORT=/dev/ttyUSB0 ampy put espsimple.py espsimple.py
