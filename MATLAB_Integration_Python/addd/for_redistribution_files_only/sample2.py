#!/usr/bin/env python
"""
Sample script that uses the addd module created using MATLAB Compiler SDK.
Refer to the MATLAB Compiler SDK documentation for more information.
"""

import addd

my_addd = addd.initialize()

# 使用編譯後的函式
result = my_addd.addd(10, 2)
print(result)  # 輸出: 12