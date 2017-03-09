class RomRecord:

    def __init__(self, name):
        self.romName = name
        self.values = dict()
    
    def getName(self):
        return self.romName
        
    def setRecordValue(self, key, value):
        self.values[key] = value

    def getRecordValue(self, key):
        if key in self.values:
            return self.values[key]
        else:
            return ''

    def debugRecord(self):
        print "Name: " + self.romName
        for key,value in self.values.iteritems():
            print "    " + key + ": " + value
