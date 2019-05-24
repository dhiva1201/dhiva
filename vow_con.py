c=input()
if(c.isalpha()):
    c=c.lower()
    x="aeiou"
    if c in x:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
