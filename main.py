from PIL import Image, ImageDraw, ImageFont
from display import init_display, WIDTH, HEIGHT

disp, backlight = init_display()

img = Image.new("RGB", (WIDTH, HEIGHT), (10, 10, 30))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)

draw.text((WIDTH // 2, 100), "HWANGGA BAND", font=font, anchor="mm", fill=(255, 230, 0))
draw.rectangle((20, 150, 220, 170), outline=(255, 255, 255))

disp.image(img)