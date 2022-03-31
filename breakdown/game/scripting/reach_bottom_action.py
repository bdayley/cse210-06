from constants import * #RC Start
from game.casting.sound import Sound
from game.scripting.action import Action


class ReachBottomAction(Action): 

   def __init__(self, physics_service, audio_service):
      self._physics_service = physics_service
      self._audio_service = audio_service    
      
   def execute(self, cast, script, callback):
      brick = cast.get_last_actor(BRICK_GROUP)

      if brick is not None:
         body = brick.get_body()
         position = body.get_position()
         stats = cast.get_first_actor(STATS_GROUP)
         y = position.get_y()
         hit_bottom_sound = Sound(HIT_BOTTOM_SOUND)

         if y >= (FIELD_BOTTOM - BRICK_HEIGHT):
            print("hit bottom...")
            points = brick.get_points() * -2
            stats.add_points(points)
            cast.remove_actor(BRICK_GROUP, brick)
            self._audio_service.play_sound(hit_bottom_sound) #RC End
