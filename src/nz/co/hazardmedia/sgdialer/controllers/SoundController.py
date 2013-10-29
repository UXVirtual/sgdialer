__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

import random
import pygame
from pygame import mixer
from pygame.mixer import Sound
from nz.co.hazardmedia.sgdialer.config.Config import Config
from nz.co.hazardmedia.sgdialer.models.SoundModel import SoundModel
from nz.co.hazardmedia.sgdialer.events.EventType import EventType


class SoundController(object):
    sounds = {}

    def __init__(self):

        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()

        """self.channel1 = Channel(0)
        self.channel2 = Channel(1)
        self.channel3 = Channel(2)
        self.channel4 = Channel(3)
        self.channel5 = Channel(4)
        self.channel6 = Channel(5)
        self.channel7 = Channel(6)
        self.channel8 = Channel(7)"""

        if mixer.get_init():
            print "Mixer initialized."

        print "SoundController initialized."

    def preload_sounds(self, files):
        """
        Preload Sounds

        :param files: Dictionary of file objects in the format {"file_name": "name", "delay": 1000, "delay_min": 1000,
        "delay_max": 1000} where the key is the ID of the file as a string
        """
        for key in files:
            path = Config.sound_path + '/' + files[key]["file_name"]
            print "Preloading sound from path: " + path

            #if delay key does not exist set its default value
            if not "delay" in files[key]:
                files[key]["delay"] = 0

            if not "delay_min" in files[key]:
                files[key]["delay_min"] = 0

            if not "delay_max" in files[key]:
                files[key]["delay_max"] = 0

            self.sounds[key] = SoundModel(Sound(path), path, files[key]["delay"], files[key]["delay_min"],
                                          files[key]["delay_max"])

    def play(self, name, queue_sounds=False, play_next_queued_sound=False, loop_forever=False):

        if not mixer.get_init():
            print "Mixer not initialized! Cannot play sound."

        #channel = mixer.find_channel()
        #channel.play(self.sounds[id])

        sound_item = self.sounds[name]

        if queue_sounds:
            if mixer.music.get_busy():
                mixer.music.queue(sound_item.path)
                print "Queued sound: " + name

                if play_next_queued_sound:
                    mixer.music.play()

            else:
                mixer.music.load(sound_item.path)
                if loop_forever:
                    mixer.music.play(-1)
                else:
                    mixer.music.play()

                print "Playing sound: " + name

        else:

            if loop_forever:
                loops = -1
            else:
                loops = 0

            if sound_item.delay == sound_item.delay_min == sound_item.delay_max == 0:
                sound_item.sound.play(loops)

            elif sound_item.delay > 0:
                #pygame.time.wait(sound_item.delay)
                self.play_after_delay(sound_item.sound, sound_item.delay, loops)

            elif sound_item.delay_min == sound_item.delay_max:
                self.play_after_delay(sound_item.sound, sound_item.delay_min, loops)
                #pygame.time.wait(sound_item.delay_min)

            elif sound_item.delay_min > 0 and sound_item.delay_max > 0:
                rand = random.randrange(sound_item.delay_min, sound_item.delay_max, 250)
                #pygame.time.wait(rand)
                self.play_after_delay(sound_item.sound, rand, loops)



            print "Playing sound: " + name

    def play_after_delay(self, sound, delay=1000, loops=0):

        pygame.time.set_timer(EventType.SOUND_PLAY_AFTER_DELAY, delay)

        got_event = False
        while not got_event:
            for event in pygame.event.get():

                if event.type == EventType.SOUND_PLAY_AFTER_DELAY:
                    sound.play(loops)
                    got_event = True
                    break

    def play_when_idle(self, name, loop_forever=False):
        mixer.music.set_endevent(EventType.SOUND_PLAYBACK_ENDED)

        got_event = False
        while not got_event:
            for event in pygame.event.get():

                if event.type == EventType.SOUND_PLAYBACK_ENDED:
                    print("Sound playback ended")
                    mixer.music.set_endevent()
                    self.play(name, False, False, loop_forever)
                    got_event = True
                    break