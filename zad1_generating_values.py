"""
Created on Wed May  5 17:59:38 2021
@author: Olek
"""
import math
import random

test_values = []
results = []

########### LEGENDA ############

# dc -> dodatnie całkowite
# uc -> ujemne całkowite
# 0 -> zero
# ur -> ujemne rzeczywsite
# dr -> dodatnie rzeczywiste

############ info ############

# ->
# 2 przypadki zostały zakomentowane
# gdyż nie mają rozwiązań należących
# do zbioru liczb rzeczywsitych

# ->
# niektóre przypadki zostały
# zabezpieczone blokami try/except
# bo niektóre wyniki które były
# zwracane, nie należały do zbioru
# liczb rzeczywsitych

##############################

def generate_values(i):
    
    #case1 (dc ^ dc)
    for x in range(i):
        base = random.randint(1,10)
        exponent = random.randint(1,10)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))       
     
    #case2 (dc ^ uc)
    for x in range(i):
        base = random.randint(1,10)
        exponent = random.randint(-10,-1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
        
    #case3 (dc ^ 0)
    for x in range(i):
        base = random.randint(1,10)
        exponent = 0
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
     
    #case4 (dc ^ dr)
    for x in range(i):
        base = random.randint(1,10)
        exponent = round(random.uniform(0.1, 9.9),1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
        
    #case5 (dc ^ ur) 
    for x in range(i):
        base = random.randint(1,10)
        exponent = round(random.uniform(-9.9, -0.1),1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))   
        
    #case6 (uc ^ dc)
    for x in range(i):
        base = random.randint(-10,-1)
        exponent = random.randint(1,10)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))       
     
    #case7 (uc ^ uc)
    for x in range(i):
        base = random.randint(-10,-1)
        exponent = random.randint(-10,-1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(str(round(result,4)).replace(",","."))
        
    #case8 (uc ^ 0)
    for x in range(i):
        base = random.randint(-10,-1)
        exponent = 0
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
        
    #case9 (uc ^ dr)
    for x in range(i):
        result = 0
        while result == 0:
            try:
                base = random.randint(-10,-1)
                exponent = round(random.uniform(0.1, 9.9),1)
                result = math.pow(base, exponent)
                test_values.append("{};{}".format(base,exponent))
                results.append(round(result,4))
            except:
                pass
            else:
                result = 1
        
    #case10 (uc ^ ur) 
    for x in range(i):
        result = 0
        while result == 0:
            try:
                base = random.randint(-10,-1)
                exponent = round(random.uniform(-9.9, -0.1),1)
                result = math.pow(base, exponent)
                test_values.append("{};{}".format(base,exponent))
                results.append(round(result,4))
            except:
                pass
            else:
                result = 1
        
    #case11 (0 ^ dc)
    for x in range(i):
        base = 0
        exponent = random.randint(1,10)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))        
     
    # #case12 (0 ^ uc)
    # for x in range(10):
    #     base = 0
    #     exponent = random.randint(-10,-1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(str(round(result,4)).replace(",","."))
        
    #case13 (0 ^ 0)
    for x in range(1):
        base = 0
        exponent = 0
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
     
    #case14 (0 ^ dr)
    for x in range(i):
        base = 0
        exponent = round(random.uniform(0.1, 9.9),1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))         
        
    # #case15 (0 ^ ur) 
    # for x in range(10):
    #     base = 0
    #     exponent = round(random.uniform(-9.9, -0.1),1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(str(round(result,4)).replace(",","."))
        
    #case16 (dr ^ dc)
    for x in range(i):
        base = round(random.uniform(0.1, 9.9),1)
        exponent = random.randint(1,10)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
        
     
    #case17 (dr ^ uc)
    for x in range(i):
        base = round(random.uniform(0.1, 9.9),1)
        exponent = random.randint(-10,-1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
        
    #case18 (dr ^ 0)
    for x in range(i):
        base = round(random.uniform(0.1, 9.9),1)
        exponent = 0
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
     
    #case19 (dr ^ dr)
    for x in range(i):
        base = round(random.uniform(0.1, 9.9),1)
        exponent = round(random.uniform(0.1, 9.9),1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))         
        
    #case20 (dr ^ ur) 
    for x in range(i):
        base = round(random.uniform(0.1, 9.9),1)
        exponent = round(random.uniform(-9.9, -0.1),1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
        
    #case21 (ur ^ dc)
    for x in range(i):
        base = round(random.uniform(-9.9, -0.1),1)
        exponent = random.randint(1,10)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
        
     
    #case22 (ur ^ uc)
    for x in range(i):
        base = round(random.uniform(-9.9, -0.1),1)
        exponent = random.randint(-10,-1)
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
        
    #case23 (ur ^ 0)
    for x in range(i):
        base = round(random.uniform(-9.9, -0.1),1)
        exponent = 0
        result = math.pow(base, exponent)
        test_values.append("{};{}".format(base,exponent))
        results.append(round(result,4))
     
    #case24 (ur ^ dr)
    for x in range(i):
        result == 0
        while result==0:
            try:
                base = round(random.uniform(-9.9, -0.1),1)
                exponent = round(random.uniform(0.1, 9.9),1)
                result = math.pow(base, exponent)
                test_values.append("{};{}".format(base,exponent))
                results.append(round(result,4))
            except :
                pass
            else:
                result = 1
        
    #case25 (ur ^ ur) 
    for x in range(i):
        result = 0
        while result == 0:
            try:
                base = round(random.uniform(-9.9, -0.1),1)
                exponent = round(random.uniform(-9.9, -0.1),1)
                result = math.pow(base, exponent)
                test_values.append("{};{}".format(base,exponent))
                results.append(round(result,4))
            except:
                pass
            else:
                result = 1

i =input("How many test values You want generate for one case? ")
generate_values(int(i))
    
print(test_values)
print(results)


# zapis wygenerowanych wartoci do plików (jeli plików nie to zostaną stworzone)
with open('zad1_tests.txt', 'w') as plik:
    for t in test_values:
        plik.write(str(t) + "\n")
        
with open('zad1_results.txt', 'w') as plik:
    for res in results:
        plik.writelines(str(res) + "\n")
