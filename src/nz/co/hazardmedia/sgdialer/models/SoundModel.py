__author__ = 'Michael Andrew michael@hazardmedia.co.nz'


class SoundModel(object):
    sound = None
    path = ""
    delay = 0
    delay_min = 0
    delay_max = 0

    def __init__(self, sound, path, delay=0, delay_min=0, delay_max=0):
        self.sound = sound
        self.path = path
        self.delay = delay
        self.delay_min = delay_min
        self.delay_max = delay_max