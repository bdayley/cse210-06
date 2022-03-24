from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveBrickAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
      #   brick = cast.get_first_actor(BRICK_GROUP)
        brick = cast.get_last_actor(BRICK_GROUP)
        body = brick.get_body()
      #   velocity = body.get_velocity()
        velocity = Point(0, 0.5)
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        body.set_position(position)
        