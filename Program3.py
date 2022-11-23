# Write a function in python which accept a list of marks
# of students and return the minimum mark,
# maximum mark and the average marks.
# Use the same function to test.

# list of the marks of students
mark_list = []

# loop for adding/appending marks to the list
for i in range(int(input(
    "Enter the number of students: "
))):

    marks = int(input("Enter the marks: "))

    mark_list.append(marks)

print("The list of marks is: ", mark_list)

# function to find the highest marks obtained


def maximum(a=mark_list):
    a = sorted(a)

    print(
        "The highest marks obtained is", a[-1]
    )

# function to find the minimum


def minimum(a=mark_list):
    a = sorted(a)
    print(
        "The lowest marks obtained is", a[0]
    )

# function to find the average


def average(a=mark_list):
    add = sum(a)
    length = len(a)
    average = (add/length)

    print(
        "The average of all the marks is"
        "{:2f}".format(average)
    )

# main function to call all the necessary functions at once


def call(a=mark_list):
    minimum(a=mark_list)
    maximum(a=mark_list)
    average(a=mark_list)


# call the main function
call(mark_list)
