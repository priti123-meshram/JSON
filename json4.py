# Python dictionary(sort by key) object ko json data : mai convert karne ka program likho?

import json
n={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4,
}
p=json.dumps(n,sort_keys=True)
print(p)













