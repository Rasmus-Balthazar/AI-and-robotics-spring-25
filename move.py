from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import multitask, run_task, wait

hub = PrimeHub()

motor_left = Motor(Port.C, Direction.CLOCKWISE)
motor_right = Motor(Port.D, Direction.COUNTERCLOCKWISE)
# wheel_circumferance = 17.6
wheel_circumferance = 56
axle_track = 110
drive_base = DriveBase(motor_left, motor_right, wheel_circumferance, axle_track)
speed = 100

# methods of movement
async def turn(angle):
    await drive_base.turn(angle, Stop.COAST_SMART)

async def move_forward(distance: int):
    await drive_base.straight(distance, Stop.COAST_SMART)

# run_task(turn(360))
# run_task(move_forward(10))
async def s():
    await multitask((turn(400), move_forward(100)), race=False)
    wait(3000)
    print('done')
run_task(s())

# wait(4000)