def reverse_sentence():
    s = input("Enter a sentence: ")
    words = s.split()
    return " ".join(reversed(words))

print(reverse_sentence())
