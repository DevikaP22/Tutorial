def remove(s):
    return "".join(char for char in s if char.lower() not in "aeiou")

i = "Hello, World!"
print("String after removing vowels:", remove(i))
