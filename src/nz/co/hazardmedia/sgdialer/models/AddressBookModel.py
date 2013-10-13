__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

import os
import xmltodict
from nz.co.hazardmedia.sgdialer.config.Config import Config
from nz.co.hazardmedia.sgdialer.models.AddressModel import AddressModel

class AddressBookModel(object):

    addresses = []

    def __init__(self):
        self.import_data()
        pass

    def import_data(self):
        print "Importing stargate addresses from data source..."

        data_file = open(os.getcwd()+"\\"+Config.address_data_file_path)
        xml = data_file.read()
        parsed_xml = xmltodict.parse(xml)

        address_data = parsed_xml["addresses"]["address"]

        #print address_data

        for address in address_data:

            #get address lock status
            locked = False

            if address["locked"]:
                locked = True

            symbol1 = "",
            symbol2 = "",
            symbol3 = "",
            symbol4 = "",
            symbol5 = "",
            symbol6 = "",
            symbol7 = "",
            symbol8 = "",
            symbol9 = ""

            symbols = str(address["symbols"]).split("-")

            #print symbols

            try:
                symbol1 = symbols[0]
            except IndexError:
                pass

            try:
                symbol2 = symbols[1]
            except IndexError:
                pass

            try:
                symbol3 = symbols[2]
            except IndexError:
                pass

            try:
                symbol4 = symbols[3]
            except IndexError:
                pass

            try:
                symbol5 = symbols[4]
            except IndexError:
                pass

            try:
                symbol6 = symbols[5]
            except IndexError:
                pass

            try:
                symbol7 = symbols[6]
            except IndexError:
                symbol7 = ""
                pass

            try:
                symbol8 = symbols[7]
            except IndexError:
                symbol8 = ""
                pass

            try:
                symbol9 = symbols[8]
            except IndexError:
                symbol9 = ""
                pass

            self.addresses.append(
                AddressModel(
                    address["name"],
                    address["id_code"],
                    str(symbol1),
                    str(symbol2),
                    str(symbol3),
                    str(symbol4),
                    str(symbol5),
                    str(symbol6),
                    str(symbol7),
                    str(symbol8),
                    str(symbol9),
                    locked,
                    address["description"]
                )
            )

            print "Imported address."
            #print address["name"]

        #print xml

        print "Addresses imported."

        print self.addresses