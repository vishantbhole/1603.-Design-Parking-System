class ParkingSystem(object):
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small
        
    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1 and self.big > 0:
            self.big = self.big - 1
            return True
        if carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        if carType == 3 and self.small > 0:
            self.small -= 1
            return True
        return False
if __name__ == "__main__":
    obj = ParkingSystem(1, 1, 0)
    print(obj.addCar(1))  # True
    print(obj.addCar(2))  # True
    print(obj.addCar(3))  # False
    print(obj.addCar(1))  # False
