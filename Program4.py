# WAP to read a text file “myfile.txt” line by line and display each word separated by a #.

# Opening the file in read mode
fh = open(
    r"myfile.txt",
    'r'
)

# Reading content of the file
content = fh.read().split()

# Print the words separated by '#'
for x in content:
    print(x, end="#")
