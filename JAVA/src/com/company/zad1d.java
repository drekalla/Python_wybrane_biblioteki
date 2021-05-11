package com.company;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.Scanner;

// te zadanie myli się gdy wykładnik jest liczbą po przecinku
public class zad1d {

    static double potegowanie(double a, double b) {
        // https://www.codegrepper.com/code-examples/java/how+to+find+power+of+a+number+in+java+without+math.pow
        double result = 1;
        while (b != 0)
        {
            result *= a;
            --b;
        }
        return result;
    }

    public static void main(String[] args) {
        DecimalFormatSymbols nf = new DecimalFormatSymbols(Locale.US);
        DecimalFormat df = new DecimalFormat("0.0###", nf);
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi):");
        Scanner readInput = new Scanner(System.in).useLocale(Locale.US);
        double a = readInput.nextDouble();
        double b = readInput.nextDouble();
        readInput.close();
        double wynik = potegowanie(a,b);
        System.out.println("Wynik potęgowania: "+df.format(wynik));
    }
}
