__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

import pygame
from pygame import key
from pygame import event
from pygame.event import Event

from nz.co.hazardmedia.sgdialer.controllers.ChevronController import ChevronController
from nz.co.hazardmedia.sgdialer.models.AddressBookModel import AddressBookModel
from nz.co.hazardmedia.sgdialer.models.SymbolModel import SymbolModel
from nz.co.hazardmedia.sgdialer.events.EventType import EventType
from nz.co.hazardmedia.sgdialer.config.Config import Config


class DialerController(object):
    chevron_controller = None
    address_book_model = None

    manual_input = False

    def __init__(self):
        self.chevron_controller = ChevronController()
        self.address_book_model = AddressBookModel()
        self.manual_input = True

        print "DialingController initialized."

        #self.prompt_address_input()
        #self.address_input_listener()
        #27-7-15-32-12-30
        #dial abydos

    def input_symbol(self, character):
        if self.manual_input:
            if character in Config.address_symbol_keyboard_character:
                symbol = Config.address_symbol_keyboard_character[character]
                print 'Pressed symbol: '+symbol
                event.post(Event(EventType.SOUND_PLAY, {
                    "value": "dhd-button-press"
                }))

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

    def dial_auto(self, symbol1, symbol2, symbol3, symbol4, symbol5, symbol6, symbol7, symbol8='', symbol9=''):

        print "Dialing " + str(symbol1) + "-" + str(symbol2) + "-" + str(symbol3) + "-" + str(symbol4) + "-" + \
              str(symbol5) + "-" + str(symbol6) + "-" + str(symbol7) + "-" + str(symbol8) + "-" + str(symbol9)

        last_symbol = False
        success = True

        for address in self.address_book_model.addresses:

            success = True

            #automatically set final symbol to symbol with code 1 as the terminator
            if address.symbol7 == None and address.symbol8 == None and address.symbol9 == None:
                address.symbol7 = SymbolModel("1")

            elif address.symbol8 == None and address.symbol9 == None:
                address.symbol8 = SymbolModel("1")

            elif address.symbol9 == None:
                address.symbol9 = SymbolModel("1")

            check_string = "Check address: "+str(address.symbol1.code)+"-"+str(address.symbol2.code)+"-"+str(address.symbol3.code)+"-"\
                           +str(address.symbol4.code)+"-"+str(address.symbol5.code)+"-"+str(address.symbol6.code)+"-"

            if address.symbol7 is not None:
                check_string += address.symbol7.code+"-"

            if address.symbol8 is not None:
                check_string += address.symbol8.code+"-"

            if address.symbol9 is not None:
                check_string += address.symbol9.code

            print check_string

            print "against address: "+str(symbol1)+"-"+str(symbol2)+"-"+str(symbol3)+"-"+str(symbol4)+"-"+str(symbol5)+\
                  "-"+str(symbol6)+"-"+str(symbol7)+"-"+str(symbol8)+"-"+str(symbol9)

            #match entered symbols against gate addresses
            if str(address.symbol1.code) == str(symbol1) and str(address.symbol2.code) == str(symbol2) and str(address.symbol3.code) == str(symbol3) and str(address.symbol4.code) == str(symbol4) and str(address.symbol4.code) == str(symbol4) and str(address.symbol5.code) == str(symbol5) and str(address.symbol6.code) == str(symbol6):
                pass
            else:
                success = False

            if (address.symbol7 is not None and symbol7 != '') and str(address.symbol7.code) == str(symbol7):
                pass
            elif address.symbol7 is None and symbol7 == '':
                pass
            else:
                success = False

            if (address.symbol8 is not None and symbol8 != '') and str(address.symbol8.code) == str(symbol8):
                pass
            elif address.symbol8 is None and symbol8 == '':
                pass
            else:
                success = False

            if (address.symbol9 is not None and symbol9 != '') and str(address.symbol9.code) == str(symbol9):
                pass
            elif address.symbol9 is None and symbol9 == '':
                pass
            else:
                success = False

            if success:
                break

        dial_symbols = [symbol1, symbol2, symbol3, symbol4, symbol5, symbol6, symbol7]

        if symbol8 != '':
            dial_symbols.append(symbol8)

        if symbol9 != '':
            dial_symbols.append(symbol9)

        for dial_symbol in dial_symbols:

            if dial_symbols[len(dial_symbols)-1] == dial_symbol:
                last_symbol = True

            event.post(Event(EventType.SOUND_PLAY, {
                "value": "dhd-button-press-auto"
            }))

            if success and last_symbol:
                event.post(Event(EventType.SOUND_ADD_TO_QUEUE, {
                    "value": "gate-engage"
                }))

                event.post(Event(EventType.SOUND_LOOPING_PLAY_WHEN_IDLE, {
                    "value": "gate-loop"
                }))

            elif not success and last_symbol:
                event.post(Event(EventType.SOUND_ADD_TO_QUEUE, {
                    "value": "gate-no-engage"
                }))

            else:
                event.post(Event(EventType.SOUND_ADD_TO_QUEUE, {
                    "userevent_type": "sound-queued",
                    "value": "gate-dial-single"
                }))

            if last_symbol:
                break


        print "Dialing success: "+str(success)