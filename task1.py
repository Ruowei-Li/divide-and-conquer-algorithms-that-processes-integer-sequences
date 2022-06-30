
import sys

def get_highest_index(s1, index_position):
    value = s1[index_position]
    while ((index_position + 1) < len(s1)) and (s1[index_position + 1] == value):
        index_position += 1
    return index_position
    

def main():
    first_line = sys.stdin.readline().strip().split(" ")
    second_line = sys.stdin.readline().strip().split(" ")
    s1 = [int(i) for i in first_line]
    s2 = [int(i) for i in second_line]
    for element in s2:
        index_position = -1 # initial value
        left = 0
        right = len(s1) - 1
        while left <= right:
            mid = (left + right) // 2
            if s1[mid] < element:
                left = mid + 1
            elif s1[mid] > element:
                right = mid - 1
            else:
                index_position = get_highest_index(s1, mid)
                break
        print(index_position, end = "\n")
 

main()
