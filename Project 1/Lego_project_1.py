#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialiser EV3-brikken (hovedenheten til roboten)
hjernen = EV3Brick()

# Initialiser motorene på port B og C (venstre og høyre hjul)
venstre_motor = Motor(Port.C)
hoyre_motor = Motor(Port.B)

# Vis "Hello World" på LCD-skjermen
hjernen.screen.print("Hello World")
wait(2000)  # Vent 2 sekunder så teksten vises
 
# Funksjon for å kjøre rett frem
def kjør_frem_kort():
    # Kjør begge motorer 720 grader (to hele runder) med hastighet 200
    # Stop.BRAKE gjør at motoren bremser og stopper raskt etter kjøringen
    # False betyr at denne motoren ikke venter på at kjøringen skal bli ferdig før neste linje
    venstre_motor.run_angle(2000, 720, Stop.BRAKE, False)
    # True betyr at denne motoren venter til kjøringen er ferdig før programmet går videre
    hoyre_motor.run_angle(2000, 720, Stop.BRAKE, True)

def kjør_frem_langt():
    # Kjør begge motorer 720*2 grader (to hele runder) med hastighet 200
    # Stop.BRAKE gjør at motoren bremser og stopper raskt etter kjøringen
    # False betyr at denne motoren ikke venter på at kjøringen skal bli ferdig før neste linje
    venstre_motor.run_angle(2000, 720*2, Stop.BRAKE, False)     
    # True betyr at denne motoren venter til kjøringen er ferdig før programmet går videre
    hoyre_motor.run_angle(2000, 720*2, Stop.BRAKE, True)

# Funksjon for å svinge 90 grader til høyre
def sving_hoyre():
    # Venstre motor kjører fremover, høyre motor bakover for å svinge
    # 175 grader gir omtrent en 90 graders sving (avhengig av robotens design)
    venstre_motor.run_angle(400, 175, Stop.BRAKE, False)
    hoyre_motor.run_angle(400, -175, Stop.BRAKE, True)

def drift():
    #Vi hadde det litt gøy på slutten 
    #Funksjonen får motoren til å gå i sirkler altså den drifter
    venstre_motor.run_angle(5000, 2000, Stop.BRAKE, False)
    hoyre_motor.run_angle(5000, -2000, Stop.BRAKE, True)

# Kjør i et rektangel (fire sider og fire svinger)
for i in range(4):
    if i % 2 == 0:
        kjør_frem_kort()      # Kjør kort hvis partall
    else:
        kjør_frem_langt()     # Kjør langt hvis oddetall
    sving_hoyre()    # Sving 90 grader til høyre


# Stopp begge motorene etter at rektangelet er kjørt
venstre_motor.stop()
hoyre_motor.stop()

# Roboten sier "Have a nice day" med høyttaleren
ev3.speaker.say("Have a nice day")

#drifter
drift()
#morsom ting å si
ev3.speaker.say("If police not there, everything legal!")
