__author__ = 'Michael Andrew michael@hazardmedia.co.nz'


class ChevronModel(object):
    name = ""
    locked = False
    encoded = False

    def __init__(self, name):
        self.name = name