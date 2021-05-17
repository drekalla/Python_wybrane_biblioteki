import java.util.Scanner;

public class zad2d {
    static String zamiana(String str){
        String zamieniony = "";
        char[] alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXZ1234567890".toCharArray();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            boolean ifExists = false;
            for (char x : alphabet) {
                if (x == c)
                {
                    ifExists = true;
                    break;
                }
            }
            if (!ifExists)
            {
                c = Character.toUpperCase(c);
                zamieniony = zamieniony + c;
            }
        }
        return zamieniony;
    }

    public static void main(String[] args) {
        System.out.println("Podaj tekst a ja zamienie go na wielkie litery: ");
        Scanner readInput = new Scanner(System.in);
        String str = readInput.nextLine();
        String zamieniony = zamiana(str);
        System.out.println("A nie mówiłem?: " + zamieniony);
    }
}
