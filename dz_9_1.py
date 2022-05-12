from time import sleep


class TrafficLight:
    __color = 'off'

    def running(self):
        self.__color = 'red'
        print(self.__color)
        sleep(4)
        self.__color = 'yellow'
        print(self.__color)
        sleep(2)
        self.__color = 'green'
        print(self.__color)
        sleep(3)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
