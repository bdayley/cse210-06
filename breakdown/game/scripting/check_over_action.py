from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP) #RC

        if stats.get_lives() == 0: #RC
           callback.on_next(GAME_OVER) #RC

        if len(bricks) == 0:
            # stats = cast.get_first_actor(STATS_GROUP) #RC
            stats.next_level()
            callback.on_next(NEXT_LEVEL)