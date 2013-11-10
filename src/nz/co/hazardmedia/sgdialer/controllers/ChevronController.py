__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from nz.co.hazardmedia.sgdialer.models.ChevronModel import ChevronModel


class ChevronController(object):
    chevron_model = None
    id = 0

    def __init__(self, id):
        self.id = id

        if id == 1:
            name = "Chevron 1"
        elif id == 2:
            name = "Chevron 2"
        elif id == 3:
            name = "Chevron 3"
        elif id == 4:
            name = "Chevron 4"
        elif id == 5:
            name = "Chevron 5"
        elif id == 6:
            name = "Chevron 6"
        elif id == 7:
            name = "Chevron 7"
        elif id == 8:
            name = "Chevron 8"
        elif id == 9:
            name = "Chevron 9"

        self.chevron_model = ChevronModel(name)

        print "ChevronController initialized."

    def lock(self):
        self.chevron_model.locked = True