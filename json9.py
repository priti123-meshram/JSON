# Apki pass ek shopping name ki ek dictionary hai Apki dictionary ka use kar ke ek json file create karna hai.
#  Aur apko kuch task perform karne hai jaise ki 1. main dekhna chahta hu shopping list ko json file dekhna.
#     phir main user se poochu ga ki kon sa item khareedna chahte ho.
#     uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.
#     phir aapka wo number of items json file se remove karna hai.
#     Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.

import json
a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
with open("shopping.json","w")as files:
    json.dump(a,files,indent=4)



# a=int(input("enter the num"))
# b=a%10
# c=(a//10)%10
# d=(a//100)%10
# e=(a//1000)%10
# f=(a//10000)%10
# g=(c%10000,d%1000,e%100,f%10)
# print(g)

