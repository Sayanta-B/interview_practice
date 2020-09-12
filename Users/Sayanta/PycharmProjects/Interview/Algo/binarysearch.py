pos=-1
ls=[3,8,4,6,0,10,7,5]
ls.sort()
n=7
def binary(ls,n):
    l=0
    u=len(ls)-1
    while l<u :
        mid=(l+u)//2
        if ls[mid]==n:
            globals()['pos'] = mid
            return True
        else :
            if ls[mid]<n:
                l=mid
            else:
                u=mid
if binary(ls,n):
    print("Found at",pos+1)
else:
    print("Not Found")
