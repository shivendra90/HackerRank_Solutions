# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
Student = namedtuple("Student", input().split())

list_students = [Student(*input().split()) for _ in range(n)]
marks = [int(s.MARKS) for s in list_students]

print(round((sum(marks) / n), 2))