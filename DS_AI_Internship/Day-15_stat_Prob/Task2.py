import random

# Independent Event
print("Independent Event")

p_heads = 1/2
p_six = 1/6
print("Probability of Heads AND 6 =", p_heads * p_six)

# Probability of Heads = 1/2
# Probability of rolling 6 = 1/6
# P(A∩B)=P(A)×P(B)
#  = 1/2*1/6=1/12  

  
# Dependent Event
print("\nDependent Event")

p_first_red = 5/10
p_second_red = 4/9
print("Probability of both Red =", p_first_red * p_second_red)


# Simple Simulation (Dice Sum = 7)
print("\nSimulation of Dice (1000 times)")

count = 0
for i in range(1000):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    
    if d1 + d2 == 7:
        count += 1

print("Experimental Probability of sum 7 =", count/1000)
