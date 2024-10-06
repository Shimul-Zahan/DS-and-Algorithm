def factors(number, kth):
    array = []
    for i in range(1, number+1):
        if number % i == 0:
            array.append(i)
    for index in range(0, len(array)):
        if index == kth - 1:
            return array[index]
        else: return -1

print(factors(4, 4))