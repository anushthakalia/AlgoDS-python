def roman_to_int(roman):
    dict ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    sum=0
    n=len(roman)
    for i in range(n):
        if i==n-1:
            sum+=dict[roman[i]]
        elif dict[roman[i+1]]>dict[roman[i]]:
            sum-=dict[roman[i]]
        else:
            sum+=dict[roman[i]]
    print(sum)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        roman=input()
        roman_to_int(roman)