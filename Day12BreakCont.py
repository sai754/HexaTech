# Break - Stop the loop completely
# Continue - Skip one iteration


# print until 5
# for i in range(1,10):
#     if(i == 6):
#         break
#     print(i)

# # Print odd
# for i in range(1,10):
#     if(i%2 == 0):
#         continue
#     print(i)

# Task 1: Find the first negative value

def first_negative(l):
    for i in l:
        if i<0:
            print(i)
            break

def process_until_duplicate(s):
    set1 = set()
    for i in s:
        if i in set1:
            print("Duplicate is Found")
            break
        else:
            set1.add(i)
            print (f"Processed {i}")
 
 
def censorship_bot(messages, banned_words):
    messages2=set()
    for i in messages:
        for x in banned_words:
            if x in i: 
                break
            else:
                messages2.add(f"Approved Message: {i}")
    print(list(messages2))
 
messages = [
    "Hello everyone!",
    "This is a bad word example!",
    "Let's keep our chat clean!",
    "Oops another bad content!",
    "Have a nice day!"
]
 
banned_words = ["bad", "oops"]
 
 
# Expected output
# Approved message: Hello everyone!
# Approved message: Let's keep our chat clean!
# Approved message: Have a nice day!

if __name__ =='__main__':
    #first_negative([3,5,7,-1,9,-3])
    process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])
    censorship_bot(messages,banned_words)