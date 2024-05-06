quote = 'Dream'

#print(quote[<start>:<end>:<skip>])
print(quote[1:3])
print(quote[-1])
print(quote[-4:-1])
print(quote[1:4:2])

#  0 1 2 3 4
#  D r e a m
# -5-4-3-2-1

print(quote[::-1])

print(quote[-1:-4:-1])

palin = 'malayalam'
print(palin == palin[::-1])

# Task 2: Remove junk[*,(] to find the secret

message1 = "    🚨🔍📱🔑*****secret_code✌️(("
code = "SECRET_CODE✌️"
i = message1.find("🔑")
message1 = message1[i+1:]
# message1 = message1.upper()
# message1 = message1.replace("*","")
# message1 = message1.replace("(","")
message1 = message1.strip("*").strip("(").upper()

if (message1 == code):
  print("You are a hacker")
else:
  print("Try Again")
# Can use strip too to remove junk

