print("# Creation of Set")
n1 = {32, 44, 67, 98}
n2 = {11, 30, 65, 44}
print('Initial Set:', n1)

print("\n# Adding Element into the set")
print('Initial Set:', n1)
n1.add(32)
print('Updated Set:', n1)

print("\n# Removing Element From the set")
print('Initial Set:', n1)
n1.remove(67)
print('Updated Set:', n1)

print("\n# Size of set")
print(len(n1))

print("\n# Intersection of the set")
intersection = n1.intersection(n2)
print(intersection)

print("\n# Union of the set")
union = n1.union(n2)
print(union)

print("\n# Difference Between two set")
diff = n1.difference(n2)
print(diff)

print("\n# Symmetric Difference Between two set")
sd = union-diff
print(sd)

print("\n# Iteration of set")
p = iter(n1)
print(next(p))
