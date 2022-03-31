from constants import *
from game.scripting.action import Action


class ControlBallAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        ball_list = cast.get_actors(BALL_GROUP)
        if len(ball_list) > 0:
            ball = cast.get_first_actor(BALL_GROUP)
            if self._keyboard_service.is_key_down(SPACE):
                ball.release()