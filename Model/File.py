class File:
    def __init__(self, path):
        self.path = path
        self.numbers = []

    def read(self):
        with open(self.path, 'r') as file:
            numbers = [line.strip() for line in file.readlines()]
        for number in numbers:
            number = number.replace(',', '.')
            count = 0
            for i in number:
                if i == '.':
                    count += 1
            if count > 1:
                print('El número', number, 'no es válido, por lo tanto no se tendra en cuenta.')
            else:
                self.numbers.append(float(number))
            count = 0

    def view(self):
        print('Los numeros del archivo son estos: ', self.numbers)