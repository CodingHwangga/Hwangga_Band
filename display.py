import board, digitalio
from adafruit_rgb_display import st7789

WIDTH = HEIGHT = 240

def init_display():
    cs = digitalio.DigitalInOut(board.CE0)
    dc = digitalio.DigitalInOut(board.D25)
    rst = digitalio.DigitalInOut(board.D24)

    backlight = digitalio.DigitalInOut(board.D26)
    backlight.switch_to_output()
    backlight.value = True

    disp = st7789.ST7789(
        board.SPI(), width=WIDTH, height=HEIGHT, rotation=0,
        x_offset=0, y_offset=80,
        cs=cs, dc=dc, rst=rst, baudrate=24000000,
    )
    return disp, backlight