import pyautogui
import ctypes
from time import sleep
from time import perf_counter

# Credit to https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
PUL = ctypes.POINTER(ctypes.c_ulong)
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


def main() -> None:
    print("Move mouse to any corner of the screen to stop")
    print("Ctrl+C will also stop the program")
    print("You have 10 seconds before mining starts: Switch back to Minecraft now!")
    print("Test")
    while perf_counter() < 10:
        continue

    width: int = pyautogui.size()[0]
    height: int = pyautogui.size()[1]
    try:
        pyautogui.moveTo(width/2, height/2)
        start_time = perf_counter()
        for i in range(9):
            print(i)
            while(perf_counter() - start_time) < 190.0:
                pyautogui.mouseDown(button='left', x=width/2, y=height/2)
            else:
                print("I got here!")
                #TODO- Key input will not work
                pyautogui.mouseUp(button='left')
                presskey(0x0+(i + 3))
                sleep(1.0)
                start_time = perf_counter()
    except KeyboardInterrupt:
        return


# Actuals Functions

def presskey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def releasekey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


if __name__ == '__main__':
    main()
