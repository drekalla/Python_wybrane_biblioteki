import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.Scanner;

// to zadanie wykona się błędnie gdy wykładnik jest liczbą po przecinku
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
        DecimalFormatSymbols nf = new DecimalFormatSymbols(Locale.US);
        DecimalFormat df = new DecimalFormat("0.0###", nf);
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi):");
        Scanner readInput = new Scanner(System.in).useLocale(Locale.US);
        double a = readInput.nextDouble();s
        double b = readInput.nextDouble();
        readInput.close();
        double wynik = potegowanie(a,b);
        System.out.println("Wynik potęgowania: "+df.format(wynik));
    }
}

