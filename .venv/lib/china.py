b = 20
c = [1,2,3]

prime_numbers = [2,3,5,11,23,29,53]
def is_prime(num):
    """
    Checks if a number is prime
    :param num: the number to check
    :return: True/False
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print("Testing the prime function")
print("Prime numbers:")
for i in prime_numbers:
    print(f"{i} is prime = {is_prime(i)}")

    print("Non Prime numbers:")
    for i in non_prime_numbers:
        print(f"{i} is prime")

