reduce_p
==================
Simple parallelized reduce for Python instead of `functools.reduce`, which is serial.



Quick Start
-----------

Installation

```shell
pip install git+https://github.com/IncubatorShokuhou/reduce_p.git
```

Parallel iteration with a process/CPU:

```python
import os
import time
from reduce_p import reduce_p
form functools import reduce

def max_new(i,j):  #attention: the function should better be able to handle with a None parameter
    time.sleep(0.1)
    if i == None:
        if j == None:
            return None
        else:
            return j
    else:
        if j == None:
            return i
        else:
            return max(i,j)

a = time.time()
reduce_p(max_new,range(500))
b = time.time()
p_time = b-a

a = time.time()
reduce_s(max_new,range(500))
b = time.time()
s_time = b-a

print("serial version spends ",s_time," seconds")
print("parallelized version spends ",p_time," seconds")
```
