from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        ball = cast.get_first_actor(BALL_GROUP) #RC
        ball_body = ball.get_body() #RC

        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - RACKET_WIDTH):
            position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())
            
        body.set_position(position)

        ball_position = ball_body.get_position() #RC
        ball_position = Point(position.get_x(), ball_position.get_y()) #RC        
        ball_body.set_position(ball_position) #RC
        