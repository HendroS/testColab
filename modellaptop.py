class laptop:
    def __init__(self) -> None:
        self.power = 0
    def charge(self,duration):
        self.power = self.power + duration
        if self.power > 100:
            self.power = 100

            print(f'Charging.....Battery Power is {self.power} %')
        else:
            print(f'Charging.....Battery Duration {duration} Minutes')
    def play_game(self,duration):
        self.power = self.power -  duration
        if self.power > 100:
            self.power = 100
            print(f'Play game Duration = {duration} Minutes' )
        else:
            print(f'Daya Battery .... {self.power} %')
    def coding(self,duration):
        self.power = self.power - (duration / 10)
        if self.power < 0:
            self.power = 0
            print(f'Coding Duration = {duration} Minutes')
        elif self.power > 0:
            print(f'Baterry Daya Consumsion .. {self.power} %')
    def browsing(self,duration):
        self.power = self.power - (duration / 5)
        if self.power < 20 or self.power <= 0:
            self.power = 0
            print(f'Browsing Duration = {duration} Minutes')
        else:
            print(f'Browsing Daya Consumsion {self.power} %')
    def play_audio(self,duration):
        self.power = self.power - (duration / 2)
        if self.power < 0:
            self.power = 0
            print(f'Play Audio Duration = {duration} Minutes')
        else:
            print(f'Play Audio Consumsion Daya  {self.power} %')
            
# inputan   # 
# def main():
#     omen = laptop()
#     omen.charge(int(input('charging duration = ')))
#     omen.play_game(int(input('play_game duration = ')))
#     omen.browsing(int(input('browsing duration = ')))
#     omen.coding(int(input('coding duration = ')))
#     omen.play_audio(int(input('play_audio duration = ')))
#     print(omen.power)
# main()
def main():
    omen = laptop()
    omen.charge(120)
    omen.play_game(60)
    omen.browsing(60)
    omen.charge(20)
    omen.coding(120)
    omen.play_audio(120)
    print(omen.power)
main()