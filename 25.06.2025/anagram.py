s1 = input("First word: ")
s2 = input("Second word: ")

print("Anagram" if sorted(s1) == sorted(s2) else "Not an Anagram")
