from colored import fg,attr
class PackTwo:
    def __init__(self):
        self.name = 'PackTwo'

    def process(self):
        print("This is {}{}{}".format(fg(226),self.name, attr("reset")))
        print('This is', self.name)
        return 2
