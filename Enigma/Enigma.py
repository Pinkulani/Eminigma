from Modules.Converter import *
from Data import *

class Enigma:
    def __init__(self):
        self.Settings("I")
        self.Debug = True

    def Settings(self, Model):
        match Model:
            case "I":
                Static = 0
                System = 0
                Rotors = ["I", "II", "III"]
                Reflector = "B"
            case "M3":
                Static = 0
                System = 0
                Rotors = ["VI", "VII", "VIII"]
                Reflector = "B"
            case "M4":
                Static = 0
                System = 0
                Rotors = ["VI", "VII", "VIII"]
                Extra = "Beta"
                Reflector = "B-M4"

        if Model == "M4":
            self.Data = Data(Static, System, Rotors, Reflector, Extra)
        else:
            self.Data = Data(Static, System, Rotors, Reflector)

        self.Setup()
    
    def Setup(self):
        self.Static = self.Data.ReturnStatic()
        self.System = self.Data.ReturnSystem()
        self.Wiring = self.Data.ReturnWiring()
        self.Notches = self.Data.ReturnNotches()
        self.Reflector = self.Data.ReturnReflector()
        self.Extra = self.Data.ReturnExtra()

        self.Converter = Converter(self.System)

if __name__ == "__main__":
    App = Enigma()
