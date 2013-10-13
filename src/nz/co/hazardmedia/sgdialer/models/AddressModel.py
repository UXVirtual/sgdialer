__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

from nz.co.hazardmedia.sgdialer.models.SymbolModel import SymbolModel


class AddressModel(object):
    name = ""
    id_code = ""
    symbol1 = None
    symbol2 = None
    symbol3 = None
    symbol4 = None
    symbol5 = None
    symbol6 = None
    symbol7 = None
    symbol8 = None
    symbol9 = None #this symbol may not be required for the address book as this should be the point of origin
    locked = False
    description = ""

    def __init__(self, name, id_code, symbol1, symbol2, symbol3, symbol4, symbol5, symbol6,
                 symbol7="", symbol8="", symbol9="", locked=False, description=""):
        self.name = name
        self.id_code = id_code
        self.locked = locked
        self.description = description
        self.symbol1 = SymbolModel(symbol1)
        self.symbol2 = SymbolModel(symbol2)
        self.symbol3 = SymbolModel(symbol3)
        self.symbol4 = SymbolModel(symbol4)
        self.symbol5 = SymbolModel(symbol5)
        self.symbol6 = SymbolModel(symbol6)
        self.symbol7 = SymbolModel(symbol7) if symbol7 != "" else None
        self.symbol8 = SymbolModel(symbol8) if symbol8 != "" else None
        self.symbol9 = SymbolModel(symbol9) if symbol9 != "" else None

    def __repr__(self):
        return 'AddressModel(%s)' % self.name