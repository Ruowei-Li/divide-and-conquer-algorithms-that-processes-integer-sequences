
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
        turn = 0
        while left <= right:
            turn += 1
            mid = (left + right) // 2
            if s1[mid] == element:
                index_position = get_highest_index(s1, mid)
                break

            if s1[left] <= s1[mid]:
                if (element >= s1[left]) and (element < s1[mid]):
                    right = mid
                else:
                    left = mid + 1

            else:
                if (element <= s1[right]) and (element > s1[mid]):
                    left = mid + 1
                else:
                    right = mid
            
        print(index_position, end = "\n")
 

main()
