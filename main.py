from espsimple import mqtt, name
import time, machine, sht31

try:
    m = mqtt()
    # NodeMCU: Pin(5) = D1, Pin(4) = D2
    sensor = sht31.SHT31(machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4)))
    while True:
        (temp, humi) = sensor.get_temp_humi()
        print("Temp: %s Humi: %s" % (temp, humi))
        m.publish('hackeriet/sensor/' + name() + '/temp', str(temp))
        m.publish('hackeriet/sensor/' + name() + '/humi', str(humi))
        time.sleep(1)
except KeyboardInterrupt:
    raise
except Exception as e:
    print(e)
    print("** machine.reset() in 5 sec **")
    time.sleep(5)
    machine.reset()
