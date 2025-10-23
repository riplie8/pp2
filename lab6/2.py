string = "i love Fortnite DADDADADAnono"
uppercase = 0;
lowercase = 0;
for char in string:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print(uppercase, lowercase)