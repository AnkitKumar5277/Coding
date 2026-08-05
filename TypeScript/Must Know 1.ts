// variables
let age: number = 22;
let name: string = "Ankit";
let isStudent: boolean = true;
let address: null = null;
let phone: undefined = undefined;
let skills: string[] = ["Playwright", "TypeScript", "SQL"];
console.log("Age:", age);

// String Array
let users: string[] = ["Ankit", "Rahul", "Amit"];
console.log("Users:", users);

// Number Array
let ids: number[] = [1, 2, 3];
console.log("IDs:", ids);

// Access Array Element
console.log("First User:", users[0]);
console.log("Second ID:", ids[1]);

// Add New Element
users.push("Rohit");
numbers.push(40);
console.log("After Push:");
console.log(users);
console.log(numbers);

// Remove Last Element
users.pop();
console.log("After Pop:");
console.log(users);

// Loop Through Array
console.log("All Users:");
for (let user of users) {
    console.log(user);
}

// Type Annotation
let age: number = 25;
console.log(age);
// 25

// any
let value: any = "Hello";
value = 100;
value = true;
console.log(value); 
// 100
// true

// Unknown
let value: unknown = "Hello";
// console.log(value.toUpperCase()); // ❌ Error
if (typeof value === "string") {
console.log(value.toUpperCase()); // ✅ HELLO
}

// Interface
interface Student {
  name: string;
  age: number;
}
const student: Student = {
  name: "Ankit",
  age: 21
}
console.log(student.name);
console.log(student.age);
// Ankit
// 21

// Type Alias
type User = {
  name: string;
  age: number;
};
const user1: User = {
  name: "Ankit",
  age: 22,
};
console.log(user1.name);
console.log(user1.age);  
// Ankit
// 22
