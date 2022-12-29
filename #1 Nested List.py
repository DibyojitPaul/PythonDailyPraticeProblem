'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If 

there are multiple students, order their names alphabetically and print each one on a new line.
'''
if __name__ == '__main__':
    lst = list()
    lst2 = list()
    nwlst = list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        lst += [[name, score]]
        lst2 += [score]
    length = len(lst)
    lst2=list(set(lst2))
    lst2.sort()
    
    
    for k in range(1,length+1):
        if lst[-k][1] == lst2[1]:
            nwlst+=[lst[-k][0]]
    nwlst.sort()
    n=len(nwlst)
    for j in range(n):
        print(nwlst[j])
  