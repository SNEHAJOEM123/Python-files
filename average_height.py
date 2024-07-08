student_heights=input("Input a list of student heights separated by space\n").split()
for i in range(0,len(student_heights)):
    student_heights[i]=int(student_heights[i])

print(student_heights)
no_of_students=0
sum_of_heights=0
for height in student_heights:
    no_of_students+=1
    sum_of_heights+=height
avg_height=round(sum_of_heights/no_of_students) 
print(f"Average height is {avg_height}")   

