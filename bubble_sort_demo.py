#use a list of unsorted integers
number=[64,25,12,22,11]
print("original list:",number)
#implement the bubble sort algorithm using nested loop
n= len(number)
for i in range(n-1):
    for j in range(n-1-i):
        #compare adjacent element
        if number[j] > number[j+1]:
            #swap elements if they are in the wrong order
            number[j], number[j+1] = number[j+1], number[j]
#print the list at each pass of the outer loop to show the progress of the sorting
    print("After pass", i+1, ":", number)
#print the sorted list
print("Final sorted list:", number)