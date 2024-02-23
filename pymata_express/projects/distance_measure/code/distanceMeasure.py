"""

Copyright (c) 2024 Ezhuthola edTech Private Limited All rights reserved.

This is a free software. you can redistribute it and/or modify it under
the terms of the GENERAL PUBLIC LICENSE Version 1 as published by the
Ezhuthola edTech Private Limited, either or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

CONTACT
Ezhuthola edTech Private Limited
KP 14/607, 1st Floor
P.O Koodali, Kannur, Kerala, India - 670592
Mob - +91 7034484222
Email - contact@ezhuthola.online

"""

import asyncio
import sys
from pymata_express import pymata_express

#This program continuously monitor Ultrasonic Sensor (HC-SR04)
#and reports changes in distance sensed.

async def displayDistance(data):
    print("Distance in CM : ", data[2])

async def getDistance(myBoard, triggerPin, echoPin, callBack):
    await myBoard.set_pin_mode_sonar(triggerPin, echoPin, callBack)
    while True:
        try:
            await asyncio.sleep(3)
            print(await myBoard.sonar_read(13))
        except KeyboardInterrupt:
            await myBoard.shutdown()

eventLoop = asyncio.get_event_loop()
myBoard = pymata_express.PymataExpress()

try:
    eventLoop.run_until_complete(getDistance(myBoard, 13, 12, displayDistance))
    eventLoop.run_until_complete(myBoard.shutdown())
except(KeyboardInterrupt, RuntimeError):
    eventLoop.run_until_complete(myBoard.shutdown())
    sys.exit(0)
