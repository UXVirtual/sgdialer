__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from nz.co.hazardmedia.sgdialer.config.Config import Config


class SymbolModel(object):

    name = ""
    character_code = None

    def __init__(self, character_code):
        self.character_code = character_code

        #print "Character code: "+character_code

        self.name = Config.address_symbol_names[character_code]

        print "Symbol name: "+self.name