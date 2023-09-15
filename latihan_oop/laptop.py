class Laptop:
    def __init__(self) -> None:
        self.__power = 0

    def __isDrop(self):
        return self.__power<=0
    
    def __acitivity(self,duration:int,type:str,consumtion_per_minute:float)->None:
        if self.__isDrop():
            print('Power exhausted, need to charge first')
        else:
            self.__power-=(duration*consumtion_per_minute)
            if self.__power<0:
                print(f'Only {type} for {int(duration + self.__power)} {"minutes" if duration + self.__power==1 else "Minutes"}')
                self.__power=0
            else:
                print(f'{type[0:1].upper()+type[1:]} for {duration} {"minutes" if duration + self.__power==1 else "Minutes"}')
            self.power
    def playGame(self,duration:int)->None:
        consumption=1
        self.__acitivity(duration,'play game',consumption)


    def coding(self,duration:int)->None:
        consumption=1/10
        self.__acitivity(duration,'coding',consumption)

    
    def browsing(self,duration:int)->None:
        consumption=2/10
        self.__acitivity(duration,'browsing',consumption)

    
    def playAudio(self,duration): 
        consumption=5/10
        self.__acitivity(duration,'play audio',consumption)

    
    def charge(self,duration): 
        self.__power= self.__power+ duration
        charging=duration
        if self.__power >100:
            charging=duration - (self.__power-100)
            self.__power =100
        print(f'Charging for {charging} {"minutes" if duration + self.__power==1 else "Minutes"}')
        self.power

    @property
    def power(self):
        if self.__power <= 0:
            print(f'Battery is Empty')
        elif self.__power >= 100:
            print(f'Battery is Full')
        else:            
            print(f'Remaining battery power is {int(self.__power)}%')

    
    

    



def main():
    laptop=Laptop()
    laptop.charge(120)
    laptop.playGame(60)
    laptop.browsing(60)
    laptop.charge(20)
    laptop.coding(120)
    laptop.playAudio(120)

main()




    
   