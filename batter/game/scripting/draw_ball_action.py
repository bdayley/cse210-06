from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class DrawBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        # need racket position to draw the ball #BD
        racket = cast.get_first_actor(RACKET_GROUP)
        racket_body = racket.get_body()
        racket_x = racket_body.get_position().get_x()
        racket_y = racket_body.get_position().get_y()

        if ball.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
        
        position = body.get_position()
        
        # ball moves with racket #BD
        ball_vy = body.get_velocity().get_y() # ball is not moving up or down
        if ball_vy == 0:
            position = Point(racket_x + RACKET_WIDTH / 2, racket_y - RACKET_HEIGHT)
            
        image = ball.get_image()
        #position = body.get_position() #BD
        self._video_service.draw_image(image, position)