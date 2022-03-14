class Pet():

    def __init__(self, name):
            self.name=name

    def sayhi(self):
            print ("Hi! My name is ", self.name)

def Pet2(name):
    return {
            "name":name,
            "greeting":f"Hi! My name is {name}"
            }
dogs = [Pet2(n) for n in ["Suzzy","Dorothy","Heidi","Casey"]]
print(dogs)

