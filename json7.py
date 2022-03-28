# .Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

import json
a={"Name": "Abhishek","Designation": "CEO of navgurukul","Gender": "male","Age": 29}
banks_list=open("priti.json","w")
json.dump(a,banks_list,indent=4)
# print(p)
























# n=[2,7,[8,9],[3,4,6],[5,9]]
# sum=0
# i=0
# while i<len(n):
#     # print(n[i])
#     if type(n[i])==list:
#         j=0
#         while j<len(n[i]):
#             # print(n[i][j])
#             sum+=n[i][j]
#             j+=1
#     else:
#         sum+=n[i]        
#     i+=1
# print(sum)    

# a=[1,2,3,4,5,6,7]
# n=int(input("enter the number"))
# print(a[n:]+a[:n])
# # a[2:2]=[100]
# # print(a)



# n=["mina",10,20,"dty",[12,34]]
# i=0
# a=[]
# b=[]
# c=[]
# while i <len(n):
#     if type(n[i])==str:
#         a.append(n[i])
#     elif type(n[i])==list:
#         b.append(n[i])
#     else:
#         c.append(n[i])
#     i=i+1
# print(a)
# print(b)
# print(c)




# n=[1,2,3,8,6,9,6,9,3,2]
# o=[]
# # c=0
# i=0
# while i <len(n):
#     o.append(n[-i])
#     # c=c+1
#     i=i-1
# print(o)
# # print(e)




