'''
Modules
--------

--> A modules is a python file (.py) that written using function, variables, operators, etc.

1. built-in modules:
 ------------------------
--> The modules are developed by programmers and those comes with installation

* math:
---------
import math
print(math.pow(2,3))

* os:
-------
import os
print(os.getcwd())

* sys:
--------
import sys
print(sys.version)

* random:
----------
import random
print(random.randint(1000,9999))


2. user-define modules
------------------------

* importing specific function from modules
--> syntax module name import function
eg:
---
from manoj import add_
print(add_(2,3))

* using alias name or different names
------------------------------------------
--> syntax : import module as alias name
eg:
---

'''

import manoj as mk
print(mk.add_(2,3))
