#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
from stepper_motor import StepperMotor

# Instance the motor supplying GPIO ports
# Instancia al motor indicando los puertos GPIO a los que está conectado
motor = StepperMotor(12,16,20,21)

# Go 360 degrees clockwise (full turn)
# Avanza 360 grados en sentido del reloj (vuelta completa)
motor.clockwise(360)

# Espera un segundo
time.sleep(1)

# Go 180 degrees anticlockwise
# Regresa 180 grados en el sentido contrario al reloj
motor.anticlockwise(180)

# Go on till it reach its initial position
# Continua reduciendo de poco a poco hasta llegar a la posición inicial
time.sleep(0.5)
motor.anticlockwise(90)
time.sleep(0.5)
motor.anticlockwise(45)
time.sleep(0.5)
motor.anticlockwise(22.5)
time.sleep(0.5)
motor.anticlockwise(22.5)

GPIO.cleanup()
