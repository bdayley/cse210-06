from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.image import Image

class DrawNewBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ball_list = cast.get_actors(BALL_GROUP)

        racket = cast.get_first_actor(RACKET_GROUP)
        racket_body = racket.get_body()
        rx = racket_body.get_position().get_x()
        ry = racket_body.get_position().get_y()

        if len(ball_list) == 0:
            cast.clear_actors(BALL_GROUP)
            x = rx
            y = ry - RACKET_HEIGHT
            position = Point(x, y)
            size = Point(BALL_WIDTH, BALL_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(BALL_IMAGE)
            ball = Ball(body, image, True)
            cast.add_actor(BALL_GROUP, ball)
