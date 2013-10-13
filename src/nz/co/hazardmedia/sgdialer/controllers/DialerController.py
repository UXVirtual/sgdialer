__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from nz.co.hazardmedia.sgdialer.controllers.ChevronController import ChevronController
from nz.co.hazardmedia.sgdialer.models.AddressBookModel import AddressBookModel


class DialerController(object):

    chevron_controller = None
    address_book_model = None

    def __init__(self):
        self.chevron_controller = ChevronController()
        self.address_book_model = AddressBookModel()

        print "DialingController initialized."
