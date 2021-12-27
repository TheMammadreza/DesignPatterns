class Observer:
    def __init__(self) -> None:
        self.observers = []

    def subscribe(self, fn):
        self.observers.append(fn)
    
    def unsubscribe(self, fn):
        self.observers.remove(fn)
    
    def fire(self):
        for fn in self.observers:
            fn()


# Test
sample = Observer()

ValueA = 8
ValueB = 4
def sum():
    print (ValueA + ValueB)

def sub():
    print (ValueA - ValueB)

def mul():
    print (ValueA * ValueB)

def div():
    print (ValueA / ValueB)

sample.subscribe(sum)
sample.subscribe(sub)
sample.subscribe(mul)
sample.subscribe(div)

sample.unsubscribe(mul)

sample.fire()