var a = 10; // Global Scope
console.log(a);

// Defination of the function
function pringHello() {
  console.log("Hello SoftwareX");
  var a = 20;
  console.log(a);
  if (true) {
    var a = 30;
    console.log(a);
  }
  console.log("F ->",a);
}
console.log("G ->",a);
printHello();
