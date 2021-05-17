import java.util.Scanner;

public class zad2b {
    static String zamiana(String str){
        String zamieniony = "";
        for (int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            c = Character.toUpperCase(c);
            zamieniony = zamieniony + c;
        }
        return zamieniony;
    }

    public static void main(String[] args) {
        System.out.println("Wpisz tekst ktory zostanie zamineiony na wielkie litery: ");
        Scanner readInput = new Scanner(System.in);
        String str = readInput.nextLine();
        String zamieniony = zamiana(str);
        System.out.println("Zamieniony tekst: " + zamieniony);
    }
}
