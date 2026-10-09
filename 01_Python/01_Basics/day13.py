# def prime_check(num):

#     is_prime = True

#     for i in range(2,num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not prime")

# prime_check(30)

def calculate_average(numbers):
    total = 0

    for number in numbers:
        total = total + number

    average = total / len(numbers)

    return average


scores = [80, 90, 70]

print(calculate_average(scores))