__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

import random
import pygame
from pygame import mixer
from pygame.mixer import Sound
from nz.co.hazardmedia.sgdialer.config.Config import Config
from nz.co.hazardmedia.sgdialer.models.SoundModel import SoundModel


class SoundController(object):
    sounds = {}

    def __init__(self):

        mixer.init(44100)

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

        :param file_names: Dictionary of file names, where the key is the ID of the file as a string
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

    def play(self, name, queue_sounds=False, play_next_queued_sound=False):

        if not mixer.get_init():
            print "Mixer not initialized! Cannot play sound."

        #channel = mixer.find_channel()
        #channel.play(self.sounds[id])

        sound_item = self.sounds[name]

        if queue_sounds:
            mixer.music.load(sound_item.path)
            mixer.music.queue(sound_item.path)
            print "Queued sound: " + name
            if play_next_queued_sound:
                mixer.music.play()
            pass
        else:

            if sound_item.delay > 0:
                pygame.time.wait(sound_item.delay)

            elif sound_item.delay_min == sound_item.delay_max:
                pygame.time.wait(sound_item.delay_min)

            elif sound_item.delay_min > 0 and sound_item.delay_max > 0:
                rand = random.randrange(sound_item.delay_min, sound_item.delay_max, 250)
                pygame.time.wait(rand)

            sound_item.sound.play()

            print "Playing sound: " + name



