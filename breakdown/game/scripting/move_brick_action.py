from constants import * #RC Start
from game.casting.point import Point
from game.scripting.action import Action


class MoveBrickAction(Action):

   def __init__(self):
      pass

   def execute(self, cast, script, callback):
      brick = cast.get_last_actor(BRICK_GROUP)
      if brick is not None:
         body = brick.get_body()
         velocity = BRICK_DROP_VELOCITY
         position = body.get_position()
         x = position.get_x()
         
         position = position.add(velocity)

         body.set_position(position) #RC End
        