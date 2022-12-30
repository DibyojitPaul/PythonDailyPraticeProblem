if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    query_name=''
    def marksAverage(query_name,student_marks):
        marksAverage=sum(student_marks[query_name])/3
        return marksAverage
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("%.2f" % marksAverage(query_name, student_marks))