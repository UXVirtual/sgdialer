__author__ = 'Michael Andrew michael@hazardmedia.co.nz'

class Config(object):
    """ Config class """
    sound_path = 'assets/sounds' #path from src folder to sound assets

    point_of_origin_code = 0 #index of the point of origin

    address_data_file_path = "data/addresses.xml" #path from src folder to data file for stargate addresses

    #use font Stargate SG-1 Address Glyphs
    address_symbol_names = {#names of the symbols on the stargate and dhd
                            "?": "Unknown",
                            "1": "Earth", #letter A, key 1
                            #point of origin (in our alternate universe the point of origin acts as a terminator and is
                            #can be the same on all DHDs)
                            "2": "Crater", #letter B, key 2
                            "3": "Virgo", #letter C, key 3
                            "4": "Bootes", #letter D, key 4
                            "5": "Centaurus", #letter E, key 5
                            "6": "Libra", #letter F, key 6
                            "7": "Serpens Caput", #letter G, key 7
                            "8": "Norma", #letter H, key 8
                            "9": "Scorpio", #letter I, key 9
                            "10": "Cra", #letter J, key 0
                            "11": "Scutum", #letter K, key - (hyphen)
                            "12": "Sagittarius", #letter L, key q
                            "13": "Aquila", #letter M, key w
                            "14": "Mic", #letter N, key e
                            "15": "Capricorn", #letter O, key r
                            "16": "Pisces Austrinus", #letter P, key t
                            "17": "Equuleus", #letter Q, key y
                            "18": "Aquarius", #letter R, key u
                            "19": "Pegasus", #letter S, key i
                            "20": "Sculptor", #letter T, key o
                            "21": "Pisces", #letter U, key p
                            "22": "Andromeda", #letter V, key a
                            "23": "Triangulum", #letter W, key s
                            "24": "Aries", #letter X, key d
                            "25": "Perseus", #letter Y, key f
                            "26": "Cetus", #letter Z, key g
                            "27": "Taurus", #letter a, key h
                            "28": "Auriga", #letter b, key j
                            "29": "Eridanus", #letter c, key k
                            "30": "Orion", #letter d, key l
                            "31": "Canis Minor", #letter e, key z
                            "32": "Monoceros", #letter f, key x
                            "33": "Gemini", #letter g, key c
                            "34": "Hydra", #letter h, key v
                            "35": "Lynx", #letter i, key b
                            "36": "Cancer", #letter j, key n
                            "37": "Sextans", #letter k, key m
                            "38": "Leo Minor", #letter l, key , (comma)
                            "39": "Leo" #letter m, key . (period)
    }

    address_symbol_font_character = { #mappings of address symbol to font character
        "1":"A",
        "2":"B",
        "3":"C",
        "4":"D",
        "5":"E",
        "6":"F",
        "7":"G",
        "8":"H",
        "9":"I",
        "10":"J",
        "11":"K",
        "12":"L",
        "13":"M",
        "14":"N",
        "15":"O",
        "16":"P",
        "17":"Q",
        "18":"R",
        "19":"S",
        "20":"T",
        "21":"U",
        "22":"V",
        "23":"W",
        "24":"X",
        "25":"Y",
        "26":"Z",
        "27":"a",
        "28":"b",
        "29":"c",
        "30":"d",
        "31":"e",
        "32":"f",
        "33":"g",
        "34":"h",
        "35":"i",
        "36":"j",
        "37":"k",
        "38":"l",
        "39":"m"

    }