__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from nz.co.hazardmedia.sgdialer.controllers.ChevronController import ChevronController


class GateController(object):

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
        self.chevron1 = ChevronController(1)
        self.chevron2 = ChevronController(2)
        self.chevron3 = ChevronController(3)
        self.chevron4 = ChevronController(4)
        self.chevron5 = ChevronController(5)
        self.chevron6 = ChevronController(6)
        self.chevron7 = ChevronController(7)
        self.chevron8 = ChevronController(8)
        self.chevron9 = ChevronController(9)
        pass

    def lock_chevron(self, number):
        if number == 1:
            self.chevron1.lock()

        elif number == 2:
            self.chevron2.lock()

        elif number == 3:
            self.chevron3.lock()

        elif number == 4:
            self.chevron4.lock()

        elif number == 5:
            self.chevron5.lock()

        elif number == 6:
            self.chevron6.lock()

        elif number == 7:
            self.chevron7.lock()

        elif number == 8:
            self.chevron8.lock()

        elif number == 9:
            self.chevron9.lock()