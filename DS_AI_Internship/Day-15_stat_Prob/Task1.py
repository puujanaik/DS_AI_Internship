import random
# This allows us to generate random numbers.

# Number of simulations
trials = 1000
count_sum_7 = 0

for _ in range(trials):
#     This loop runs 1000 times.
# _ means we don’t care about the loop variable.
# Each loop = one experiment (rolling two dice once).
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    # random number between 1 and 6.
    
    if dice1 + dice2 == 7:
        count_sum_7 += 1

# Experimental probability
experimental_probability = count_sum_7 / trials

# P(E)= Total trials
#       Favorable outcomes
# 	​
# Probability= 1000
#             Number of times sum was 7


print("Number of times sum was 7:", count_sum_7)
print("Experimental Probability:", experimental_probability)
