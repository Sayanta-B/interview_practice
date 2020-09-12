
ls=[4,3,6,4,9,8,0]

def bubble(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j]>ls[j+1]:
                temp=ls[j]
                ls[j]=ls[j+1]
                ls[j+1]=temp
bubble(ls)
print(ls)