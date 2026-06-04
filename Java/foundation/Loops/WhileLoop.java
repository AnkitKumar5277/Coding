public class WhileLoopExample {
    public static void main(String[] args) {
        
        boolean isDisplayed = true;
        int attempts = 0;

        // Jab tak isDisplayed true hai, loop chalega
        while (isDisplayed) {
            System.out.println("Checking element... Attempt: " + (attempts + 1));
            
            attempts++;

            // Break ka use: loop ko beech mein hi rokne ke liye
            if (attempts == 3) {
                System.out.println("Element found! Breaking loop.");
                break; 
            }
        }
        
        System.out.println("Loop ke bahar aa gaye.");
    }
}
