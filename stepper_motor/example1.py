#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

from stepper_motor import StepperMotor

# Instance the motor supplying GPIO ports
# Instancia al motor indicando los puertos GPIO a los que está conectado
motor = StepperMotor(12,16,20,21)

# Go 100 steps forward
# Avanza 100 pasos a la derecha
motor.goForward(100)

# Go 150 steps backwards
# Avanza 150 pasos a la izquierda
motor.goBackwards(150)

GPIO.cleanup()
