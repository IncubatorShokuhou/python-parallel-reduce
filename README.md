python-parallel-reduce  
==================
Simple parallelized reduce for Python instead of `functools.reduce`, which is serial.

[中文版](https://github.com/IncubatorShokuhou/python-parallel-reduce/blob/master/README_zh.md)

Quick Start
-----------

Installation

```shell
pip install git+https://github.com/IncubatorShokuhou/python-parallel-reduce.git
```
,or
```shell
git clone https://github.com/IncubatorShokuhou/python-parallel-reduce.git
```
then
```
python setup install
```
Parallel reduce example:

```python
import os
import time
from reduce_p import reduce_p
from functools import reduce

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
p_result = reduce_p(max_new,range(500))
b = time.time()
p_time = b-a

a = time.time()
s_result = reduce(max_new,range(500))
b = time.time()
s_time = b-a

print("serial version spends ",s_time," seconds, result is ",s_result)
print("parallelized version spends ",p_time," seconds, result is ",p_result)
```

result  
```
>>> print("serial version spends ",s_time," seconds, result is ",s_result)
serial version spends  49.99384617805481  seconds, result is  499
>>> print("parallelized version spends ",p_time," seconds, result is ",p_result)
parallelized version spends  5.494153022766113  seconds, result is  499
```