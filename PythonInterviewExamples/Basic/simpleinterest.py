def simpleinterst(principle,time,rate):
    return principle*time*rate/100

print(simpleinterst(8,6,8))


"""
A = P(1 + R/100) t
Compound Interest = A – P
Where,
A is amount
P is principle amount
R is the rate and
T is the time span
"""

def compound_interest(principle, rate, time):
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)


# Driver Code
compound_interest(10000, 10.25, 5)