from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


motor_left = Motor(Port.C, Direction.CLOCKWISE)
motor_right = Motor(Port.D, Direction.COUNTERCLOCKWISE)
# wheel_circumferance = 17.6
wheel_circumferance = 56
axle_track = 110
drive_base = DriveBase(motor_left, motor_right, wheel_circumferance, axle_track)
speed = 100

# methods of movement
def turn_right(db: DriveBase = drive_base):
    drive_base.turn(90, Stop.BRAKE, wait=True)
def turn_left(db: DriveBase = drive_base):
    drive_base.turn(-90, Stop.BRAKE, wait=True)
def turn(angle):
    drive_base.turn(angle, Stop.BRAKE, wait=True)
def move_forward(distance: int):
    drive_base.straight(distance * -1, Stop.BRAKE, True)
def move_slow(distance: int):
    drive_base.settings(20)
    drive_base.straight(distance * -1, Stop.BRAKE, True)
    drive_base.settings(195)

# fun stuff
def play_woody_woodpecker():
    woody_woodpecker_laugh = ["C4/8", "F4/8", "A4/8", "C5/8", "R/8", "A4/8", "R/2"] * 2
    hub.speaker.play_notes(woody_woodpecker_laugh, 300)

# move_forward(100) #moves about 10 cm
# 93 - mid
# 125 - good turning point
# 144 - distance to target 2
def drive_to_target_1():
    move_forward(1250 + 15 + 5)
    turn(90)
    move_forward(310 - 35 - 15 + 5)
    turn(-45)
    play_woody_woodpecker()

def drive_to_target_2():
    move_forward(1440 + 50 + 15)
    turn(90)
    move_forward(10 * -1)
    play_woody_woodpecker()

def drive_to_target_3():
    move_forward(930 + 65 + 30)
    turn(-90)
    move_forward(175 + 35 + 20)
    turn(-(135 + 3))
    play_woody_woodpecker()


# turn(45)

# drive_to_target_1()
# drive_to_target_2()
# drive_to_target_3()

wait(1500)