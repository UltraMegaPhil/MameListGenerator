import xml.etree.cElementTree as et
import re
from rom_record import RomRecord

DESCRIPTION_KEY = "description"
MANUFACTURER_KEY = "manufacturer"
YEAR_KEY = "year"
INPUT_KEY = "input"
BUTTONS_KEY = "buttons"
PLAYERS_KEY = "players"
DISPLAY_KEY = "display"
DISPLAY_TYPE_KEY = "type"
ROTATION_KEY = "rotate"

CATEGORY_KEY = "Category"
VER_ADDED_KEY = "VerAdded"


#####################################################################
#                                                                   #
# Quick and dirty utility class for parsing MAME XML and catver.ini #
# files into a single set of records                                #
#                                                                   #
#####################################################################
class MultiParser:

    def __init__(self):
        self.roms = dict()

    def getRomRecords(self, romNameList):
        newList = []
        for romName in romNameList:
            if romName in self.roms:
                newList.append(self.roms[romName])
        return newList

    def getAllRomRecords(self):
        return self.roms
        
    def getRomRecord(self, romName):
        return self.roms[romName] 
        
    def getRomValue(self, romName, key):
        if romName in self.roms:
            return self.roms[romName].getRecordValue(key)
        else:
            return None

    # Parse in the catver.ini file
    def readCatverIni(self, fileName):
        file = open(fileName)
        
        currentBlock = ""
        for line in file:
            if(not line or line.startswith(";;")):      # Line is a comment or blank, ignore
                continue
            elif(line.startswith("[")):                 # Line is a new block value
                blockValue = re.search(r'\[(.*?)\]', line).group(1)
                if blockValue:
                    currentBlock = blockValue
            else:                                       # Line is a ROM definition
                name, value = line.partition("=")[::2]
                romName = name.strip()
                romValue = value.strip()

                # Sanity check everything
                if not romName or not romValue or not currentBlock:
                    continue
                
                # Grab the ROM record and update the key field
                rom = None
                if romName in self.roms:
                    rom = self.roms[romName]
                else:
                    rom = RomRecord(romName)
                    self.roms[romName] = rom
                    
                rom.setRecordValue(currentBlock, romValue)
                
        file.close()
    
    # Parse in the MAME XML db
    def readMAMEXML(self, fileName):
        gametree = et.parse(fileName)
        root = gametree.getroot()

        for game in gametree.findall("game"):
            romName = game.get("name")                        # ROM Name (e.g. 'dkong')
            if not romName:
                continue
            
            # Find all the tags we're interested in
            descriptionTag = game.find(DESCRIPTION_KEY)
            manufacturerTag = game.find(MANUFACTURER_KEY)
            yearTag = game.find(YEAR_KEY)
            inputTag = game.find(INPUT_KEY)
            displayTag = game.find(DISPLAY_KEY)
            
            # Grab the ROM record and update the key field
            if romName not in self.roms:
                self.roms[romName] = RomRecord(romName)
            rom = self.roms[romName]
            
            # Set attribute values
            if descriptionTag is not None and descriptionTag.text:
                rom.setRecordValue(DESCRIPTION_KEY, descriptionTag.text)

            if manufacturerTag is not None and manufacturerTag.text:
                rom.setRecordValue(MANUFACTURER_KEY, manufacturerTag.text)

            if yearTag is not None and yearTag.text:
                rom.setRecordValue(YEAR_KEY, yearTag.text)
                
            if inputTag is not None:
                players = inputTag.get(PLAYERS_KEY)
                if players:
                    rom.setRecordValue(PLAYERS_KEY, players)
                
                buttons = inputTag.get(BUTTONS_KEY)
                if buttons:
                    rom.setRecordValue(BUTTONS_KEY, buttons)
            
            if displayTag is not None:
                displayType = displayTag.get(DISPLAY_TYPE_KEY)
                if displayType:
                    rom.setRecordValue("displayType", displayType)
                
                rotation = displayTag.get(ROTATION_KEY)
                if rotation:
                    rom.setRecordValue("rotation", rotation)

