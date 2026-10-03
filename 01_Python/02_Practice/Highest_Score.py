student_score=[150,200,130,88,99,100,23,78,98,45,67,88,77,55,43,54,90,96,83,58,92]
# total_score=sum(student_score)
# print(total_score)
total=0
max=0
for score in student_score:
    total+=score
print(total)
# print(max(student_score))
for score in student_score:
    if score > max:
        max= score
print(max)