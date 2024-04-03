class Numbers:
    def __init__(self):
        pass

    def average(numbers):
        sum = 0
        for number in numbers:
            sum = sum + number
        return sum / len(numbers)
    
    def variance(numbers):
        n = len(numbers)
        sum = 0
        average = Numbers.average(numbers)
        for number in numbers:
            sum = sum + pow((number - average), 2)
        return round(sum / n, 2)
    
    def median(numbers):
        numbers.sort()
        if len(numbers) % 2 == 0:
            half = int(len(numbers) / 2)
            return round((numbers[half - 1] + numbers[half]) / 2, 2)
        else: 
            return round(numbers[len(numbers) // 2], 2)