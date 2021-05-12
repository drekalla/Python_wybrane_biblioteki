import string
import random
from itertools import combinations

s_alphabet = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz
b_alphabet = string.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ
s_pl_letters  = 'ąćęłńóśźż'
b_pl_letters  = s_pl_letters.upper() #'ĄĆĘŁŃÓŚŹŻ'
digits = string.digits #0123456789
punctuation = string.punctuation #!"#$%&\'()*+,-./:<=>?@[\\]^_`{|}~
punctuation = punctuation.replace(';','')
 
lists = [s_alphabet, b_alphabet, s_pl_letters, b_pl_letters, digits, punctuation]
cases = []

# to generate cases (combination number or n choose k or binomial coefficient or simply combinations):
# (n/k) = n!/k!(n-k)!, len(lists) = 6 
# (6/1) + (6/2) + (6/3) + (6/4) + (6/5) +(6/6) = 6 + 15 + 20 + 15 + 6 + 1 = 63 cases
for x in range(1,len(lists)+1):
    cases.extend(list(combinations(lists,x)))

# sample = []
# for case in cases:
#     sample.append(''.join(z for z in case))

test_values = []
results = []

def generate_values(i):
        
   # all casses with one word 
    for case in cases:
        for x in range(i):
            test = ''.join(random.choice(''.join(z for z in case)) for _ in range(random.randint(1,20)))
            result = test.upper()
            test_values.append(test)
            results.append(result)
     
    # all cases with using few words
    for case in cases:
        for x in range(i):
            words = random.randint(2,10)
            test = ''
            for x in range(words):
                test = test + ''.join(random.choice(''.join(z for z in case)) for _ in range(random.randint(1,20)))+ ' '  
            result = test.upper()    
            test_values.append(test)
            results.append(result)
        
        
i =input("How many test values You want generate for one case? ")
generate_values(int(i))

# print(test_values)
# print(results)

# print(len(test_values))
# print(len(results))

# writing test_values and results to files:
with open('zadania/zad2_tests.txt', 'w', encoding='utf-8') as plik:
    for t in test_values:
        plik.write(t + "\n")
        
with open('zadania/zad2_results.txt', 'w', encoding='utf-8') as plik:
    for res in results:
        plik.writelines(res + "\n")       