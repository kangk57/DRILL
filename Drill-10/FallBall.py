from pico2d import *
from pico2d import *
import random


# Game object class here


# 생성자 self는 다음에설명
# 클래스안에 객체의 상태를 나타내는 변수에 연결하거나
# 그 객체의 함수를 호출할 때는 self를 붙여줘야함
class Grass:
    def __init__(self):  # 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class BigBall:
    def __init__(self):
        self.fall = random.randint(0, 300)
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 800), 599
        self.frame = 0

    def update(self):
        falling = random.randint(0, 300)
        self.y -= falling
        self.frame = (self.frame + 1) % 2

    def draw(self):
        self.image.clip_draw(self.frame * 41, 0, 41, 41, self.x, self.y)


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(0, 700), 90
        self.frame = 0

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code 초기화
open_canvas()

grass = Grass()  # 잔디 객체를 생성
ball = BigBall()

# team
team = [Boy() for i in range(11)]

# balls
balls = [BigBall() for i in range(20)]
running = True

# game main loop code  로직/드로잉/끝?
while running:

    handle_events()  # 키 입력을 받아들이는 처리..

    # Game logic
    # grass 에 대한 상호작용. 은 움직이지 않으므로 무시
    for boy in team:
        boy.update()  # 소년의 상호작용
    for BigBall in balls:
        BigBall.update()

    # Game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for BigBall in balls:
        BigBall.update()

    update_canvas()

    delay(0.05)
