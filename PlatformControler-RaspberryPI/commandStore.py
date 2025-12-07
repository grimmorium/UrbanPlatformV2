import copy

class Command:
    commandID = -1
    AS1 = -1
    AS2 = -1
    AS3 = -1
    AS4 = -1
    AS5 = -1
    AS6 = -1
    ADC1 = -1
    ADC2 = -1
    
    BS1 = -1
    BS2 = -1
    BS3 = -1
    BS4 = -1
    BS5 = -1
    BS6 = -1
    BDC1 = -1
    BDC2 = -1
    
    CS1 = -1
    CS2 = -1
    CS3 = -1
    CS4 = -1
    CS5 = -1
    CS6 = -1
    CDC1 = -1
    CDC2 = -1
    
    time = -1
  
    def GetAS1(self):
        return self.AS1
    
    def GetAS2(self):
        return self.AS2
    
    def GetAS3(self):
        return self.AS3
    
    def GetAS4(self):
        return self.AS4
    
    def GetAS5(self):
        return self.AS5
    
    def GetAS6(self):
        return self.AS6
    
    def GetADC1(self):
        return self.ADC1
    
    def GetADC2(self):
        return self.ADC2
    
    def GetBS1(self):
        return self.BS1
    
    def GetBS2(self):
        return self.BS2
    
    def GetBS3(self):
        return self.BS3
    
    def GetBS4(self):
        return self.BS4
    
    def GetBS5(self):
        return self.BS5
    
    def GetBS6(self):
        return self.BS6
    
    def GetBDC1(self):
        return self.BDC1
    
    def GetBDC2(self):
        return self.BDC2
    
    def GetCS1(self):
        return self.CS1
    
    def GetCS2(self):
        return self.CS2
    
    def GetCS3(self):
        return self.CS3
    
    def GetCS4(self):
        return self.CS4
    
    def GetCS5(self):
        return self.CS5
    
    def GetCS6(self):
        return self.CS6
    
    def GetCDC1(self):
        return self.CDC1
    
    def GetCDC2(self):
        return self.CDC2
    
    def GetTime(self):
        return self.time
    
    def __init__(self, _AS1, _AS2, _AS3, _AS4, _AS5, _AS6, _ADC1, _ADC2, _BS1, _BS2, _BS3, _BS4, _BS5, _BS6, _BDC1, _BDC2, _CS1, _CS2, _CS3, _CS4, _CS5, _CS6, _CDC1, _CDC2, _time, _commandID):
        self.AS1 = _AS1
        self.AS2 = _AS2
        self.AS3 = _AS3
        self.AS4 = _AS4
        self.AS5 = _AS5
        self.AS6 = _AS6
        self.ADC1 = _ADC1
        self.ADC2 = _ADC2
        
        self.BS1 = _BS1
        self.BS2 = _BS2
        self.BS3 = _BS3
        self.BS4 = _BS4
        self.BS5 = _BS5
        self.BS6 = _BS6
        self.BDC1 = _BDC1
        self.BDC2 = _BDC2
        
        self.CS1 = _CS1
        self.CS2 = _CS2
        self.CS3 = _CS3
        self.CS4 = _CS4
        self.CS5 = _CS5
        self.CS6 = _CS6
        self.CDC1 = _CDC1
        self.CDC2 = _CDC2
        
        self.time = _time
        self.commandID = _commandID
    
    def __str__(self):
        return f"AS1: {self.AS1} AS2: {self.AS2} AS3: {self.AS3} AS4: {self.AS4} AS5: {self.AS5} AS6: {self.AS6} ADC1: {self.ADC1} ADC2: {self.ADC2} BS1: {self.BS1} BS2: {self.BS2} BS3: {self.BS3} BS4: {self.BS4} BS5: {self.BS5} BS6: {self.BS6} BDC1: {self.BDC1} BDC2: {self.BDC2} CS1: {self.CS1} CS2: {self.CS2} CS3: {self.CS3} CS4: {self.CS4} CS5: {self.CS5} CS6: {self.CS6} CDC1: {self.CDC1} CDC2: {self.CDC2} time: {self.time} commandID: {self.commandID} "
    
class ComandStore:
    commandId = 0
    lastReturnedCommandID = 0
    
    store = [Command(-1, -1, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -4, -5)];
        
    def __init__(self):
        pass
    
    def __str__(self):
        return str("CommandStore - commands in buffer:" + str(self.StoreLen()))
    
    def _getNextCommandID(self):
        tmp_commandId = self.commandId
        self.commandId = self.commandId + 1
        return tmp_commandId
    
    def AddCommand(self, _AS1, _AS2, _AS3, _AS4, _AS5, _AS6, _ADC1, _ADC2, _BS1, _BS2, _BS3, _BS4, _BS5, _BS6, _BDC1, _BDC2, _CS1, _CS2, _CS3, _CS4, _CS5, _CS6, _CDC1, _CDC2, _time):
        self.store.append(Command(_AS1, _AS2, _AS3, _AS4, _AS5, _AS6, _ADC1, _ADC2, _BS1, _BS2, _BS3, _BS4, _BS5, _BS6, _BDC1, _BDC2, _CS1, _CS2, _CS3, _CS4, _CS5, _CS6, _CDC1, _CDC2, _time, self._getNextCommandID()) )
        pass
    
    def StoreLen(self):
        return self.store.__len__()-1
    
    def RemoveCommandByCommandID(self, _CommandID):
        result = False
        
        for i in range(len(self.store)):
            if(self.store[i].commandID == _CommandID):
                self.store.pop(i)
                result = True
                break
        
        return result
    
    def DelleteAllCommands(self):
        while len(self.store)>1:
            #self.store.pop(1)
            self.GetNextCommand()
            pass
    
    def GetNextCommand(self):
        commandCopy = None
        for i in range(len(self.store)):
            if(self.store[i].commandID == self.lastReturnedCommandID):
                commandCopy = copy.deepcopy(self.store[i])
                self.store.pop(i)
                break
       
        self.lastReturnedCommandID = self.lastReturnedCommandID + 1
        return commandCopy