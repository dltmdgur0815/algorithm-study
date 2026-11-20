class ChainingTable:
    def __init__(self, size=5):
        if size <= 0:
            raise ValueError('size must be positive')
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def put(self, number, name):
        address = number % len(self.buckets)
        bucket = self.buckets[address]
        for index, item in enumerate(bucket):
            if item[0] == number:
                bucket[index] = (number, name)
                return
        bucket.append((number, name))
        self.count += 1
        if self.count > len(self.buckets) * 0.75:
            self.resize(len(self.buckets) * 2 + 1)

    def resize(self, new_size):
        new_buckets = [[] for _ in range(new_size)]
        for bucket in self.buckets:
            for number, name in bucket:
                address = number % new_size
                new_buckets[address].append((number, name))
        self.buckets = new_buckets

    def get(self, number):
        address = number % len(self.buckets)
        for saved_number, name in self.buckets[address]:
            if saved_number == number:
                return name
        raise KeyError(number)
