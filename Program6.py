# Remove all the lines that contain the character `a' in a file and write it
# to another file.

# Opening the original file in read mode
original_file = open(
    r"original.txt"
    "r"
)

# Opening the new file in write mode
new_file = open(
    r"newfile1.txt",
    "w"
)

# Opening an another file in write mode
new_file1 = open(
    r"newfile2.txt",
    'w'
)

# File object for original file
lines = original_file.readlines()

# Reading the words in the object file and write them to the new file if they
# contain the letter 'a' for both uppercase and lowercase

try:
    for i in lines:
        if 'a' not in i:
            new_file.write(i)

        elif 'A' not in i:
            new_file.write(i)

        else:
            new_file1.write(i)

        print("SUCCESSFULLY EXECUTED...")

except Exception as E:
    print("FAILED...")
    print(E)


# Close the files
original_file.close()
new_file.close()
new_file1.close()
