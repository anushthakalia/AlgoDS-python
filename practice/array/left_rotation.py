
def rotLeft(a, d):
    n = len(a)
    shifts = d%n
    temp = a[0:shifts]
    a[0:n-shifts] = a[shifts:]
    a[n-shifts :] = temp
    return a

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()