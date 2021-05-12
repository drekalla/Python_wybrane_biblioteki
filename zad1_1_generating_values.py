import math
import random
import numpy as np

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
# przypadki zostały
# zabezpieczone blokami try/except
# bo niektóre wyniki które były
# zwracane, nie należały do zbioru
# liczb rzeczywsitych

##############################

cases = {'dc':[x for x in range(1,11)],
         'uc':[x for x in range(-10,0)],
         '0': [0],
         'dr': list(np.round(x,1) for x in np.arange(0.1,10.1,0.1)),
         'ur': list(np.round(x,1) for x in np.arange(-10,0,0.1))}


def generate_values(i):
    
    for key_case in cases:
        for k_c in cases:
            if ((key_case == '0' and k_c == 'uc') or (key_case == '0' and k_c == 'ur')):
                pass
            else:            
                for x in range(i):
                    result = 0
                    while result == 0:
                        try:           
                            base = random.choice(cases[key_case])
                            exponent = random.choice(cases[k_c])
                            pow_result = round(math.pow(base, exponent),4)
                            test_values.append("{};{}".format(base,exponent))
                            if (str(pow_result) == '-0.0'):
                                pow_result = 0.0
                            results.append(pow_result)
                        except:
                            pass
                        else:
                            result = 1
                    if key_case == '0' and k_c == '0': break
                
    
    
    # #case1 (dc ^ dc)
    # for x in range(i):
    #     base = random.randint(1,10)
    #     exponent = random.randint(1,10)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))       
     
    # #case2 (dc ^ uc)
    # for x in range(i):
    #     base = random.randint(1,10)
    #     exponent = random.randint(-10,-1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
        
    # #case3 (dc ^ 0)
    # for x in range(i):
    #     base = random.randint(1,10)
    #     exponent = 0
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
     
    # #case4 (dc ^ dr)
    # for x in range(i):
    #     base = random.randint(1,10)
    #     exponent = round(random.uniform(0.1, 9.9),1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
        
    # #case5 (dc ^ ur) 
    # for x in range(i):
    #     base = random.randint(1,10)
    #     exponent = round(random.uniform(-9.9, -0.1),1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))   
        
    # #case6 (uc ^ dc)
    # for x in range(i):
    #     base = random.randint(-10,-1)
    #     exponent = random.randint(1,10)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))       
     
    # #case7 (uc ^ uc)
    # for x in range(i):
    #     base = random.randint(-10,-1)
    #     exponent = random.randint(-10,-1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(str(round(result,4)).replace(".",","))
        
    # #case8 (uc ^ 0)
    # for x in range(i):
    #     base = random.randint(-10,-1)
    #     exponent = 0
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
        
    # #case9 (uc ^ dr)
    # for x in range(i):
    #     result = 0
    #     while result == 0:
    #         try:
    #             base = random.randint(-10,-1)
    #             exponent = round(random.uniform(0.1, 9.9),1)
    #             result = math.pow(base, exponent)
    #             test_values.append("{};{}".format(base,exponent))
    #             results.append(round(result,4))
    #         except:
    #             pass
    #         else:
    #             result = 1
        
    # #case10 (uc ^ ur) 
    # for x in range(i):
    #     result = 0
    #     while result == 0:
    #         try:
    #             base = random.randint(-10,-1)
    #             exponent = round(random.uniform(-9.9, -0.1),1)
    #             result = math.pow(base, exponent)
    #             test_values.append("{};{}".format(base,exponent))
    #             results.append(round(result,4))
    #         except:
    #             pass
    #         else:
    #             result = 1
        
    # #case11 (0 ^ dc)
    # for x in range(i):
    #     base = 0
    #     exponent = random.randint(1,10)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))        
     
    # # #case12 (0 ^ uc)
    # # for x in range(10):
    # #     base = 0
    # #     exponent = random.randint(-10,-1)
    # #     result = math.pow(base, exponent)
    # #     test_values.append("{};{}".format(base,exponent))
    # #     results.append(str(round(result,4)).replace(".",","))
        
    # #case13 (0 ^ 0)
    # for x in range(1):
    #     base = 0
    #     exponent = 0
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
     
    # #case14 (0 ^ dr)
    # for x in range(i):
    #     base = 0
    #     exponent = round(random.uniform(0.1, 9.9),1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))         
        
    # # #case15 (0 ^ ur) 
    # # for x in range(10):
    # #     base = 0
    # #     exponent = round(random.uniform(-9.9, -0.1),1)
    # #     result = math.pow(base, exponent)
    # #     test_values.append("{};{}".format(base,exponent))
    # #     results.append(str(round(result,4)).replace(".",","))
        
    # #case16 (dr ^ dc)
    # for x in range(i):
    #     base = round(random.uniform(0.1, 9.9),1)
    #     exponent = random.randint(1,10)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
        
     
    # #case17 (dr ^ uc)
    # for x in range(i):
    #     base = round(random.uniform(0.1, 9.9),1)
    #     exponent = random.randint(-10,-1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
        
    # #case18 (dr ^ 0)
    # for x in range(i):
    #     base = round(random.uniform(0.1, 9.9),1)
    #     exponent = 0
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
     
    # #case19 (dr ^ dr)
    # for x in range(i):
    #     base = round(random.uniform(0.1, 9.9),1)
    #     exponent = round(random.uniform(0.1, 9.9),1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))         
        
    # #case20 (dr ^ ur) 
    # for x in range(i):
    #     base = round(random.uniform(0.1, 9.9),1)
    #     exponent = round(random.uniform(-9.9, -0.1),1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
        
    # #case21 (ur ^ dc)
    # for x in range(i):
    #     base = round(random.uniform(-9.9, -0.1),1)
    #     exponent = random.randint(1,10)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
        
     
    # #case22 (ur ^ uc)
    # for x in range(i):
    #     base = round(random.uniform(-9.9, -0.1),1)
    #     exponent = random.randint(-10,-1)
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
        
    # #case23 (ur ^ 0)
    # for x in range(i):
    #     base = round(random.uniform(-9.9, -0.1),1)
    #     exponent = 0
    #     result = math.pow(base, exponent)
    #     test_values.append("{};{}".format(base,exponent))
    #     results.append(round(result,4))
     
    # #case24 (ur ^ dr)
    # for x in range(i):
    #     result == 0
    #     while result==0:
    #         try:
    #             base = round(random.uniform(-9.9, -0.1),1)
    #             exponent = round(random.uniform(0.1, 9.9),1)
    #             result = math.pow(base, exponent)
    #             test_values.append("{};{}".format(base,exponent))
    #             results.append(round(result,4))
    #         except :
    #             pass
    #         else:
    #             result = 1
        
    # #case25 (ur ^ ur) 
    # for x in range(i):
    #     result = 0
    #     while result == 0:
    #         try:
    #             base = round(random.uniform(-9.9, -0.1),1)
    #             exponent = round(random.uniform(-9.9, -0.1),1)
    #             result = math.pow(base, exponent)
    #             test_values.append("{};{}".format(base,exponent))
    #             results.append(round(result,4))
    #         except:
    #             pass
    #         else:
    #             result = 1

i =input("How many test values You want generate for one case? ")
generate_values(int(i))
    
print(test_values)
print(results)


# zapis wygenerowanych wartoci do plików (jeli plików nie to zostaną stworzone)
with open('zadania/zad1_tests.txt', 'w') as plik:
    for t in test_values:
        plik.write(str(t) + "\n")
        
with open('zadania/zad1_results.txt', 'w') as plik:
    for res in results:
        plik.writelines(str(res) + "\n")
