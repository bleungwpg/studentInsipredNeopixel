import globalvariables

import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
    if color == 0:
        strip[i] = (255,255,255)

    elif color == 10:
        strip[i] = (255,77,175)

    elif color == 11:
        strip[i] = (252,0,128)

    elif color == 12:
        strip[i] = (252,0,83)

    elif color == 13:
        strip[i] = (252,37,37)

    elif color == 14:
        strip[i] = (255,96,0)

    elif color == 15:
        strip[i] = (255,129,0)
# your color 16 did not exist
    elif color == 16:
        strip[i] = (255,163,0)
    
    elif color == 17:
        strip[i] = (255,186,0)

# ----------------------------------------------------------------------------------------------------
# START DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------


def showMessageMaskD(nextMessage,duration,myMessage,mask,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxRow = startingPoint
        globalvariables.countToMaxCol = 0


    i = 0
    r = globalvariables.countToMaxRow
    r2 = 0
    while r2 < 8:
        for c in range(globalvariables.countToMaxCol,globalvariables.countToMaxCol+8):
            temp = r % len(myMessage)
            tempC = c % 8
            color = myMessage[temp][tempC]
            if mask[r2][c] == 1:
                lookupColor(color,i)
            else:
                strip[i] = (0,0,0)
            i += 1
        r2 += 1
        r += 1

    r = globalvariables.countToMaxRow
    r2 = 0
    while r2 < 8:
        for c in range(globalvariables.countToMaxCol+8,globalvariables.countToMaxCol+16):
#            temp = r2;
            tempC = c % 16
            temp = r % len(myMessage)
            color = myMessage[temp][tempC]
            if mask[r2][c] == 1:
                lookupColor(color,i)
            else:
                strip[i] = (0,0,0)
            i += 1
        r2 += 1
        r += 1

    strip.write()

    globalvariables.countToMaxCol += 1
    if (globalvariables.countToMaxCol >= len(mask[0])):
        globalvariables.countToMaxCol = 0

    globalvariables.countToMaxRow += 1
    globalvariables.durationCounter += 1
    if globalvariables.durationCounter > duration:
        globalvariables.countToMaxRow = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage




# ----------------------------------------------------------------------------------------------------
# END DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------



while True:
    if globalvariables.messageID == 1:
        # Call function - showMessage(nextMessageID, messageDuration, messagecolor, messagemask, start)
        showMessageMaskD(1,25,globalvariables.message4,globalvariables.mask1,0)
    elif globalvariables.messageID == 2:
        # Call function - showMessage(nextMessageID, messageDuration, messagecolor, messagemask, start)
        showMessageMaskD(1,20,globalvariables.message3,globalvariables.mask1,0)