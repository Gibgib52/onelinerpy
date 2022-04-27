from pynput import mouse
from pyautogui import size
from time import sleep

def coords_grab():
    print(f"CoordGrabber Starting...")
    # ANSI escape sequences for color
    class c:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m' # end color
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    # area calc and slope
    def calc_area(x1, y1, x2, y2):
        if x1 < x2: 
            width = x1 - x2
        else:
            width = x2 - x1
        
        if y1 > y2:
            height = y2 - y1
        else:
            height = y1 - y2

        sx, sy = size()
        screen_area = sx * sy

        calcArea = width * height
        calcPercent = round((calcArea / screen_area) * 100, 2) # round percentage to 2 decimal places
        
        # safe incase div by zero
        try:
            calcSlope = round(height/width, 2)
        except:
            calcSlope = "undefined"

        return (calcArea, calcPercent, calcSlope)

    coords = []
    def on_click(x, y, button, pressed):
        if button == button.middle and pressed:
            coords.append((x, y)) # add tuple with coords to list
            on_click.count += 1
            print(f"{c.OKGREEN}Capture{c.ENDC} {on_click.count}")
            if on_click.count == 2:
                return False # kill listener and exit func
    on_click.count = 0 # keeps track of how many times you've clicked

    with mouse.Listener(on_click=on_click) as listener:
        print(f"{c.OKGREEN}Listener Joined.{c.ENDC} Middle click to capture coords")
        listener.join()

    # after 2 clicks
    x1 = coords[0][0]
    y1 = coords[0][1]
    x2 = coords[1][0]
    y2 = coords[1][1]

    areaTuple = calc_area(x1,y1,x2,y2)

    # add "," between thousands and replace the "," with " "
    formattedArea = f"{areaTuple[0]:,}".replace(",", " ")
    formattedPercent = areaTuple[1]
    formattedSlope = areaTuple[2]
    tuplePair = f"{coords[0]} {coords[1]}"
    rawPair = f"{x1},{y1} {x2},{y2}"

    sleep(0.5) # sleep to look cool

    # the {c.OKGREEN} things are ANSI escape sequences for colors. {c.ENDC} goes to default term color
    print(f"{c.WARNING}{'-'*28}{c.ENDC}") # 10 "-"
    print(f"tuples: {tuplePair:>20}")
    print(f"raw: {rawPair:>23}")
    print(f"slope: {c.OKGREEN}{formattedSlope:>21}{c.ENDC}")
    print(f"area: {c.OKGREEN}{formattedArea:>20}px{c.ENDC}")
    print(f"% total: {c.OKGREEN}{formattedPercent:>18}%{c.ENDC}")
    print(f"{c.WARNING}{'-'*28}{c.ENDC}") # 10 "-"

coords_grab()
