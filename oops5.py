#multilevel inheritance
class electronic:
    motherboard=4
    circuit=10
    _pro=38
    __private=9

    def detail(self):
        return f"No of motherboard {self.motherboard} and circuit{self.circuit}"
    
class phonegadget(electronic):
    motherboard=5
    gps=1
    sim=1
    def detail(self):
        return f"No of motherboard{self.motherboard} and gps is{self.gps} and sim is{self.sim} "
class phone(phonegadget):
    motherboard=5
    gps=2
    screentouch=1

    def detail(self):
        return f"No of motherboard{self.motherboard} and gps is{self.gps} and screentouch is{self.screentouch} and circuit is {self.circuit} "

tv=electronic()
ipod=phonegadget()
iphone=phone()
print(tv.detail())
print(ipod.detail())
print(iphone.detail())
print(iphone.circuit)
print(iphone._pro)
print(tv._electronic__private)