a = "Mutable"
a1 = list(''.join(a))
b = "Marakesh"
b1 = list("".join(b))
c = list(set(a1) & set(b1))

print(f"First list: {a1}")
print(f"Second list: {b1}")
print(f"Crossing symbol {c}")