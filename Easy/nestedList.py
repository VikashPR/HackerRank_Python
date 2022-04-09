if __name__ == '__main__':
    students = []
    sortedList = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        students += [[name,score]]
        sortedList += [score]
    
    secondLargest = sorted(list(set(sortedList)))[1]
    
    for i,j in sorted(students):
        if(j == secondLargest):
            print(i)
            