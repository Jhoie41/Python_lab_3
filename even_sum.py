#use a for loop to iterate through the numbers 1 to 50
total_even_for = 0
for i in range(1,51): 
     if i %2==0:
#calculate the sum of all even number in that range
        total_even_for +=i
#print the result
print("The sum of even numbers from 1 to 50 is",total_even_for,".")


#Use a while loop
total_even_while = 0
i =1
while i <=50:
    if i %2 ==0:
        total_even_while += i
    i+=1
print("The sum of even numbers from 1 to 50 is", total_even_while, ".")