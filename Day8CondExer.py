#Task 1
stock1 = 'Vanilla'
stock2 = 'Lime'
stock3 = 'Chocolate'

stocks = [stock1, stock2, stock3]

#Ask the user for their flavour
flavour = input("Enter your flavour: ")

if flavour in (stock1, stock2, stock3):
  print('Yes, we do have it')
else:
  print('No, we dont have it')

if (flavour == stock1) or (flavour == stock2) or (flavour == stock3):
  print('Yes, we do have it')
else:
  print('NO, we Dont have it')

output = "Yes, Available" if flavour in stocks else "Not Available"
print(output)

# Code Quality
# 1. Readability
# 2. Maintainability
# 3. Extensiblility
# 4. Performance
# 5. Testability

# Ternary Operators ( 3 operands )
# "Cool" if 5>4 else 4

# Binary Operators ( 2 operands )
# 5 > 4
# Arithmetic Operators +,-,/,*

# Unary Operators (1 operand)
# not operator, ++, --
