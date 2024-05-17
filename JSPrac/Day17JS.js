2 + 3
var name = "Sai subash"

name + " is super cool 🎉"
'Sai subash is super cool 🎉'

3 ** 2
9
typeof(name)
'string'
typeof(9)
'number'
typeof(true) 
'boolean'
typeof(false) // False 
'boolean'
var marks = [70, 80, 90, 100]

marks
(4) [70, 80, 90, 100]

var student =  {
    "name" : "Tonika",
    "batch" : 3
}

typeof(student)
'object'
typeof(marks)
'object'
student["name"]
'Tonika'
marks[0]
70
student
{name: 'Tonika', batch: 3}
student["name"] // box syntax
'Tonika'
student.name
'Tonika'
student.name  + ' is in ' + student.batch 
'Tonika is in 3'
student.name  + ' is in batch ' + student.batch 
'Tonika is in batch 3'
// type casting or coercion
undefined
[]  + [] // Will result in Empty string
[5, 6, 10] + " nice" // Will aoutomatically convert the object into string and concatenate