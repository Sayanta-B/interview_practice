# ls=[2,4,7,9,14,18]
# n=7
# pos=-1
#
# def binary(ls,n):
#     l=0
#     u=len(ls)-1
#     while l<=u :
#         mid=(l+u)//2
#         if ls[mid]==n:
#             globals()['pos']=mid
#             return True
#         else :
#             if list[mid]<n:
#                 l=mid+1
#             else:
#                 u=mid-1
#         return False
#
# if binary(ls,n)   :
#     print("Found at pos",pos+1)
# else:
#     print("Not found")

# dict1={'name':'sayanta','Age':20,'School':'MRHS'}
# print(dict1['name'])
#
# t=(1,4,3,4,2,3)
# (t[2])=4
# s1={4,5,3,1,8,3,4,8}
# print(s1)
# s1[4]=5
# print(s1)
ls=[2,2,1,3,2]
d=4
m=2
for i in range(len(ls)):
    if (ls[i]+ls[i+1]==4):
        print("found")
        