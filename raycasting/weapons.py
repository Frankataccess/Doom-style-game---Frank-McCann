from sprite_object import *

class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png' , scale=0.4, animations_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time= animations_time)
        self.images = deque([])