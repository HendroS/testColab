# - Latihan membuat model laptop:
#     - attributes: power
#     - behavior:
#         - play_game(duration): 1% per 1 minutes (1% per minute)
#         - coding(duration): 1% per 10 minute (0,1% per minute )
#         - browsing(duration): 2% per 10 minutes (0,2% per minute)
#         - play_audio(duration): 5% per 10 minutes (0,5% per minute)
#         - charge(duration): 1% per minute
#     - what is the power level after:
#         - charge 2 hours
#         - play game 1 hour
#         - browsing 1 hour
#         - charge 20 minutes
#         - coding 2 hours
#         - play audio 2 hours 

class Laptop:
    def __init__(self) -> None:
         self.power = 0
         
    def sisa_batre(self):
        print(f'Battery  Remains {int(self.power)} %')
            
    def charging(self, duration):
        self.power = int(self.power + duration)
        print(f'Charging ')
        if self.power >= 100:
            self.power = 100
            print('Battery Is Full')
        else :
            print(f'Battery is {self.power} %')
                  
    def play_game(self, duration):
        play_duration = int(self.power)
        self.power = self.power - duration
        if self.power < 0:
            self.power = 0
            print(f'Gaming Duration Only {play_duration} Minutes')
        else :
            print(f'Gaming Duration {duration} Minutes')
    
    def coding(self, duration):
        coding_duration = int(self.power)
        self.power = self.power - (duration / 10)
        if self.power < 0:
            self.power = 0
            print(f'Coding Duration Only {coding_duration} Minutes')
        else :
            print(f'Coding Duration {duration} Minutes')
        
    def browsing(self, duration):
        browsing_duration = int(self.power)
        self.power = self.power - (duration / 5)
        if self.power < 0:
            self.power = 0
            print(f'Browsing Duration Only {browsing_duration} Minutes')
        else :
            print(f'Browsing Duration {duration} Minutes')
        
    def play_audio(self, duration):
        Audio_duration = int(self.power)
        self.power = self.power - (duration / 2)
        if self.power < 0:
            self.power = 0
            print(f'Play Audio Duration Only {Audio_duration} Minutes')
        else :
            print(f'Play Audio Duration {duration} Minutes')
        
def main():
    lenovo = Laptop()
    lenovo.charging(30)
    lenovo.play_game(30)
    lenovo.browsing(60)
    lenovo.charging(20)
    lenovo.coding(120)
    lenovo.play_audio(120)
    
    lenovo.sisa_batre()
main()
        
# def main():
#     lenovo = Laptop()
#     lenovo.charging(int(input('Charging Duration = ')))
#     lenovo.play_game(int(input('Play Game Duration = ')))   
#     lenovo.coding(int(input('Coding Duration = ')))
#     lenovo.browsing(int(input('Browsing Duration = ')))
#     lenovo.play_audio(int(input('Play Audio Duration = ')))
    
#     print(lenovo.power)
    
# main()
    
    
    
    

