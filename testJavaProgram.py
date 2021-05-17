import os
import re
import datetime
from subprocess import PIPE, Popen, call, TimeoutExpired
from tqdm import tqdm
import time

def testJavaProgram(jdkPath,resultFilePath, testFilePath, filePath, fileName):

    # przejście do ścieżki, gdzie znajduje się kompilator
    os.chdir(jdkPath)
    if len(fileName) == 0:
        return "Żadem z plików nie został wskazany", 0
    # sprawdzenie czy ścieżka została poprawnie wskazana
    if re.match('.*jdk.*bin$', jdkPath) is None or os.path.exists(jdkPath + '\\' + 'java.exe') is False:
        return 'Ścieżka do JDK została błędnie wskazana \nlub brakuje jednego ze składowych jdk. \nSprawdź, czy wskazany został folder "bin"',0
    # sprawdzam, czy program się kompiluje
    if call(['javac', filePath + "\\" + fileName]) == 0:
        # otwieram pliki z danymi testowymi i wynikami dla danych testow - jeśli plik nie istnieje zwracam błąd do gui
        # każdy test powinien znajdować się w nowej linii w pliku tekstowym, a dane w poszczególnych testach
        # powinny być oddzielone średnikiem
        # każdy wynik powinien znajdować się w nowej linii w pliku tekstowym z wynikami
        try:
            testLines = open(testFilePath, encoding='utf8').read().splitlines()
        except UnicodeDecodeError:
            return 'Błędne kodowanie pliku z testawmi. \nPlik powinien być zakodowany w "utf-8"', 0
        except IOError:
            return 'Brak pliku z danymi testowymi', 0

        try:
            resultLines = open(resultFilePath, encoding='utf8').read().splitlines()
        except UnicodeDecodeError:
            return 'Błędne kodowanie pliku z wynikami. \nPlik powinien być zakodowany w "utf-8"', 0
        except IOError:
            return 'Brak pliku z wynikami dla danych testowych', 0


        # uruchamiam jednorazowo program, żeby sprawdzić co program wypisuje przed wypisaniem wyniku
        # ta zmienna jest później wykorzystana do prawidłowego rozpoznania wyjścia z programu
        p = Popen(["java", "-cp", filePath, fileName.split(".")[0]],
                  stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        out, err = p.communicate()
        OutputOfJavaProgramBeforeResult = out
        p.kill()

        # zmienne do sprawdzania czasu wykonania, ilośi wykonanych testów oraz ich poprawności
        i = 0
        countOfCorrectTests = 0
        countOfTotalTests = 0
        passedCorrectTestsList = []
        passedIncorrectTestsList = []
        totalTimePassed = 0.0
        for line in tqdm(testLines):
            isTimeoutExpired = False
            inputString = ''
            variables = line.split(';')
            for var in variables:
                if var != '':
                    if len(inputString) == 0:
                        inputString += var
                    else:
                        inputString += ' ' + var

            startTime = time.time()
            # właście uruchomienie programu w javie
            p = Popen(["java", "-cp", filePath, fileName.split(".")[0]],
                      stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            # w funkcji communicate przekazuje poprzez inputString dane testowe z pliku
            try:
                out, err = p.communicate(input=inputString, timeout=1)
                out = out.replace(OutputOfJavaProgramBeforeResult, '')
            # jeśli program nie odpowiada dłużej niż sekudnę wyrzuca wyjątek TimeoutExpired,
            # który zmienną isTimeoutExpired na True, która jest później wykorzystana
            # do prawidłowego zwrócenia wyników
            except TimeoutExpired as e:
                isTimeoutExpired = True

            # obliczenie czasu wykonania pojedynczego uruchomienia programu w Javie i dodanie go zmiennej
            # zawierającej sumaryczny czas wykonania wszystkich testów
            timePassed = time.time() - startTime
            totalTimePassed += timePassed

            #p.returncode zwraca 0 jeśli program w Javie został zakończony z sukcesem
            if p.returncode == 0:
                # W przypadku, gdy wynik jest zmienną typu string sprawdzam, czy nie zawiera dwukropka,
                # aby zapobiec błędnemu odczytaniu wyjścia
                if out.lstrip().rpartition(':')[0].rstrip('\n').find(':'):
                    index = out.lstrip().rstrip('\n').find(':')
                    result = out[index+1:].lstrip().rstrip('\n')
                else:
                    result = '{result}'.format(result=out.strip().rpartition(':')[0].strip())
                try:
                    if result == resultLines[i]:
                        countOfCorrectTests += 1
                        passedCorrectTestsList.append("%d - dane testowe: %s, wyjście z programu: %s, prawidłowy wynik: %s"%(i, variables, result, resultLines[i]))
                    else:
                        passedIncorrectTestsList.append("%d - dane testowe: %s, wyjście z programu: %s, prawidłowy wynik: %s"%(i, variables, result, resultLines[i]))
                except:
                    return 'Wystąpił nieoczekiwany błąd', 0
            else:  # error
                if isTimeoutExpired:
                    passedIncorrectTestsList.append("%d - dane testowe: %s, Błąd: Wystąpiło przerwanie z powodu zbyt długiego czasu wykonania"%(i, variables))
                else:
                    passedIncorrectTestsList.append("%d - dane testowe: %s, Błąd: Error: exit code: %s, stderr: %s"%(i, variables,p.returncode, err))
            i += 1
            countOfTotalTests += 1
            p.kill()

        passedIncorrectOutputFile = open(filePath + '\\' + fileName + '_incorrect.txt','w',encoding='utf-8')
        passedCorrectOutputFile = open(filePath + '\\' + fileName + '_correct.txt','w',encoding='utf-8')
        passedCorrectTestsList = map(lambda x: x + '\n', passedCorrectTestsList)
        passedIncorrectTestsList = map(lambda x: x + '\n', passedIncorrectTestsList)

        passedCorrectOutputFile.writelines(passedCorrectTestsList)
        passedCorrectOutputFile.close()
        passedIncorrectOutputFile.writelines(passedIncorrectTestsList)
        passedCorrectOutputFile.close()

        return 'Poprawnie {} z {}'.format(countOfCorrectTests, countOfTotalTests), datetime.timedelta(seconds=totalTimePassed)
    else:
        return 'Błąd kompilacji', 0