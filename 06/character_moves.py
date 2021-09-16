from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


#사각형 운동

x = 400
y = 90
ang = 0
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

#원 운동

    if(x == 400 and y == 90):
        for i in range(0 , 359+1):
            sin = math.sin(ang / 360 * 2 * math.pi)
            cos = math.cos(ang / 360 * 2 * math.pi)
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(400-255*sin,345-255*cos)
            ang +=1
            delay(0.005)

    




close_canvas()
