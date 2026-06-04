public class OperatorsDemo {
    public static void main(String[] args) {
        
        // --- 1. Arithmetic Operators (+, -, *, /) ---
        int x = 10;
        int y = 5;
        System.out.println("Sum: " + (x + y));        // 15
        System.out.println("Difference: " + (x - y)); // 5
        System.out.println("Product: " + (x * y));    // 50
        System.out.println("Division: " + (x / y));   // 2

        // --- 2. Comparison Operators (==, !=, >, <, >=, <=) ---
        // These always return a boolean (true/false)
        System.out.println("Is Equal? " + (x == y));      // false
        System.out.println("Is Not Equal? " + (x != y));  // true
        System.out.println("Greater than? " + (x > y));   // true
        System.out.println("Less than or equal? " + (x <= y)); // false

        // --- 3. Logical Operators (&&, ||, !) ---
        // Used to combine multiple conditions
        boolean isValid = true;
        boolean isMember = false;
        
        // AND (&&): Both must be true
        System.out.println("AND Result: " + (isValid && isMember)); // false
        // OR (||): At least one must be true
        System.out.println("OR Result: " + (isValid || isMember));  // true
        // NOT (!): Reverses the value
        System.out.println("NOT Result: " + (!isValid));           // false

        // --- 4. Assignment Operators (=, +=, -=) ---
        int score = 100; // Standard assignment
        score += 10;     // Same as: score = score + 10 (Result: 110)
        score -= 5;      // Same as: score = score - 5  (Result: 105)
        System.out.println("Final Score: " + score);
    }
}
