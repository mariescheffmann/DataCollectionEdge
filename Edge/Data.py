class Data:
    def __init__(self, name, value, realTimeDatabase):
        self.name = name
        self.value = value
        self.realTimeDatabase = realTimeDatabase

    def prepareData(self):
        print(f"Name: {self.name} value: {self.value} realTimeDatabase: {self.realTimeDatabase}.")
