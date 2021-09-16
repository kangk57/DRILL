from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#사각형 운동

x = 400
y = 90
while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)
    if(x < 800 and y == 90):
        x += 2
    if(x == 800 and y < 600):
        y += 2
    if(x > 0 and y == 600):
        x -= 2
    if(x == 0 and y > 0 ):
        y -= 2
    delay(0.005)

#원

    




close_canvas()
