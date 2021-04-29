package com.company;

import java.text.DecimalFormat;
import java.util.Scanner;

public class zad1c {

    static double potegowanie(double a, double b)
    // https://stackoverflow.com/questions/35783215/exponents-without-math-pow-using-for-loop-in-java
    {
        double result = 1;

        if (b < 0) {
            a = 1.0 / a;
            b = -b;
        }

        for (int  i = 0; i < b; i++) {
            result = result * a;
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi):");
        Scanner readInput = new Scanner(System.in);
        double a = readInput.nextDouble();
        double b = readInput.nextDouble();
        readInput.close();
        double wynik = potegowanie(a,b);
        DecimalFormat df = new DecimalFormat("#.####");
        System.out.println("Wynik potęgowania: "+df.format(wynik));
    }
}

