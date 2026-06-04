public class Main {
    public static void main(String[] args) {
        
        // 1. Declaration and Initialization
        String[] browsers = {"Chrome", "Firefox", "Edge"};

        // 2. Accessing Elements (Indexing starts at 0)
        System.out.println("First browser: " + browsers[0]); // Chrome
        System.out.println("Second browser: " + browsers[1]); // Firefox

        // 3. Modifying an Element
        browsers[2] = "Brave"; 
        System.out.println("Updated third browser: " + browsers[2]);

        // 4. Getting Array Length
        System.out.println("Number of browsers: " + browsers.length);

        System.out.println("--- Full List ---");

        // 5. Iterating through the array using a for-each loop
        for (String b : browsers) {
            System.out.println(b);
        }
    }
}
