from constants import * #RC Start
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacketBrickAction(Action):

   def __init__(self, physics_service, audio_service):
      self._physics_service = physics_service
      self._audio_service = audio_service
      
   def execute(self, cast, script, callback):
      brick = cast.get_last_actor(BRICK_GROUP)
      if brick is not None:
         racket = cast.get_first_actor(RACKET_GROUP)
         stats = cast.get_first_actor(STATS_GROUP)

         brick_body = brick.get_body()
         racket_body = racket.get_body()

         if self._physics_service.has_collided(brick_body, racket_body):
            cast.remove_actor(BRICK_GROUP, brick)
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    
            stats.lose_life() #RC End
