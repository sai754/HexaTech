# After the 🔑
# message = "    🚨🔍📱🔑secret_code✌️"
# code = "SECRET_CODE✌️"

message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRECT_CODE✌️"

i = message.find("🔑")
output = message.upper()
output = output[i + 1:]

if (output == code):
  print("You are a hacker")
else:
  print("Try Again")
