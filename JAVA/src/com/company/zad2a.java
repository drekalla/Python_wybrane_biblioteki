package com.company;
import java.util.Locale;
import java.util.Scanner;

public class zad2a {
    static String zamiana(String str){
        return str.toUpperCase(Locale.ROOT);
    }

    public static void main(String[] args) {
        System.out.println("Podaj tekst który chcesz zamienić na wielkie litery: ");
        Scanner readInput = new Scanner(System.in);
        String str = readInput.nextLine();
        String zamieniony = zamiana(str);
        System.out.println("Zamieniony tekst: " + zamieniony);
    }
}
