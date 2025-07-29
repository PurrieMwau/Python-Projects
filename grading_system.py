#Ash the user to input a score
score = int(input("Enter the student's score (0 - 100): "))

if score >= 90:
    grade = 'A' 
    
elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C" 

elif score >= 60:
    grade = "D" 

else:
    grade = "F"  

#print the result

print(f"The student's grade is: {grade}")