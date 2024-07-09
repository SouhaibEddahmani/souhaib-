

def max_list(l):

    maxim = max([0])
    for i in l:
        if l[i]>max:
            max = i
    return maxim
def min_list(l):
    minum = min([0])
    for i in l:
        if l[i] < minum:
            minum = i
        return minum


def moyenne_list(l):
    s = 0
    for i in l:
        s+=i
    return s//len(l)

def median_list(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j] :
                a=l[i]
                l[i]=l[j]
                l[j]=a
        median = l[len(l)//2]
        return median
