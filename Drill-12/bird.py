import game_framework
from pico2d import *

import random
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SPEED_KMPH = 20.0  # Km / Hour
SPEED_MPM = (SPEED_KMPH * 1000.0 / 60.0)
SPEED_MPS = (SPEED_MPM / 60.0)
SPEED_PPS = (SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHT, LEFT = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT,
    (SDL_KEYUP, SDLK_LEFT): LEFT
}

class IdleState:
    def enter(bird, event):
        if event == RIGHT:
            bird.velocity += SPEED_PPS
        elif event == LEFT:
            bird.velocity -= SPEED_PPS

    def exit(bird, event):
        pass

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16

    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 200, 100, 100, bird.x, bird.y)


next_state_table = {
    IdleState: {RIGHT: IdleState, LEFT: IdleState}
}

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(0, 1600), random.randint(0, 600)
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


birds = [Bird() for i in range(5)]