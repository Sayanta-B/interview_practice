ls=[3,6,8,2,5,9,0,4,88]
n=4
pos=-1
def linear(ls,n):
    i=0
    """Using while loop"""
    # while i<len(ls):
    #
    #     if ls[i]==n:
    #         globals() ['pos']=i
    #         return True
    #     i+=1
    # return False
    """Using for loop"""
    for i in range(len(ls)):
        if ls[i]==n:
    # for i in ls:
    #     if i== n:
            globals()['pos'] = i
            return True
    return False

if linear(ls,n):
    print("Found at" ,pos+1)
else:
    print("Not Found")


