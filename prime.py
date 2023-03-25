def prime_numbers(low,high):
    result = []
    if type(high) == float: high = int(high)
    if type (low) == float: low = int(low)+1
    if (type (low) == type (high) == int) and low < high:
        if low < 2: # отсекаем всё что меньше двух, так как всё что меньше 2-х не является простыми числами (0 и 1 тоже)
            low = 2
        buffer = list(range(low,high+1))  # заполняем буффер целыми числами от low до high
        for i in range(2,high+1):
            for j in range(2,high+1):
                if i!= 1 and j!=i and j%i == 0 and buffer.count(j) != 0:  
                    buffer.remove(j) # Удаляем все числа, которые не ялвляются простыми
        result = buffer 
    return result

print(prime_numbers(2.01,10.))