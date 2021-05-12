import java.util.Locale;
import java.util.Scanner;

public class zad1e {

    //ten program bedzie zwracał złe wyniki gdyż w wyniku bedzie zwracał przecinki zamiast kropek
    static double potegowanie(double a, double b)
    {
        double wynik = Math.pow(a,b);
        return wynik;
    }

    public static void main(String[] args) {
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi): ");
        Scanner readInput = new Scanner(System.in).useLocale(Locale.US);
        double a = readInput.nextDouble();
        double b = readInput.nextDouble();
        double wynik = potegowanie(a,b);
        System.out.format("Wynik potęgowania: %.4f",wynik);
    }
}
