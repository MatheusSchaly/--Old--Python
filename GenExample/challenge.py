def odd_generator():
    odd_number = 1
    while True:
        yield odd_number
        odd_number += 2


def pi_series():
    odds = odd_generator()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(10000000):
    print(next(approx_pi))