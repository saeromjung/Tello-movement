echo "# Tello-movement" >> README.mdfrom djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
me.send_rc_control(0,0,0,0)

