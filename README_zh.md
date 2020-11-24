python-parallel-reduce  
==================
`functools.reduce`的简单并行版本。

[中文版](https://github.com/IncubatorShokuhou/python-parallel-reduce/blob/master/README_zh.md)|[ENGLISH](https://github.com/IncubatorShokuhou/python-parallel-reduce/blob/master/README.md)

快速开始
-----------

### 安装

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


### 并行规约示例

```python
import os
import time
from reduce_p import reduce_p, handle_nan
from functools import reduce

@handle_nan 
def max_new(i,j): #对函数进行修饰，使它能够处理None的参数
    time.sleep(0.1)
    return max(i,j)

a = time.time()
p_result = reduce_p(max_new,range(500))
b = time.time()
p_time = b-a

a = time.time()
s_result = reduce(max_new,range(500))
b = time.time()
s_time = b-a

print("串行版本消耗 ",s_time," 秒, 结果是 ",s_result)
print("并行版本消耗 ",p_time," 秒, 结果是 ",p_result)
```

### 结果 
```
>>> print("串行版本消耗 ",s_time," 秒, 结果是 ",s_result)
串行版本消耗  49.99384617805481  秒, 结果是  499
>>> print("并行版本消耗 ",p_time," 秒, 结果是 ",p_result)
并行版本消耗  5.494153022766113  秒, 结果是  499
```

### 参数
```python
reduce_p(function, iterable[,n_jobs ,initializer])
```
`function`, `iterable`, `initializer`: 与`functools.reduce`相同  

`n_jobs`: 进程数。默认值使用全部cpu。

### 注意！
仅推荐在 `iterable` 长度远大于cpu个数时使用, 否则它将不一定比 `functools.reduce`快。

`function` 最好能够处理参数中包含 `None`的情况，否则可能出现错误，尤其在`iterable`长度较小时。