diccionary = {
    "a" : 1,
    "e" : 2
}
print()
print(diccionary)
print(f"clave a: {diccionary["a"]}")
print(f"clave e: {diccionary["e"]}")

diccionary2 = {"numbers": [10,20,30],
               "grops":("a", 1, "b", 2),
               "z": (5) 
}

print(diccionary2)
print(f"clave numbers: {diccionary2['numbers']}")
print(f"clave groups: {diccionary2["grops"]}")

print(f"clave numbers: {diccionary2["numbers"][1]}")
print(f"clave groups: {diccionary2["grops"],["b"]}")

print(diccionary2["z"])