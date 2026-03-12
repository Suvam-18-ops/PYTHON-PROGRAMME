s = input("Enter the character: ")

if s.isalnum():
    if s.isalpha():
        if s.isupper():
            if s in "AEIOUaeiou":
                print("It is alphabet and vowel")
            else:
                print("It is alphabet and consonant")
            print("It is uppercase")

        elif s.islower():
            if s in "AEIOUaeiou":
                print("It is alphabet and vowel")
            else:
                print("It is alphabet and consonant")
            print("It is lowercase")

    elif s.isdigit():
        print("It is a digit")
else:
    print("It is a special character")
