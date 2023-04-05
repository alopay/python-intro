# string built in 
# Find and replace


# count - certain characters in a targetted string

sentence = "Each method in this group"
# print(len(sentence))
# print(sentence.count('h'))

sentence_2 = """I will be using Gmail to send user confirmation emails. You will need a Google app password. Don't worry, I have you covered! Watch this video to set up a Google app password.

Also, You will need Docker and Docker Compose installed on a virtual machine. I have a good video to help you set one up on Digital Ocean.

We will also be using a managed database service. I have a good video to help you set one up on...your guessed it, Digital Ocean.

One last thing. You will need a domain! I buy most of mine via Interserve and 123 Reg. But others are available."""

print(len(sentence_2))
print(sentence_2.count('i', 0, 100))


print(sentence_2.count('o', 300, 560))

"""
the second parameter represents the start and the third paramter represents the end 
"""

balance = 333333.22
print(len(str(balance)))