from rom_record import RomRecord
import os

class RomLister:

    def __init__(self, romPath, imgPath, romExtension, imgExtension):
        self.romPath = romPath if romPath else ""
        self.imgPath = imgPath if imgPath else ""
        self.romExtension = romExtension if romExtension else ""
        self.imgExtension = imgExtension if imgExtension else ""
        
    def printAttractModeList(self, roms):
        print "#" \
                "Name;" \
                "Title;" \
                "Emulator;" \
                "CloneOf;" \
                "Year;" \
                "Manufacturer;" \
                "Category;" \
                "Players;" \
                "Rotation;" \
                "Control;" \
                "Status;" \
                "DisplayCount;" \
                "DisplayType;" \
                "AltRomname;" \
                "AltTitle;" \
                "Extra;" \
                "Buttons"
        
        for rom in roms:
            emulator = "M.A.M.E."
            
            record = rom.getName() + ";"
            record += rom.getRecordValue("description") + ";"
            record += emulator + ";"
            record += rom.getRecordValue("cloneOf") + ";"
            record += rom.getRecordValue("year") + ";"
            record += rom.getRecordValue("manufacturer") + ";"
            record += rom.getRecordValue("Category") + ";"
            record += rom.getRecordValue("players") + ";"
            record += rom.getRecordValue("rotation") + ";"
            record += rom.getRecordValue("control") + ";"
            record += rom.getRecordValue("status") + ";"
            record += rom.getRecordValue("displayCount") + ";"
            record += rom.getRecordValue("displayType") + ";"
            record += rom.getRecordValue("altRomName") + ";"
            record += rom.getRecordValue("altTitle") + ";"
            record += rom.getRecordValue("extra") + ";"
            record += rom.getRecordValue("buttons")
            
            print record

    def printEmulationStationGamelistXML(self, roms):
        print "<gameList>"
        
        for rom in roms:
        
            romName = rom.getName()
            imgName = rom.getName()
                
            if self.romPath:
                romName = self.romPath + os.path.sep + romName
            if self.imgPath:
                imgName = self.imgPath + os.path.sep + imgName
            if self.romExtension:
                romName = romName + "." + self.romExtension
            if self.imgExtension:
                imgName = imgName + "." + self.imgExtension
        
        
            print "  <game>"
        
            print "    <path>" + romName + "</path>"
            print "    <name>" + rom.getRecordValue('description') + "</name>"
            print "    <image>" + imgName + "</image>"
            print "    <releasedate>" + rom.getRecordValue('year') + "0101T000000</releasedate>" 
            print "    <developer>" + rom.getRecordValue('manufacturer') + "</developer>"
            print "    <genre>" + rom.getRecordValue('Category') + "</genre>"
            print "    <players>" + rom.getRecordValue('players') + "</players>"
            
            print "  </game>"
        
        print "</gameList>"
        
        



