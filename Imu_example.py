from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Define colors for each side in a dictionary.
SIDE_COLORS = {
    Side.TOP: Color.RED,
    Side.BOTTOM: Color.BLUE,
    Side.LEFT: Color.GREEN,
    Side.RIGHT: Color.YELLOW,
    Side.FRONT: Color.MAGENTA,
    Side.BACK: Color.BLACK,
}

# Keep updating the color based on detected up side.
while True:

    # Check which side of the hub is up.
    up_side = hub.imu.up()
    # Change the color based on the side.
    hub.light.on(SIDE_COLORS[up_side])
    accel = hub.imu.acceleration()
    # print(f"acceleration! {accel}")

    # Get the acceleration vector in g's.
    # print(hub.imu.acceleration() / 9810)

    # Get the angular velocity vector.
    print(hub.imu.angular_velocity())

    # pitch, roll = hub.imu.tilt()
    # print(pitch, roll)
    # Also print the result.
    # print(up_side)
    wait(2000)

