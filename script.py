import pyautogui
from time import perf_counter


def main() -> None:
    print("Move mouse to any corner of the screen to stop")
    print("Ctrl+C will also stop the program")
    width: int = pyautogui.size()[0]
    height: int = pyautogui.size()[1]
    start_time: float
    try:
        pyautogui.moveTo(width/2, height/2)
        start_time = perf_counter()
        for i in range(9):
            print(i)
            while(perf_counter() - start_time) < 90.0:
                pyautogui.mouseDown(button='left', x=width/2, y=height/2)
            else:
                pyautogui.write(str(i+1))
                start_time = perf_counter()
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()
