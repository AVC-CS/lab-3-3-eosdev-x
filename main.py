def main():
    # Step 1: Get input from the user
    num1 = int(input("Please enter the first integer value: "))
    num2 = int(input("Please enter the second integer value: "))
    num3 = int(input("Please enter the third integer value: "))

    # Step 2: Determine the maximum value using if-else statements
    maxnum = num1  # Start by assuming num1 is the maximum

    if num2 > maxnum:  # Check if num2 is greater than the current max
        maxnum = num2 

    if num3 > maxnum:  # Check if num3 is greater than the current max
        maxnum = num3

    # Step 3: Print the result
    print("The greatest number is:", maxnum)  

    return maxnum


if __name__ == '__main__':
    main()
