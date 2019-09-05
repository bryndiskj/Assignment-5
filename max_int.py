# Find the maximum positive integer input by a user 
# stop when a negative value is entered

#num_int = int(input("Input a number: "))

max_int = 0

num_int = int(input("Input a number: "))

while num_int > 0:
    if num_int > max_int:
        max_int = num_int
    if max_int > 0:
            num_int = int(input("Input a number: "))

else:
    print("The maximum is", max_int) 