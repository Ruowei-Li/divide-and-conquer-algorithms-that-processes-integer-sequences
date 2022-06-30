
import sys



def main():
    first_line = sys.stdin.readline().strip().split(" ")
    second_line = sys.stdin.readline().strip().split(" ")
    
    length_S1 = len(first_line)
    for i in second_line:
        print(length_S1 + int(i), end = "\n")
 

main()


