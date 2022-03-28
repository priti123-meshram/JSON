# import json
# print("*WELCOME TO LOGIN SIGN UP*")
# print("you want login and sign up")
# user=input("enter the login and sign up")
# if user=="sign up":
#     user=input("enter the name")
#     password1=int(input("enter the password"))
#     password2=int(input("enter the confirm password"))
#     if password1==password2:
#         description=input("enter the description")
#         gander=input("enter the gander")
#         date_of_birth=input("enter the date_of_birth")
#         hobby=input("enter your hobby")
#         dict={"user":user,"password1":password1,"password2":password2,"description":description,"gander":gander,"date_of_birth":date_of_birth,"hobby":hobby}
#         out_file=open("text1.json","w")
#         json.dump(dict,out_file,indent=4)
#     else:
#         print("wrong password")
# else:
#     if user=="login":
#         name=input("enter the name")
#         password1=int(input("enter the password"))
#         with open("text1.json","r")as file:
#             b=json.load(file)
#             if password1==b["password2"]:
#                 print("login sucessfull")
#             else:
#                 print("fail") 
#     else:
#         print("wrong")






import json
print("*WELCOME TO LOGIN SIGN UP*")
print("you want login and sign up")
user=input("enter the login and sign up")
if user=="sign up":
    user=input("enter the name")
    password1=int(input("enter the password"))
    password2=int(input("enter the confirm password"))
    if password1==password2:
        description=input("enter the description")
        gander=input("enter the gander")
        date_of_birth=input("enter the date_of_birth")
        hobby=input("enter your hobby")
        dict={"user":user,"password1":password1,"password2":password2,"description":description,"gander":gander,"date_of_birth":date_of_birth,"hobby":hobby}
        out_file=open("text1.json","w")
        json.dump(dict,out_file,indent=4)
    else:
        print("wrong password")
else:
    if user=="login":
        name=input("enter the name")
        password1=(input("enter the password"))
        if password1=="a" and password1=="z":
            print(password1)
            with open("text1.json","r")as file:
                b=json.load(file)
            password2=input("enter the confom password")
            if password1==password2:
                print("login sucessfull")
            else:
                print("fail") 
    else:
        print("wrong")






# a=input("enter the name")
# if a=="priti":
#     print("yes it's your account")
#     b=input("enter the email")
#     if b=="priti@123":
#         print("correct e-mail")
#         c=int(input("enter the password"))
#         d=int(input("conform your password"))
#         if c==d:
#             print("log in")
#         else:
#             print("incorrect password")
#     else:
#         print("error")
# else:
#     print("incorrect id")