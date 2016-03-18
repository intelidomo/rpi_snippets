#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

from stepper_motor import StepperMotor

# Instance the motor supplying GPIO ports, change mode and delay time
# Instancia al motor indicando los puertos GPIO a los que está conectado, cambia modo y tiempo de espera
motor = StepperMotor(12,16,20,21,3,0.002)

# Go 100 steps forward
# Avanza 100 pasos a la derecha
motor.goForward(100)

# Turns back mode to default
# Cambia el modo al predeterminado
motor.setMode(2)

# Go 150 steps backwards
# Avanza 150 pasos a la izquierda
motor.goBackwards(200)

GPIO.cleanup()
