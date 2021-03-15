class time:
    def __init__(self, hour, minute, second ):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        return self.__hour + other.__hour, self.__minute + other.__minute, self.__second + other.__second
time1 = time(2,10,25)
time2 = time(3,5,20)
time3 = time1 + time2
print(time3) 