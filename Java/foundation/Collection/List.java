import java.util.ArrayList; // 1. Import the ArrayList class

public class Main {
    public static void main(String[] args) {
        
        // 2. Create an ArrayList of Strings
        ArrayList<String> list = new ArrayList<>();

        // 3. Add elements to the list
        list.add("PASS");
        list.add("FAIL");
        list.add("PENDING"); // Adding one more to show growth

        // 4. Print the entire list
        System.out.println("Current List: " + list);

        // 5. Access a specific element (Index starts at 0)
        String firstItem = list.get(0);
        System.out.println("The first item is: " + firstItem);

        // 6. Get the size of the list
        System.out.println("List size: " + list.size());
    }
}
