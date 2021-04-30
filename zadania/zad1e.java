
import java.util.Scanner;

public class zad1e {

    static double potegowanie(double a, double b)
    {
        double wynik = Math.pow(a,b);
        return wynik;
    }

    public static void main(String[] args) {
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi): ");
        Scanner readInput = new Scanner(System.in);
        double a = readInput.nextDouble();
        double b = readInput.nextDouble();
        double wynik = potegowanie(a,b);
        System.out.println("Wynik potęgowania: "+wynik);
    }
}
