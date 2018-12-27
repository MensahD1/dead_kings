import random
class Dialouge:
    def __init__(self,phrases):
        self.phrases = phrases
    def selectPhrace(self):
        return random.randchoice(phrases)


test = Dialouge(["%s rushes foward and strikes the %s. Damage Done: %d"])
