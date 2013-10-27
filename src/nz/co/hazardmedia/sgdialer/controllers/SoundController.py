__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from pygame import mixer
from pygame.mixer import Channel
from pygame.mixer import Sound
from nz.co.hazardmedia.sgdialer.config.Config import Config


class SoundController(object):

    sounds = []

    def __init__(self):
        mixer.init(44100)

        self.channel1 = Channel(1)
        self.channel2 = Channel(2)
        self.channel3 = Channel(3)
        self.channel4 = Channel(4)
        self.channel5 = Channel(5)
        self.channel6 = Channel(6)
        self.channel7 = Channel(7)
        self.channel8 = Channel(8)

    def preload_sounds(self, file_names):
        """
        Preload sounds
        @param file_names: Dictionary of file names, where the key is the of the file as a string
        """
        for key in file_names:
            self.sounds[key] = (Sound(Config.sound_path+'/'+file_names[key]))

    def play(self, name, channel):
        channel = mixer.find_channel()


