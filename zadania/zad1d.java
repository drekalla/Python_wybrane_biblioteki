
import java.text.DecimalFormat;
import java.util.Scanner;

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
