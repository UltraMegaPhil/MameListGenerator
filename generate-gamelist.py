import sys, getopt

from multi_parser import MultiParser
from rom_lister import RomLister


# Output modes
ATTRACTMODE = "am"
EMULATIONSTATIONMODE = "es"

# Inputs
romlist = []
inputRomFile = ""
mameXMLFile = ""
catverFile = ""
outputFormat = ""
outputRomPath = ""
outputImgPath = ""
romFileExtension = ""
imgFileExtension = ""

# Parse the input file to create an array of rom names
def buildRomlist(fileName):
    file = open(fileName)
        
    for line in file:
        if(not line):      # Ignore blank lines
            continue
        else:
            romlist.append(line.strip())

    file.close()

# Prints the program usage options
def printUsage():
    print "Usage:"
    print " -i  : Input file (list of ROMS)                 - REQUIRED"
    print " -m  : MAME XML file                             - REQUIRED"
    print " -c  : catver.ini file                           - REQUIRED"
    print " -f  : Output file format (options: es or am)    - REQUIRED"
    print " -r  : ROM output path prefix                    - OPTIONAL - EmulationStation mode only"
    print " -p  : Image output path prefix                  - OPTIONAL - EmulationStation mode only"
    print " -z  : ROM file extension                        - OPTIONAL - EmulationStation mode only"
    print " -y  : Image file extension                      - OPTIONAL - EmulationStation mode only"
    
    
# Parse the program options
def parseOpts(argv):
    global inputRomFile
    global mameXMLFile
    global catverFile
    global outputRomPath
    global outputImgPath
    global outputFormat
    global romFileExtension
    global imgFileExtension
    
    try:
        opts, args = getopt.getopt(argv,"i:m:c:r:p:f:z:y:")
    except getopt.GetoptError:
        printUsage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == "-i":
            inputRomFile = arg
        elif opt == "-m":
            mameXMLFile = arg
        elif opt == "-c":
            catverFile = arg
        elif opt == "-r":
            outputRomPath = arg
        elif opt == "-p":
            outputImgPath = arg
        elif opt == "-z":
            romFileExtension = arg
        elif opt == "-y":
            imgFileExtension = arg
        elif opt == "-f":
            if arg == ATTRACTMODE or arg == EMULATIONSTATIONMODE:
                outputFormat = arg
            else:
                print "Error, invalid output format specified"
                printUsage()
                sys.exit(2)

    if not inputRomFile:
        print "Error - no input ROM file list provided"
        printUsage()
        sys.exit(2)
    if not mameXMLFile:
        print "Error - no MAME XML file provided"
        printUsage()
        sys.exit(2)
    if not catverFile:
        print "Error - no catver.ini file provided"
        printUsage()
        sys.exit(2)
    if not outputFormat:
        print "Error - no output format specified"
        printUsage()
        sys.exit(2)

def main(argv):
    parseOpts(argv)

    multiParser = MultiParser()
    multiParser.readCatverIni(catverFile)
    multiParser.readMAMEXML(mameXMLFile)

    buildRomlist(inputRomFile)

    roms = multiParser.getRomRecords(romlist)
    romLister = RomLister(outputRomPath, outputImgPath, romFileExtension, imgFileExtension)

    if outputFormat == ATTRACTMODE:
        romLister.printAttractModeList(roms)
    elif outputFormat == EMULATIONSTATIONMODE:
        romLister.printEmulationStationGamelistXML(roms)


if __name__ == "__main__":
   main(sys.argv[1:])

