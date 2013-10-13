__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from nz.co.hazardmedia.sgdialer.config.Config import Config


class SymbolModel(object):

    name = ""
    code = None
    font_code = ""

    def __init__(self, code):
        self.character_code = code

        #print "Character code: "+code

        self.name = Config.address_symbol_names[code]
        #self.font_code = Config.address_symbol_names[code]

        print "Symbol name: "+self.name