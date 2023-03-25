class Frequence:
    def __init__(self):
        self.opacity8 = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
                         0.25, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                         0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75,
                         0.75, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 1, 1, 1, 1, 1, 1, 1]

    def gen(self):

        for i in range(0, 7):
            self.opacity8.append(0.25)
        for i in range(7, 15):
            self.opacity8.append(0.5)
        for i in range(15, 22):
            self.opacity8.append(0.75)
        for i in range(22, 30):
            self.opacity8.append(1)
        for i in range(30, 37):
            self.opacity8.append(0.25)
        for i in range(37, 45):
            self.opacity8.append(0.5)
        for i in range(45, 53):
            self.opacity8.append(0.75)
        for i in range(53, 60):
            self.opacity8.append(1)
        print(self.opacity8)


fre = Frequence()
fre.gen()
