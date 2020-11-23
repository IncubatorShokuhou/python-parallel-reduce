python-parallel-reduce  
==================
`functools.reduce`的简单并行版本。

[ENGLISH](https://github.com/IncubatorShokuhou/python-parallel-reduce/blob/master/README.md)

快速开始
-----------

安装

```shell
pip install git+https://github.com/IncubatorShokuhou/python-parallel-reduce.git
```
，或
```shell
git clone https://github.com/IncubatorShokuhou/python-parallel-reduce.git
```
然后
```
python setup install
```


并行规约示例:

```python
import os
import time
from reduce_p import reduce_p
from functools import reduce

def max_new(i,j):  #注意：此函数最好可以能够处理None值，以免异常出错。
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

结果 
```
>>> print("serial version spends ",s_time," seconds, result is ",s_result)
serial version spends  49.99384617805481  seconds, result is  499
>>> print("parallelized version spends ",p_time," seconds, result is ",p_result)
parallelized version spends  5.494153022766113  seconds, result is  499
```