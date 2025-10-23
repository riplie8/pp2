string = "madam"
lower = string.lower()

normalized = ""
for char in lower:
    if char.isalpha():
        normalized += char

reversed = normalized[::-1]

if normalized == reversed:
    print("palindrome")
else:
    print("not palindrome")