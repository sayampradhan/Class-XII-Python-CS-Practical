# WAP to read a text file “myfile.txt” and display the number of vowels/ consonants/
# uppercase/ lowercase characters in the file.

# Open the file in read mode
f = open(r"mytxt.txt", 'r')

# Reading the contents of the file
content = file.read()

# List of vowels
default_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# function to count


def count():
    # count of the required objects
    vowels = 0
    consonants = 0
    uppercase = 0
    lowercase = 0

    for i in content:

        # counting the number of vowels and consonants
        if i not in default_vowels:
            consonants += 1

        else:
            vowels += 1

        # counting the uppercase and lowercase
        if i.isupper():
            uppercase += 1

        else:
            lowercase += 1

        # Printing the count results
        print(
            "The number of the vowels present is", vowels
            "\nThe number of the consonant letters is", consonants
            "\nThe number of uppercase letters is", uppercase
            "\nThe number of lowercase letters is", lowercase
        )

        # Calling the function named "count"
        count()
