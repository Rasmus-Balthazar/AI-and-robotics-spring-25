from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from urandom import randint

hub = PrimeHub()

# setup
motor_left = Motor(Port.B, Direction.CLOCKWISE)
motor_right = Motor(Port.A, Direction.COUNTERCLOCKWISE)
# wheel_circumferance = 17.6
wheel_circumferance = 56
axle_track = 110
drive_base = DriveBase(motor_left, motor_right, wheel_circumferance, axle_track)

#setup sensor
sensor_left = ColorSensor(Port.F) # left
sensor_right = ColorSensor(Port.E) # right

#permissable ranges

def turn(angle):
    drive_base.turn(angle, Stop.COAST_SMART, wait=True)

def move(distance: int):
    drive_base.straight(distance, Stop.COAST_SMART, wait=True)

def calibrate():
    initial_heading = hub.imu.heading()
    return initial_heading
# method for keeping direction.

desk_color = Color(h=200, s=15, v=21)

def check_if_in_range(val, r):
    lower, upper = r
    return lower <= val and val <= upper

hue = (0, 50)
saturation = (0, 30)
brightness = (0, 30)
# hue = (160,240)
# saturation = (9, 21)
# brightness = (18, 24)
def check_line(sensor: ColorSensor):
    c = sensor.hsv(True)
    h = c.h
    s = c.s
    v = c.v
    return check_if_in_range(h, hue) and check_if_in_range(s, saturation) and check_if_in_range(v, brightness)

while not hub.imu.ready():
    print('calibrating')
    wait(1000)

def check_for_black_line(s: ColorSensor):
    detected_color = s.color()
    return detected_color == Color.BLACK


def noise(n):
    hub.speaker.volume(30)
    for _ in range(n):
        hub.speaker.beep()
        wait(50)

# main loop!
reached_goal = False
drive_base.drive(-100, 0)
while not reached_goal:
    if(check_line(sensor_left) and check_line(sensor_right)):
        #If we get here, we have found a line meaning we have veered off of the path
        # or gotten to a crossing
        turn(90)
        reached_goal = True

drive_base.stop()


maze_representation = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
#starting in upper left corner
box_length = (184.5, 65.5, 185, 66)


# def turn_corner():
     

# debug tools /////////////////////////////////////
def measure_average_hsv(n, sensor: ColorSensor, surface = False):
    vs = []
    hs = []
    ss = []
    for i in range(n):
        vs.append(sensor.hsv(surface).v)
        hs.append(sensor.hsv(surface).h)
        ss.append(sensor.hsv(surface).s)
        # wait(1)

    return sum(hs)/n, sum(ss)/n, sum(vs)/n
    # return sum(hs)/n
def debug():
    print('-------------------------------------------------------------------')
    print(f'sensor_left average hsv with surface true{measure_average_hsv(1000, sensor_left, True)}')
    print(f'sensor_right average hsv with surface true{measure_average_hsv(1000, sensor_right, True)}')
    print(f'sensor_left average hsv with surface false{measure_average_hsv(5000, sensor_left, False)}')
    print(f'sensor_right average hsv with surface false{measure_average_hsv(5000, sensor_right, False)}')
    print('-------------------------------------------------------------------')
    while True:
        # print(check_for_black_line(sensor_right))
        print(sensor_left.hsv(True), sensor_right.hsv())
        print(sensor_left.color(True), sensor_right.color())
        wait(2000)