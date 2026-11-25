#Create a list of at least 5 integers
number=[20,25,15,35,7,22]
#print the original list
print("Original list:", number)
#print a sorted version of the list using sorted()
sorted_number=sorted(number)
print("Sorted list using sorted():", sorted_number)
#use .sort() method to sort the list
number.sort()
print("Sorted list using .sort():", number)
#add new integer to the list
number.append(32)
print("New list after adding an element:", number)
#remove an element from the list
number.remove(22)
print("New list after removing an element:", number)
#use the reverse() method on the list
number.reverse()
print("Reversed list:", number)
