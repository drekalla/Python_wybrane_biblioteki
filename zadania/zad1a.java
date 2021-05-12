import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.Scanner;

// to zadanie powinnp być wykonane poprawnie dla każdego przypadku liczb z zakresu liczb double
public class zad1a {

    static double potegowanie(double a, double b){
        return Math.pow(a,b);
    }

    public static void main(String[] args) {
        DecimalFormatSymbols nf = new DecimalFormatSymbols(Locale.US);
        DecimalFormat df = new DecimalFormat("0.0###", nf);
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi):");
        Scanner readInput = new Scanner(System.in).useLocale(Locale.US);
        double a = readInput.nextDouble();
        double b = readInput.nextDouble();
        double wynik = potegowanie(a,b);
        System.out.println("Wynik potęgowania: "+df.format(wynik));
    }
}
