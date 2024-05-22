console.log('Hello');

// console.log("Hi from loops");
// const marks = [40, 50, 60, 70, 40];

// console.log("Normal for loop");
// for (let i = 0; i < marks.length; i++) {
//   console.log(marks[i]);
// }

// console.log("for...in");
// for (let idx in marks) {
//   console.log(marks[idx]);
// }

// console.log("for...of"); // for...in (python)
// for (let mark of marks) {
//   console.log(mark);
// }

// for...in
// const avenger = {
//   name: "Tony Stark",
//   house: "🏘️",
//   networth: "💰💰💰",
//   power: "🤖",
//   phrase: "❤️ you 3000",
// };

// for (let key in avenger) {
//   console.log(key, avenger[key]);
// }

// console.log(Object.keys(avenger));
// console.log(Object.values(avenger));
// for of will not work with object, for in will work with both object and array
const avenger = {
  name: 'Tony Stark',
  house: '🏘️',
  networth: '💰💰💰',
  power: '🤖',
  phrase: '❤️ you 3000',
};

const details = {
  age: 40,
  power: '💿',
};

// Merging objects
console.log({ ...avenger, ...details }); // ** - unpacking operator
console.log({ ...details, ...avenger }); // only unique keys

const heights = [120, 140, 190, 80, 170];
heights[0] = 90;
console.log(heights);

// Implicit Coercion
// JS automatically converts the data

var a1 = 3;
var a2 = '5';
console.log(a1 + a2); // gives 35
console.log(a1 - a2); // gives -2

// Explicit Coercion
// We are changing the data type
console.log(x1 + parseInt(x2));

// Comparison
// == and ===
// == Checks only for values, it allows coercion
// === Checks strictly for data type and values
