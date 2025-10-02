def f_to_c(f):
    return (5 / 9) * (f - 32)

f = float(input("temperature in F: "))
c = f_to_c(f)
print("temp e in C:", c)
