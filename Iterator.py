class Itrator:
    def __init__(self, item) -> None:
        self.item = item
        self.index = 0
    
    def count(self):
        return len(self.item)
    
    def hasNext(self):
        return (self.index < self.count())

    def next(self):
        if self.hasNext():
            result = self.item[self.index]
            self.index = self.index + 1
        else:
            result = None
            self.index = self.count() + 1
        return result
    
    def first(self):
        if self.count() > 0:
            self.index = 0
            return self.item[self.index]
        else:
            return None

    def last(self):
        if self.count() > 0:
            self.index = self.count() - 1
            return self.item[self.index]
        else:
            return None


# Test
sample = Itrator(["Sam", 24, True, 157.4, "Alex"])

while sample.hasNext():
    print(sample.next())
