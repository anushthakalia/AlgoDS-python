{
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        print(atoi(string))
# Contirbuted By: Harshit Sidhwa
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# function should return an integer
def atoi(string):
    sum=0
    l=1
    for i in string[::-1]:
        n = ord(i)
        if (n>=48) and (n<=57):
            sum+=(n-48)*l
            l=l*10
        elif (i=='-'):
            sum = 0 - sum
        elif (i=='+'):
            continue
        else:
            return -1
    return sum
            
            
    # Code here