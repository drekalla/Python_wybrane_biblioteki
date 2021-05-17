import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.Scanner;

// to zadanie nie wykona się poprawnie jeśli podana zostanie lczba po przecinku lub obydwie liczby będą ujemne
public class zad1b {
    //https://www.geeksforgeeks.org/calculating-the-power-of-a-number-in-java-without-using-math-pow-method/
    public static int potegowanie(int x, int y)
    {
        int temp;
        if (y == 0)
            return 1;
        temp = potegowanie(x, y / 2);

        if (y % 2 == 0)
            return temp * temp;
        else {
            if (y > 0)
                return x * temp * temp;
            else
                return (temp * temp) / x;
        }
    }

    public static void main(String[] args) {
        DecimalFormatSymbols nf = new DecimalFormatSymbols(Locale.US);
        DecimalFormat df = new DecimalFormat("0.0###", nf);
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi):");
        Scanner readInput = new Scanner(System.in).useLocale(Locale.US);
        int a = readInput.nextInt();
        int b = readInput.nextInt();
        readInput.close();
        int wynik = potegowanie(a,b);
        System.out.println("Wynik potęgowania: "+df.format(wynik));
    }
}
