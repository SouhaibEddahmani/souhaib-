t=[[10,100,1],[-3,10,200],[111,20,222]]
def max(t):
    max=t[0][0]
    for i in range (len(t)):
        for j in range(len(t)):
            if t[i][j]>max :
                max=t[i][j]
                return max
print(max(t))
def min(t):
    min=t[0][0]
    for i in range (len(t)):
        for j in range(len(t)):
            if t[i][j]<min :
                min=t[i][j]
                return min
print(min(t))
def moyenne(t):
    moyenne=0
    s=0
    for i in range (len(t)):
        for j in range(len(t[i])):
            s+=t[i][j]
    moyenne= s/(len(t)*len(t[i]))
    return moyenne
print(moyenne(t))
def median_list(t):
    l=[]
    for i in t :
        for j in i :
            l.append(j)
    for i in range(len(t)):
        for j in range(len(t)):
            if l[i]<l[j] :
                a=l[i]
                l[i]=l[j]
                l[j]=a
        median = l[len(l)//2]
        return median
print(median_list(t))

