var marks = [70, 80, 90, 100];
var student = {
  name: 'Tonika',
  batch: 3,
};
console.log(marks + student.batch);

function fullname(firstname, lastname) {
  return 'Welcome ' + firstname + ' ' + lastname;
}

function fullnametemporal(firstname, lastname) {
  return `Welcome  ${firstname}  ${lastname}`;
}

// $ interpolation
// `` supports multi line
//   Task
function movieUrl(domain, genre, year) {
  return `http://${domain}?genere=${genre}&year=${year}`;
}

console.log(movieUrl('imdb.com', 'thriller', 2020));
console.log(fullname('Sai', 'Subash'));

// Destructuring
const [t1, t2, t3 = 80] = [100, 200, null];
console.log(t1, t2, t3);
// null will get assigned to t3
console.log(typeof t3);
// Bottom values : undefined and null
// undefined vs not defined
// undefined is a value(declared a variable but not defined or given value),
// not defined is an error
var x;
typeof x; // will give string undefined
const [, r1, r2, r3 = 80] = [100, 200, null];
console.log(r1, r2, r3); // will give 200, null, 80

const [y1, y2, y3] = [100, 200, 300, 400, 500, 600];
console.log(y1, y2, y3); // will give 100,200,300 other elements will be ignored

// use ... (spread operator like * in python) to collect other items

const [x1, x2, ...x3] = [100, 200, 300, 400, 500, 600];
console.log(x1, x2, x3); // rest operator must only be used at the last

// Spread Operator
marks1 = [70, 80, 60];
marks2 = [...marks1];
marks3 = [100, 60, ...marks1, 75, 68];
console.log(marks2);
console.log(marks3);

marks4 = [...marks1, ...marks3];
console.log(marks4);

console.log(Math.max(...marks4));
