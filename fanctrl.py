#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import sys
import signal

FAN_PIN = 18
PWM_FREQ = 25

WAIT_TIME=5
HISTERY=1

STOP_TEMP=45.0
MIN_TEMP=52.0
MAX_TEMP=60.0

MIN_FAN=25.0
MAX_FAN=100.0
START_FAN=100.0
STOP_FAN=0.0

STEP=(MAX_FAN - MIN_FAN) / (MAX_TEMP - STOP_TEMP)

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

    fan=GPIO.PWM(FAN_PIN,PWM_FREQ)
    fan.start(int(STOP_FAN))

    return fan

def cleanup():
    print("END")
    GPIO.cleanup()
    sys.exit()

def get_temp():
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as ftemp:
        return float(ftemp.read()) / 1000

def wait():
    time.sleep(WAIT_TIME)

def set(fan, pf):
    fan.ChangeDutyCycle(int(pf))

def get_p(temp):
    if temp <= STOP_TEMP:
        return STOP_FAN
    if temp >= MAX_TEMP:
        return MAX_FAN

    return max(
            MIN_FAN,
            min(
                MAX_FAN,
                MIN_FAN + STEP * (temp - MIN_TEMP)
                )
            )

def handle_signal():
    raise(SystemExit)

signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

fan = init()

last_temp=0.0
last_p=0.0
try:
    while True:
        wait()
        temp=get_temp()

        print("TEMP={:.2f}, SPEED={:.0f}%".format(temp,last_p))

        if abs(last_temp - temp) < HISTERY:
            continue

        last_temp = temp

        if last_p == 0 and temp < MIN_TEMP:
            continue

        p = get_p(temp)

        if last_p == 0 and p > 0:
            last_p = START_FAN
            set(fan, START_FAN)
        elif abs(last_p - p) > HISTERY:
            last_p = p
            set(fan, p)

except:
    print("Unexpected error:", sys.exc_info())
    raise
        
finally:
    cleanup()

