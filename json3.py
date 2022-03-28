# Python object ko json string mai convert karne ka program likho?

import json
priti={"name": "priti",
        "age":21,
        "qualification":"graduation"}
a=json.dumps(priti)
print(a)