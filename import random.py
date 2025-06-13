import random
def get_numbers_ticket(min_val, max_val, quantity):
    if min_val < 1 or max_val > 1000 or min_val > max_val:
        return []
    
    if quantity > (max_val - min_val + 1):
        return []
    
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    return sorted(numbers)    

lottery_numbers = get_numbers_ticket(2,50, 9)
print("Ваші лоьарейні числа", lottery_numbers)