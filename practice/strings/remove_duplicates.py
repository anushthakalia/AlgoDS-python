# def unique_char(arr): #O(n2)
#     lst=[]
#     for i in arr:
#         if i not in lst:
#             lst.append(i)
#     return lst

def unique_char(arr): # O(n) time complexity and O(1) space complexity
    chars = [False]*256
    for i in range(len(arr)):
        if chars[ord(arr[i])]==False:
            chars[ord(arr[i])]=True
            print(arr[i],end='')
    print()


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
	    arr = input()
	    val = unique_char(arr)
	    print(''.join(val))