#Logical Operators

#Ask the user for two boolean value
value1 = input("Enter the first value (True/False): ").capitalize() == "True"
value2 = input("Enter second value (True/False): ").capitalize() =="True"

#Demonstrate logical operators
print("\nLogical AND:", value1 and value2 )
print("Logical OR:", value1 or value2)
print("Logical NOT (First value):", not value1)
print("Logical Not (Second value):", not value2)


#Bitwise Operators
#define 2 integers
print ("\n----Bitwise Operators----")
n1= 4
n2=3

print("First number:", n1, "Binary:", bin(n1))
print("Second number:", n2, "Binary:", bin(n2))

#demonstrate bitwise operation
print("\nBitwise AND (&):", bin(n1 & n2))
print("Bitwise OR (|):", bin(n1 | n2))
print("Bitwise XOR (^):", bin(n1 ^ n2))
print("Bitwise NOT (~):", bin(~n1))
print("Bitwise NOT (~):", bin(~n2))
print("Left Shift (<<):", bin(n1<<1))
print("Right Shift (>>):", bin(n2>>1))



