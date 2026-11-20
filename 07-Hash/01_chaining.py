class ChainingTable:
    def __init__(self, size=5):
        if size <= 0:
            raise ValueError('size must be positive')
        self.buckets = [[] for _ in range(size)]

    def put(self, number, name):
        address = number % len(self.buckets)
        bucket = self.buckets[address]
        for index, item in enumerate(bucket):
            if item[0] == number:
                bucket[index] = (number, name)
                return
        bucket.append((number, name))

    def get(self, number):
        address = number % len(self.buckets)
        for saved_number, name in self.buckets[address]:
            if saved_number == number:
                return name
        raise KeyError(number)
