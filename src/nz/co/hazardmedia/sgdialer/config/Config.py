__author__ = 'Michael Andrew michael@hazardmedia.co.nz'


class Config(object):
    point_of_origin_code = 0 #index of the point of origin

    address_data_file_path = "data/addresses.xml" #path from src folder to data file for stargate addresses

    #use font Stargate SG-1 Address Glyphs
    address_symbol_names = {#names of the symbols on the stargate and dhd
                            "?": "Unknown",
                            "1": "Earth", #A
                            #point of origin (in our alternate universe the point of origin acts as a terminator and is
                            #can be the same on all DHDs)
                            "2": "Crater", #B
                            "3": "Virgo", #C
                            "4": "Bootes", #D
                            "5": "Centaurus", #E
                            "6": "Libra", #F
                            "7": "Serpens Caput", #G
                            "8": "Norma", #H
                            "9": "Scorpio", #I
                            "10": "Cra", #J
                            "11": "Scutum", #K
                            "12": "Sagittarius", #L
                            "13": "Aquila", #M
                            "14": "Mic", #N
                            "15": "Capricorn", #O
                            "16": "Pisces Austrinus", #P
                            "17": "Equuleus", #Q
                            "18": "Aquarius", #R
                            "19": "Pegasus", #S
                            "20": "Sculptor", #T
                            "21": "Pisces", #U
                            "22": "Andromeda", #V
                            "23": "Triangulum", #W
                            "24": "Aries", #X
                            "25": "Perseus", #Y
                            "26": "Cetus", #Z
                            "27": "Taurus", #a
                            "28": "Auriga", #b
                            "29": "Eridanus", #c
                            "30": "Orion", #d
                            "31": "Canis Minor", #e
                            "32": "Monoceros", #f
                            "33": "Gemini", #g
                            "34": "Hydra", #h
                            "35": "Lynx", #i
                            "36": "Cancer", #j
                            "37": "Sextans", #k
                            "38": "Leo Minor", #l
                            "39": "Leo" #m
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