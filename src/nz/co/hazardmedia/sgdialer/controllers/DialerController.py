__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from nz.co.hazardmedia.sgdialer.controllers.ChevronController import ChevronController
from nz.co.hazardmedia.sgdialer.models.AddressBookModel import AddressBookModel
from nz.co.hazardmedia.sgdialer.controllers.SoundController import SoundController


class DialerController(object):
    chevron_controller = None
    address_book_model = None

    def __init__(self):
        self.chevron_controller = ChevronController()
        self.address_book_model = AddressBookModel()

        print "DialingController initialized."

        #self.prompt_address_input()
        #27-7-15-32-12-30
        #dial abydos
        self.dial(27, 7, 15, 32, 12, 30, 1)

    def prompt_address_input(self, type="command-line"):

        if type == "command-line":

            symbol1 = raw_input("Enter 1st symbol:")
            symbol2 = raw_input("Enter 2nd symbol:")
            symbol3 = raw_input("Enter 3rd symbol:")
            symbol4 = raw_input("Enter 4th symbol:")
            symbol5 = raw_input("Enter 5th symbol:")
            symbol6 = raw_input("Enter 6th symbol:")
            symbol7 = raw_input("Enter 7th symbol:")
            symbol8 = raw_input("Enter 8th symbol or leave blank to finish:")

            if symbol8 != "":
                symbol9 = raw_input("Enter 9th symbol or leave blank to finish:")
            else:
                symbol9 = ""
        elif type == "key":
            pass

        self.dial(symbol1, symbol2, symbol3, symbol4, symbol5, symbol6, symbol7, symbol8, symbol9)

    def dial(self, symbol1, symbol2, symbol3, symbol4, symbol5, symbol6, symbol7, symbol8='', symbol9=''):

        print "Dialing " + str(symbol1) + "-" + str(symbol2) + "-" + str(symbol3) + "-" + str(symbol4) + "-" + \
              str(symbol5) + "-" + str(symbol6) + "-" + str(symbol7) + "-" + str(symbol8) + "-" + str(symbol9)

        success = True
        for address in self.address_book_model.addresses:
            if address.symbol1.code != symbol1:
                success = False

            if address.symbol2.code != symbol2:
                success = False

            if address.symbol3.code != symbol3:
                success = False

            if address.symbol4.code != symbol4:
                success = False

            if address.symbol5.code != symbol5:
                success = False

            if address.symbol6.code != symbol6:
                success = False

            if (address.symbol7 is not None and address.symbol7.code != symbol7) or address.symbol7 == 1:
                success = False

            if symbol8 != '' and address.symbol8.code != symbol8:
                success = False

            if symbol9 != '' and address.symbol9.code != symbol9:
                success = False

        print "Dialing success: "+str(success)