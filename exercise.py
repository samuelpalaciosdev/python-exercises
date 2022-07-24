# n = number of students
# k = number of apples

#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.

def apple_sharing(n,k):
    # numbers of apples evenly by student
    apples_per_student = k // n
    # remainder of nro of apples by students
    apples_remaining = k % n

    return apples_per_student, apples_remaining

#Print the two answer per the example output.
print(apple_sharing(6,50))