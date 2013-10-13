__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from nz.co.hazardmedia.sgdialer.models.ChevronModel import ChevronModel


class ChevronController(object):
    chevron1 = None
    chevron2 = None
    chevron3 = None
    chevron4 = None
    chevron5 = None
    chevron6 = None
    chevron7 = None
    chevron8 = None
    chevron9 = None

    def __init__(self):
        self.chevron1 = ChevronModel("Chevron 1")
        self.chevron2 = ChevronModel("Chevron 2")
        self.chevron3 = ChevronModel("Chevron 3")
        self.chevron4 = ChevronModel("Chevron 4")
        self.chevron5 = ChevronModel("Chevron 5")
        self.chevron6 = ChevronModel("Chevron 6")
        self.chevron7 = ChevronModel("Chevron 7")
        self.chevron8 = ChevronModel("Chevron 8")
        self.chevron9 = ChevronModel("Chevron 9")

        print "ChevronController initialized."
        pass