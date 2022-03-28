# json data ko python object main convert karne ka program likho?
# dumps write karta hai and
# loads read karta hai
# read o/p deta hai tarminal par
# write file creat karta hai


import json
n='{"Name":"Ram","Class":"IV","Age":9}'
a=json.loads(n)
print(a)