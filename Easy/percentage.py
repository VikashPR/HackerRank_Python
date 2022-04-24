if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
# Soultion Start
student_score = student_marks[query_name]
sum = 0
for x in student_score:
    sum += x;
percentage = "{:.2f}".format(sum/3)
print(percentage)
# Solution End