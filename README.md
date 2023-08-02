# esp8266-redblue-env-sensors

This is (bad) micropython code for esp8266 sensors running at hackeriet

To upload the code to the sensors, you need `ampy`. To access the REPL you can use something like `screen /dev/ttyUSB0 115200`

- https://micropython.org/
- https://pypi.org/project/adafruit-ampy/

You can also download code with `ampy get main.py` or `ampy get config.json` from the device directly

You need to upload a `config.json` that contains stuff like wifi credentials, mqtt credentials, etc.

TODO: write more meaningful things
