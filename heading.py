from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# setup
motor_left = Motor(Port.A, Direction.CLOCKWISE)
motor_right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
# wheel_circumferance = 17.6
wheel_circumferance = 56
axle_track = 110
drive_base = DriveBase(motor_left, motor_right, wheel_circumferance, axle_track)

def turn(angle):
    drive_base.turn(angle, Stop.COAST_SMART, wait=False)

async def move_forward(distance: int):
    drive_base.straight(distance, Stop.COAST_SMART, wait=False)


def calibrate():
    initial_heading = hub.imu.heading()
    return initial_heading
# method for keeping direction.

initial_heading = calibrate()

# drive_base.settings(100)



def run():
    while True:
        move_forward(1000)

        # drive_base.drive(50, 0)
        deviation = hub.imu.heading() - initial_heading
        if(abs(deviation) > 10):
            # drive_base.turn(deviation, Stop.BRAKE, wait=False)
            # print(deviation)
            turn(deviation - initial_heading)
            # corregate(deviation, initial_heading)
        wait(400)
run()