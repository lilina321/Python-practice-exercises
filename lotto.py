import random

def choose_random_numbers(amount, totalAmount):
    numbers = []
    while len(numbers) < 6:
        number = random.randint(1, totalAmount)
        if number not in numbers:
            numbers.append(number)
        else:
            continue
    return numbers


#sample method - numbers without duplicates

def choose_random_numbers2(amount, totalAmount):
    return random.sample(range(1, totalAmount + 1), amount)


print(choose_random_numbers(6, 49))
print(choose_random_numbers2(6, 49))
