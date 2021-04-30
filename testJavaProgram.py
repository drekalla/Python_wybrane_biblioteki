import os
from subprocess import PIPE, Popen, call, check_call, TimeoutExpired
from datetime import datetime


def testJavaProgram(jdkPath,resultFilePath, testFilePath, filePath, fileName):

    # os.chdir("C:\\jdk-16.0.1\\")
    # os.chdir(".\\bin\\")
    # przejście do ścieżki, gdzie znajduje się kompilator
    os.chdir(jdkPath)
    # sprawdzenie czy ścieżka została poprawnie wskazana
    if call(['java', '--version']) != 0:
        return 'Ścieżka do JDK została błędnie wskazana. \nSprawdź, czy wskazany został folder "bin"',0
    # sprawdzam, czy program się kompiluje
    if call(['javac', filePath + "\\" + fileName]) == 0:
        # otwieram pliki z danymi testowymi i wynikami dla danych testow - jeśli plik nie istnieje zwracam błąd do gui
        # każdy test powinien znajdować się w nowej linii w pliku tekstowym, a dane w poszczególnych testach
        # powinny być oddzielone średnikiem
        # każdy wynik powinien znajdować się w nowej linii w pliku tekstowym z wynikami
        # Plik z testami powinien się nazywać: NAZWAPROGRAMUtest.txt
        # Plik z wynikami powinien się nazywać: NAZWAPROGRAMUresult.txt
        try:
            #testLines = open(filePath + "\\" + fileName.split('.')[0] + 'test.txt').read().splitlines()
            testLines = open(testFilePath, encoding='utf8').read().splitlines()
        except IOError:
            return 'Brak pliku z danymi testowymi', 0
        try:
            #resultLines = open(filePath + "\\" + fileName.split('.')[0] + 'result.txt').read().splitlines()
            resultLines = open(resultFilePath, encoding='utf8').read().splitlines()
        except IOError:
            return 'Brak pliku z wynikami dla danych testowych', 0
        # przed uruchomieniem programu przypisuje do zmiennej startTime czas rozpoczęcia uruchomienia
        startTime = datetime.now().time()
        # zmienne do sprawdzania ilość wykonanych testów oraz ich poprawności
        i = 0
        countOfCorrectTests = 0
        countOfTotalTests = 0
        for line in testLines:
            inputString = ''
            variables = line.split(';')
            for var in variables:
                if var != '':
                    inputString += var + '\n'
            # p = Popen(["C:\\jdk-16.0.1\\bin\\java", "-cp", filePath, fileName.split(".")[0]],
            #           stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            p = Popen(["java", "-cp", filePath, fileName.split(".")[0]],
                      stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            try:
                out, err = p.communicate(input=inputString, timeout=1)
            except TimeoutExpired as e:
                print("Wystąpiło przerwanie z powodu zbyt długiego czasu wykonania")
                i += 1
                countOfTotalTests += 1
                p.kill()
                continue
            if p.returncode == 0:
                # print('{result}'.format(result=out.strip().rpartition(' ')[2]))
                # sprawdzam, czy wynik, który wygenerował program zgadza się z wynikiem z pliku tekstowego
                result = '{result}'.format(result=out.strip().rpartition(':')[2].strip())
                try:
                    if result == resultLines[i]:
                        countOfCorrectTests += 1
                        #print("%d - dane testowe: %s, wyjście z programu: %s, prawidłowy wynik: %s"%(i, variables, result, resultLines[i]))
                        #print("poprawne")
                    else:
                        pass
                        #print("%d - dane testowe: %s, wyjście z programu: %s, prawidłowy wynik: %s"%(i, variables, result, resultLines[i]))
                except:
                    return 'Wystąpił nieoczekiwany błąd', 0
            else:  # error
                print('Error: exit code: {}, stderr: {}'.format(p.returncode, err))
            i += 1
            countOfTotalTests += 1
            p.kill()
        # obliczanie czasu wykonania wszystkich testów
        endTime = datetime.now().time()
        date = datetime.now().date()
        datetime1 = datetime.combine(date, startTime)
        datetime2 = datetime.combine(date, endTime)
        time = datetime2 - datetime1
        return 'Poprawnie {} z {}'.format(countOfCorrectTests, countOfTotalTests), time
    else:
        return 'Błąd kompilacji', 0