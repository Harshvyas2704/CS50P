import java.util.*;
public class check{

    public static void hello(String name){
        System.out.println("Hello, " + name);
    }
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("What is your name? ");
        String name = sc.next();

        hello(name);

        sc.close();

    }

}