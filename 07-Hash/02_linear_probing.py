class LinearTable:
    def __init__(self, size=5):
        if size <= 0:
            raise ValueError('size must be positive')
        self.slots = [None] * size

    def put(self, number, name):
        size = len(self.slots)
        for step in range(size):
            address = (number + step) % size
            item = self.slots[address]
            if item is None or item[0] == number:
                self.slots[address] = (number, name)
                return address
        raise OverflowError('hash table is full')

    def get(self, number):
        size = len(self.slots)
        for step in range(size):
            address = (number + step) % size
            item = self.slots[address]
            if item is None:
                break
            if item[0] == number:
                return item[1]
        raise KeyError(number)
