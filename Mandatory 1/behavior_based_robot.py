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
sensor_middle = ColorSensor(Port.C) # middle
sensor_left = ColorSensor(Port.E) # left
sensor_right = ColorSensor(Port.F) # right

#permissable ranges

def turn(angle):
    drive_base.turn(angle, Stop.COAST_SMART, wait=True)

def move(distance: int):
    drive_base.straight(distance, Stop.COAST_SMART, wait=True)

def calibrate():
    initial_heading = hub.imu.heading()
    return initial_heading
# method for keeping direction.

def measure_reflection_n_times(n: int, s: ColorSensor):
    measurements = []
    for i in range(n):
        aux = []
        for i in range(20):
            aux.append(s.reflection())
        average = sum(aux, 0)/len(aux)
        measurements.append(average)
        if( i % 2 == 0):
            hub.speaker.volume(20)
            hub.speaker.beep()
    return measurements


def calibrate_color_sensor(sensor_port: Port):
    sensor_to_be_calibrated = ColorSensor(Port)
    v = []
    for i in range(10):
        v.append(sensor_to_be_calibrated.reflection())
    average_reflection = sum(v)/v.count
    return sensor_to_be_calibrated, average_reflection

def check_fall():
    vals = []
    # vals.append(sensor_middle.reflection())
    vals.append(sensor_left.reflection())
    vals.append(sensor_right.reflection())
    return min(vals)

def check_collision():
    # sensor_middle is responsible
    r = sensor_middle.reflection()
    # if(r > 1): 
    #     turn(180)
    return r

desk_color = Color(h=200, s=15, v=21)


def check_if_in_range(val, r):
    lower, upper = r
    return lower <= val and val <= upper

hue = (100,300)
saturation = (5, 30)
brightness = (5, 30)
# hue = (160,240)
# saturation = (9, 21)
# brightness = (18, 24)
def check_is_table(sensor: ColorSensor):
    c = sensor.hsv(True)
    # colors are immutable, but I hope this works!
    h = c.h
    s = c.s
    v = c.v
    return check_if_in_range(h, hue) and check_if_in_range(s, saturation) and check_if_in_range(v, brightness)

# while True:
#     print(check_is_table(sensor_left))
#     drive_base.drive(100, 0)
#     wait(400)
#TODO - use IMU to check if we are still moving

while not hub.imu.ready():
    print('calibrating')
    wait(1000)

# def is_moving():
    # return 100 < hub.imu.acceleration(Axis.X)

# while True:
#     turn(30) #should be left
#     wait(1000)
z
def noise(n):
    hub.speaker.volume(30)
    for _ in range(n):
        hub.speaker.beep()
        wait(50)

# while True:
#     print(check_is_table(sensor_left))

# while True:
#     print(sensor_left.reflection())

counter = 1
noise(4)
while True:
    #check if we have not collided run
    # check if it still runs
    drive_base.drive(100, 0)

    while check_fall() > 0 and check_collision() < 1 and not hub.imu.stationary():
    # while check_fall() > 0 and check_collision() < 1:
        wait(50)
        # if(check_is_table(sensor_left)):
        #     move(-50)
        #     turn(30)
        # print('so fast!')
    # error state, turn depending on which sensor detected fall
    counter = counter + 1
    move(-50)
    degree_to_turn = 45
    if counter % 5 == 0:
        turn(randint(-90, 90))
        noise(3)
    # elif check_is_table(sensor_left) or sensor_left.reflection() < 1:
    elif sensor_left.reflection() < sensor_right.reflection():
        turn(-degree_to_turn)
        noise(1) #one noise for right
    else:
        turn(degree_to_turn)
        noise(2) #two noise for left
    
    # turn(degree_to_turn)

# while True:
#     print(sensor_middle.reflection())
#     wait(500)

# sensor1.reflection()
    # wait(400)
# while True: