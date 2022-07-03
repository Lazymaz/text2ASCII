import pyfiglet as con
import sys

c2 = input("text: ")

solution = con.figlet_format(c2)

sys.stdout = open('art.txt', 'wt')
print(solution)
