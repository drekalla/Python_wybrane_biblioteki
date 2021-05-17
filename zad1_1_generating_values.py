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
                            results.append(pow_result)
                        except:
                            pass
                        else:
                            result = 1
                    if key_case == '0' and k_c == '0': break
                

i =input("How many test values You want generate for one case? ")
generate_values(int(i))
    
# print(test_values)
# print(results)


# zapis wygenerowanych wartoci do plików (jeli plików nie to zostaną stworzone)
with open('zad1_tests.txt', 'w') as plik:
    for t in test_values:
        plik.write(str(t) + "\n")
        
with open('zad1_results.txt', 'w') as plik:
    for res in results:
        plik.writelines(str(res) + "\n")
