import globalvariables

import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
    if color == 0:
        strip[i] = (0,0,0)
    elif color == 1:
        strip[i] = (100,100,100)

    elif color == 10:
        strip[i] = (0,0,0)

    elif color == 11:
        strip[i] = (52,0,28)

    elif color == 12:
        strip[i] = (52,0,83)

    elif color == 13:
        strip[i] = (25,37,37)

    elif color == 14:
        strip[i] = (255,96,0)

    elif color == 15:
        strip[i] = (255,129,0)
# your color 16 did not exist
    elif color == 16:
        strip[i] = (255,163,0)
    
    elif color == 17:
        strip[i] = (255,186,0)

    elif color == 99:
        strip[i] = (0,0,0)


# ----------------------------------------------------------------------------------------------------
# START DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------



def showMessage(nextMessage,duration,myMessage):
    # start - fixed message 4 
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(duration)

    # switch to next message
    globalvariables.messageID = nextMessage


def showMessageFixedMovingD(nextMessage,duration,messageFixed,messageMoving,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxRow = startingPoint




    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = messageFixed[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(globalvariables.countToMaxRow+0,globalvariables.countToMaxRow+8):
        for c in range(0,8):
            temp = r % len(messageMoving)
            color = messageMoving[temp][c]
            lookupColor(color,i)
            i += 1



    globalvariables.countToMaxRow += 1
    globalvariables.durationCounter += 1
    if globalvariables.countToMaxRow > duration:
        globalvariables.countToMaxRow = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage


def showMessageFixedMovingL(nextMessage,duration,messageFixed,messageMoving,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxCol = startingPoint


    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = messageFixed[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(globalvariables.countToMaxCol+8,globalvariables.countToMaxCol+16):
            temp = c % len(messageMoving[0])
            color = messageMoving[r][temp]
            lookupColor(color,i)
            i += 1


    strip.write()

    globalvariables.countToMaxCol += 1
    globalvariables.durationCounter += 1
    if globalvariables.countToMaxCol > duration:
        globalvariables.countToMaxCol = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage


# ----------------------------------------------------------------------------------------------------
# END DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------



while True:
    strip.write()
    if globalvariables.messageID == 1:
        showMessage(2,1,globalvariables.messageVSA)
    elif globalvariables.messageID == 2:
        showMessage(3,1,globalvariables.message3)
    elif globalvariables.messageID == 3:
        showMessageFixedMovingL(4,8,globalvariables.message3,globalvariables.messageVSA,-8)
    elif globalvariables.messageID == 4:
        showMessageFixedMovingD(1,8,globalvariables.messageVSA,globalvariables.messageFALL,0)
