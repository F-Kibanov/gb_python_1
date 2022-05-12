from time import sleep


class TrafficLight:
    __color = 'off'

    def running(self):
        while True:
            self.__color = 'red'
            print(self.__color)
            sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            sleep(2)
            self.__color = 'green'
            print(self.__color)
            sleep(10)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
