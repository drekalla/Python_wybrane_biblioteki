
import java.text.DecimalFormat;
import java.util.Scanner;

public class zad1a {

    static double potegowanie(double a, double b){
        return Math.pow(a,b);
    }

    public static void main(String[] args) {
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi):");
        Scanner readInput = new Scanner(System.in);
        double a = readInput.nextDouble();
        double b = readInput.nextDouble();
        double wynik = potegowanie(a,b);
        DecimalFormat df = new DecimalFormat("#.####");
        System.out.println("Wynik potęgowania: "+df.format(wynik));
    }
}
