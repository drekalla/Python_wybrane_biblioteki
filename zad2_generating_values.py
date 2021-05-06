# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:19:34 2021

@author: Olek
"""
import string
import random

s_alphabet = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz
b_alphabet = string.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ
s_pl_letters  = 'ąćęłńóśźż'
b_pl_letters  = s_pl_letters.upper() #'ĄĆĘŁŃÓŚŹŻ'
digits = string.digits #0123456789
punctuation = string.punctuation #!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~

test_values = []
results = []

def generate_values(i):
    
    # (k/n) = (6/1) = 6 cases    
    
    #case1 (one word with only small letters)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
        
    #case2 (one word with only big letters)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
        
    #case3 (one word with only samll polish letters)
    for x in range(i):
        test = ''.join(random.choice(s_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case4 (one word with only big polish letters)
    for x in range(i):
        test = ''.join(random.choice(b_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
        
    #case5 (one word with only digits)
    for x in range(i):
        test = ''.join(random.choice(digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
        
    #case6 (one word with only punctuation)
    for x in range(i):
        test = ''.join(random.choice(punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    # (k/n) = (6/2) = 15 cases
    
    #case7 (one word with small and big letters without polish digits)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case8 (one word with small letters and small letters with polish digits)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+s_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
        
    #case9 (one word with small letters and big letters with polish digits)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
        
    #case10 (one word with small letters and digits)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
        
    #case11 (one word with small letters and punctuation)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case12 (one word with big letters and small letters with polish digits)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+s_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case13 (one word with big letters and big letters with polish digits)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+b_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case14 (one word with big letters and digits)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case15 (one word with big letters and digits)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case16 (one word with small letters with polish diacritical marks 
    #        and big letters with diacritical marks)
    for x in range(i):
        test = ''.join(random.choice(s_pl_letters+b_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    #case17 (one word with small letters with polish diacritical marks 
    #        and digits)
    for x in range(i):
        test = ''.join(random.choice(s_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)   
    
    #case18 (one word with small letters with polish diacritical marks 
    #        and punctuation)
    for x in range(i):
        test = ''.join(random.choice(s_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    
    #case19 (one word with big letters with polish diacritical marks 
    #        and digits)
    for x in range(i):
        test = ''.join(random.choice(b_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case20 (one word with big letters with polish diacritical marks 
    #        and punctuation)
    for x in range(i):
        test = ''.join(random.choice(b_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
        
    #case21 (one word with digits and punctuation)
    for x in range(i):
        test = ''.join(random.choice(digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    # (k/n) = (6/3) = 20 cases   
        
    #case22 (s+b + s_pl)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case23 (s+b + b_pl)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+b_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    #case24 (s+b + d)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    #case25 (s+b + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case26 (s+s_pl + b_pl)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+s_pl_letters+b_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case27 (s+s_pl + d)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+s_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    
    #case28 (s+s_pl + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+s_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case29 (s+b_pl + d)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case30 (s+b_pl + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    
    #case31 (s+d + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case32 (b+s_pl + b_pl)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+s_pl_letters+b_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    #case33 (b+s_pl + d)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+s_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    #case34 (b+s_pl + p)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+s_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case35 (b+b_pl + d)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+b_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case36 (b+b_pl + p)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+b_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case37 (b+d + p)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case38 (s_pl+b_pl + d)
    for x in range(i):
        test = ''.join(random.choice(s_pl_letters+b_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case39 (s_pl+ b_pl+ p)
    for x in range(i):
        test = ''.join(random.choice(s_pl_letters+b_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case40 (s_pl + d + p)
    for x in range(i):
        test = ''.join(random.choice(s_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case41 (b_pl+d + p)
    for x in range(i):
        test = ''.join(random.choice(b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    # (k/n) = (6/4) = 15 cases
    
    #case42 (s+b+s_pl+b_pl)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters+b_pl_letters) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case43 (s+b+s_pl+d)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case44 (s+b+s_pl+p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case45 (s+b+b_pl+d)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+b_pl_letters + digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case46 (s+b+b_pl+p) 5
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+b_pl_letters + punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    
    #case47 (s+b+d+p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+digits + punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
    
    #case48 (s+s_pl+b_pl + d)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+s_pl_letters+b_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case49 (s+ s_pl+ b_pl+ p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+s_pl_letters+b_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    #case50 (s+ s_pl + d + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+s_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case51(s+ b_pl + d + p) 10
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case52 (b+s_pl+b_pl+d)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+s_pl_letters+b_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case53 (b+s_pl+b_pl+p)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+s_pl_letters+b_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case54 (b+s_pl+d+p)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+s_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case55 (b+b_pl+d+p)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    #case56 (s_pl+ b_pl + d + p)
    for x in range(i):
        test = ''.join(random.choice(s_pl_letters+b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    # (k/n) = (6/5) = 6 cases
    
    #case57 (s+ b + s_pl + b_pl + d) 10
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters+b_pl_letters+digits) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case58 (s+ b + s_pl + b_pl + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters+b_pl_letters+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case59 (s+ b + s_pl + d + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
        
    #case60 (s+ b + b_pl + d + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case61 (s+ s_pl + b_pl + d + p)
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+s_pl_letters+b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    #case62 (b + s_pl + b_pl + d + p)
    for x in range(i):
        test = ''.join(random.choice(b_alphabet+s_pl_letters+b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result) 
    
    # (k/n) = (6/6) = 1 case
    
    #case63 (s+ b + s_pl + b_pl + d) 10
    for x in range(i):
        test = ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters+b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))
        result = test.upper()
        test_values.append(test)
        results.append(result)
     
    #case64 few words with all combinations
    for x in range(i*7):
        words = random.randint(1,10)
        test = ''
        for x in range(words):
            test = test + ''.join(random.choice(s_alphabet+b_alphabet+s_pl_letters+b_pl_letters+digits+punctuation) for _ in range(random.randint(1,20)))+ ' '  
        result = test.upper()    
        test_values.append(test)
        results.append(result)
        
        
i =input("How many test values You want generate for one case? ")
generate_values(int(i))

# print(test_values)
# print(results)

# print(len(test_values))
# print(len(results))

# writing test_values and results to files
with open('zad2_tests.txt', 'w') as plik:
    for t in test_values:
        plik.write(t + "\n")
        
with open('zad2_results.txt', 'w') as plik:
    for res in results:
        plik.writelines(res + "\n")
        