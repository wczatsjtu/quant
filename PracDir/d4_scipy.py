# ref:https://wizardforcel.gitbooks.io/python-quant-uqer/content/8.html

# 一、SciPy概述
# 前篇已经大致介绍了NumPy，接下来让我们看看SciPy能做些什么。NumPy替我们搞定了向量和矩阵的相关操作，基本上算是一个高级的科学计算器。SciPy基于NumPy提供了更为丰富和高级的功能扩展，在统计、优化、插值、数值积分、时频转换等方面提供了大量的可用函数，基本覆盖了基础科学计算相关的问题。
# 在量化分析中，运用最广泛的是统计和优化的相关技术，本篇重点介绍SciPy中的统计和优化模块，其他模块在随后系列文章中用到时再做详述。
# 本篇会涉及到一些矩阵代数，如若感觉不适，可考虑跳过第三部分或者在理解时简单采用一维的标量代替高维的向量。
# 首先还是导入相关的模块，我们使用的是SciPy里面的统计和优化部分：
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

