#ask the user to input a numeric grade
grade= int(input("Enter your grade: "))

"""use if-elif-else structure to conert the numeric grade to 
letter grade based on typical scale:
90-100:A ; 80-89:B ; 70-79:C ; 60-69:D ; 0-59:F"""
if grade <0 or grade >100:
    print("invalid grade. please enter a number between 0 and 100")
elif grade >= 90:
    letter_grade ="A"
elif grade >= 80:
    letter_grade ="B"
elif grade >= 70:
    letter_grade ="C"
elif grade >= 60:
    letter_grade ="D"
else:
    letter_grade ="F"

#print the letter grade
if grade >= 0 and grade <= 100:
    print("YOur grade is:", letter_grade)

#include a final message using conditional expression 
message= "Congratulations you passed!" if letter_grade in ["A", "B", "C"] else "keep trying! you can do better next time."
print(message)