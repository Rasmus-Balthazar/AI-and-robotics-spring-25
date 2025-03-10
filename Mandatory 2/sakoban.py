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


tape = lambda x: x < 5
def check_line(sensor: ColorSensor):
    return sensor.reflection() < 6


def check_intersection(ls: ColorSensor, rs: ColorSensor):
    return check_line(ls) and check_line(rs)

def calibrate_movement(speed, db: DriveBase, lcs: ColorSensor, rcs: ColorSensor):
    if(check_line(lcs)):
        db.drive(speed, -100)
    elif(check_line(rcs)):
        db.drive(speed, 100)
    else:
        db.drive(speed, 0)

while not hub.imu.ready():
    print('calibrating')
    wait(1000)


def noise(n, vol: Int = 30):
    hub.speaker.volume(vol)
    for _ in range(n):
        hub.speaker.beep()
        wait(50)

# main loop!
reached_goal = False
debug_mode = True
hub.speaker.volume(10)

junction_detected = lambda s : s.reflection() < 6


while not reached_goal:
    if(junction_detected(sensor_left)):
        #
        reached_goal = True
        noise(3,30)
    calibrate_movement(100, drive_base, sensor_left, sensor_right)
    l = check_line(sensor_left)
    r = check_line(sensor_right)
    if(debug_mode):
        print(drive_base.distance())
drive_base.stop()



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