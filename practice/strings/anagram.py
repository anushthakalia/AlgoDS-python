def anagram(arr1, arr2):
    if len(arr1)!=len(arr2):
        return 'NO'
    else:
        dict1={}
        for i in range(len(arr1)):
            if arr1[i] in dict1.keys():
                dict1[arr1[i]]+=1
            else:
                dict1[arr1[i]]=1
        for i in range(len(arr2)):
            if arr2[i] in dict1.keys():
                dict1[arr2[i]]-=1
            else:
                return 'NO'
        if all(val==0 for val in dict1.values()):
            return 'YES'
        else:
            return 'NO'
    


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
	    while True:
	        try:
	            arr1 = input()
	            arr2 = input()
	        except EOFError:
	            break
	    val = anagram(arr1, arr2)
	    print(val)