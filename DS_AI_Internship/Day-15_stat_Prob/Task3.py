# Given probabilities
p_A = 0.1
p_B = 0.9

p_free_given_spam = 0.9
p_free_given_ham = 0.05

# Total probability of "Free"
p_free = (p_free_given_spam * p_A) + \
         (p_free_given_ham * p_B)

# Bayes Theorem
p_A_given_free = (p_free_given_spam * p_A) / p_free

print("Probability of Spam given 'Free' =", p_A_given_free)
 