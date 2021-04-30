
import java.text.DecimalFormat;
import java.util.Scanner;

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
        System.out.println("Podaj dwie liczby (pierwsza to podstawa, a druga to wykładnik potęgi):");
        Scanner readInput = new Scanner(System.in);
        int a = readInput.nextInt();
        int b = readInput.nextInt();
        readInput.close();
        int wynik = potegowanie(a,b);
        DecimalFormat df = new DecimalFormat("#.####");
        System.out.println("Wynik potęgowania: "+df.format(wynik));
    }
}
