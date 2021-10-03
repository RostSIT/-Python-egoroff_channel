class Zebra:

    def __init__(self):
        self.count = 1

    def which_stripe(self):
        if self.count % 2 > 0:
            print(f'Полоска белая')
        else:
            print(f'Полоска черная')
        self.count += 1
