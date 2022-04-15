class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if (Singleton.__instance == None):
            Singleton()
        return __instance
    
    def __init__(self):
        if (Singleton.__instance != None):
            raise Exception("Singleton exists already!")
        else:
            Singleton.__instance = self


# Test
sample1 = Singleton()
print(sample1)

sample2 = Singleton()
print(Singleton())