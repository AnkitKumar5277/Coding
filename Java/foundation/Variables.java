public class VariableDemo {
    
    // 1. Static Variable: Declared inside the class but outside any method.
    // It can be accessed directly by all methods in the class.
    static int total = 10; 

    public static void main(String[] args) {
        
        // 2. Local Variable: Declared inside a method.
        // It can only be used within this specific main method.
        int count = 5; 

        // Accessing both variables
        System.out.println("Local count: " + count);
        System.out.println("Static total: " + total);
        
        // You can perform math using both
        int sum = count + total;
        System.out.println("The sum is: " + sum);
    }
}
