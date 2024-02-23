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

#Global Variables
digitalPin = 13

async def blinkLED(myBoard, pin):
    #Set the pin mode
    await myBoard.set_pin_mode_digital_output(pin)

    #Toggle the pin for unlimited times with an interval of 1 second
    while True:
        await myBoard.digital_write(pin, 1)
        await asyncio.sleep(1)
        await myBoard.digital_write(pin, 0)
        await asyncio.sleep(1)

#Get the event loop
eventLoop = asyncio.get_event_loop()

#Instatiate pymata express
myBoard = pymata_express.PymataExpress()

try:
    #Start the main function
    eventLoop.run_until_complete(blinkLED(myBoard, digitalPin))
except KeyboardInterrupt:
    eventLoop.run_until_complete(myBoard.shutdown())
    sys.exit(0)
