msg = "Hello world"

# Case related methods
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())

quote = "    Hello"

print(quote)
print(quote.strip())

quote1 = "----Hello----"
print(quote1.strip('-'))
print(quote1.lstrip('-'))
print(quote1.rstrip('-'))

# Find and Replace

quote2 = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"

print(quote2.find('something'))  #return the index of the first match
print(quote2.find('Dream'))

print(quote2.replace("Dream", "🔥"))

print(quote2)

# Slicing operator ":"

quote3 = "Dream"
print(quote3[1:3])
print(quote3[3:])
print(quote3[:])
