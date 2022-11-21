#!/usr/bin/env python
# coding: utf-8

# # 1 Python3 环境搭建
# ## 1.1 Python3 下载
# Python3 最新源码，二进制文档，新闻资讯等可以在 Python 的官网查看到：
# Python 官网：https://www.python.org/
# ## 1.2 Python3 设置环境变量
# ### Windows 系统
# 可以通过以下方式设置：
# * 右键点击"计算机"，然后点击"属性"
# * 然后点击"高级系统设置"
# * 选择"系统变量"窗口下面的"Path",双击即可！
# * 然后在"Path"行，添加python安装路径即可(我的D:\Python32)，所以在后面，添加该路径即可。 ps：记住，路径直接用分号"；"隔开！
# * 最后设置成功以后，在cmd命令行，输入命令"python"，就可以有相关显示。
# ![本地路径](images/1.png)
# 
# ### macOS系统
# * 在终端中输入：
# ```
# export PATH="$PATH:/usr/local/bin/python"
# ```
# 
# ## 1.3 Python3 运行
# ### 3.1 命令行运行
# Windows系统：使用**cmd**，输入`Python`运行
# macOS系统：使用**终端（Terminal）**，输入`Python`运行
# ### 3.2 使用Python脚本
# 
# ### 3.3 使用集成开发环境(IDE)
# * Pycharm
# * VsCode

# # 2 Python3 基本语法
# ## 2.1 程序的格式框架
# ### 缩进
# 一行代码开始前的空白区域，表示程序的格式框架
# * 严格明确：缩进是语法的一部分
# * 所属关系：表达代码间包含和层次关系的唯一手段
# * 长度一致：程序内一致即可，一般用4个空格或1个TAB
# 
# ### 注释
# 用于提高代码可读性的辅助性文字，不被执行
# 
# 单行注释：
# 
# ```python
# # 开头，其后内容为注释
# ```
# 
# 多行注释：
# ```python
# ''' 多行注释第一行
#     多行注释第二行 '''
# ```
# 
# ## 2.2 命名与保留字
# 
# ### 变量
# 
# **程序中用于保存和表示数据的占位符号**
# 
# - 变量采用标识符（名字）来表示，关联标识符的过程叫**命名**
# 
#   _TempStr是变量名字_
# 
# - 可以用等号（=）向变量赋值或修改值，=被称为赋值符号
# 
#   _TempStr = "82F”#向变量TempStr赋值 "82f"_
# 
# - 使用变量之前要先声明
# 
# ### 命名
# 
# **关联标识符的过程**
# 
# - 命名规则：大小写字母、数字、下划线和中文等字符及组合
# - 注意事项：大小写敏感、首字符不能是数字、不与保留字相同
# 
# ### 保留字
# 
# **被编程语言内部定义并保留使用的标识符**
# 
# - Python语言有35个保留字
# - 保留字是编程语言的基本单词，大小写敏感
# 
# 
# ## 2.3数据类型
# 
# **数据类型**：字符串、整数、浮点数、列表
# 例如：10，011，101
# 	整数类型：10011101
# 	字符串类型："10,011,101"
# 	列表类型：[10,011,101]
# 
# ### 字符串
# 
# 1. **由0个或多个字符组成的有序字符序列**
# 
# - 字符串由一对单引号或一对双引号表示
# - 字符串是字符的有序序列，可以对其中的字符进行索引
# 
# 2. **字符串的序号**
# 
# - **正向递增序号和反向递减序号**
# 
# 3. **字符串的使用**
# 
# - **使用[ ]获取字符串中的一个或多个字符**
# 
# 4. **索引**：返回字符串中单个字符	<字符串>[M]
# 
# ```python
# "请输入带有符号的温度值："[0]
# TempStr[-1]
# ```
# 
# 5. **切片**：返回字符串中一段字符子串	<字符串>[M:N]
# 
# 从M开始但是不到N
# 
# ```python
# "请输入带有符号的温度值"[1:3]
# TempStr[0:-1]
# ```
# 
# ### 数字类型
# 
# **整数和浮点数都是数字类型**
# **整数**：数学中的整数
# **浮点数**：数学中的实数，带有小数部分
# 
# ### 列表类型
# 
# **由0个或多个数据组成的有序序列**
# 列表使用[ ]表示，采用逗号分隔各元素
# 	['F', 'f']表示两个元素 'F' 和 'f'
# 使用保留字in判断一个元素是否在列表中
# 	TempStr[-1] in ['C', 'c'] 判断前者是否与列表中某个元素相同
# 
# 
# ## 2.4语句与函数
# 
# ### 赋值语句
# 
# **由赋值符号构成的一行代码**
# 
# - 赋值语句用来给变量赋予新的数据值
# - 赋值语句右侧的数据类型同时作用于变量
# 
# ### 分支语句
# 
# **由判断条件决定程序运行方向的语句**
# 
# - 使用保留字 if elif else 构成条件判断的分支结构
# - 每个保留字所在行的最后存在一个冒号，是语法的一部分，表示后续语句与条件的所属关系
# 
# ### 循环语句
# 
# **由循环结构构成的多次运行的语句***
# ```python
# for <循环变量> in <遍历结构>:
#     <语句块>
# ```
# 
# ### 函数
# 
# **根据输入参数产生不同输出的功能过程**
# 函数采用 <函数名>(<参数>)方式使用
# 
# 
# ## 2.5 Python 程序的输入输出
# 
# ### 输入函数input()
# 
# 使用格式：
# 
# ```python
# <变量> = input(<提示信息字符串>)
# ```
# 
# 用户输入的信息以字符串类型保存在<变量>中
# 
# ### 输出函数print()
# 
# 使用格式：
# 
# ```python
# print(<拟输出字符串或字符串变量>)
# ```
# 
# 字符串类型的一堆引号仅在程序内部使用，输出无引号
# 格式化：
# 
# ```python
# print("转换后的温度是{:.2f}C".format(C))
# 
# #{ }表示槽。后续变量填充到槽中
# #{:.2f}表示将变量C填充到这个位置时取小数点后2位
# ```
# 
# end=""表示输出以什么结尾
# 
# ```python
# print(n,end=",")
# ```
# 
# ### 评估函数eval()
# 
# 使用格式：
# 
# ```python
# eval(<字符串或字符串变量>)
# ```
# 
# 去掉参数最外侧引号并执行余下语句的函数

# # 3 Python应用例子
# ## 3.1 print输出

# In[1]:


# 向Python语言打个招呼吧

print("Hello World!")


# In[3]:


# 变量、字典、列表、循环和输出的结合
# 试着更改一下 DNA 变量中的 ATCG 数量，观察一下输出

DNA="AAATCGCGCATAGCA"
count = {"A":0,"T":0,"G":0,"C":0}
for i in ["A","T","G","C"]:
    count[i] = DNA.count(i)

for i in ["A","T","G","C"]:
    print("{}: {}".format(i,count[i]))


# In[5]:


# 判断和输出结合
# 温度转换，试着输入带符号的温度（如 82F 或 28C）

TempStr = input("请输入带有符号的温度值")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")


# ## 3.2 基本数据类型

# In[22]:


# 数值运算
# 天天向上的力量：每天进步0.001和每天退步0.001的差距

dayup = pow(1.001,365) # pow函数的功能是计算指数
daydown = pow(0.999,365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup,daydown))


# **思考和扩展**
# 
# 1 `print` 中的 `{:.2f}` 和 `format` 代表什么意思？
# 
# 2 如何计算每天进步0.005和每天进步0.01的力量？
# 
# 3 如果只在工作日每天进步0.01，休息日每天退步0.01呢？
# 
# 4 工作日模式要努力到什么水平，才能与每天努力0.01一样？
# 

# In[24]:


# 文本进度条

import time # 导入时间库

scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")


# **思考和扩展**
# 
# 1 如何实现单行刷新？
# 
#     刷新的关键是 \r
# 
# * 刷新的本质是：用之后打印的字符覆盖之前的字符
# * 不能换行：print()需要被控制
# * 要能回退：打印后光标退回到之前的位置```\r```

# In[26]:


# 单行刷新示例

import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)


# ## 3.3 程序的判断结构

# In[28]:


# if, else 的应用
# 计算国际标准下的BMI

height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
who = ""
if bmi < 18.5:
    who = "偏瘦"
elif 18.5 <= bmi < 25:
    who = "正常"
elif 25 <= bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"
print("BMI 指标为:国际'{0}'".format(who))


# **思考和扩展**
# 
# 1 BMI计算有国内和国际标准，如何用国内的标准计算？
# 
# 2 如何同时显示国内和国际标准？

# ## 3.4 程序的循环结构

# In[33]:


# for循环和random库的应用
# 蒙特卡洛方法计算圆周率

from random import random
from time import perf_counter

DARTS = 1000*1000
hits = 0.0
start = perf_counter()

for i in range(1,DARTS+1):
    x, y = random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0:
        hits = hits +1
pi = 4*(hits/DARTS)

print("圆周率的值是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))


# **思考和扩展**
# 
# 1 如何使用其他方法（比如近似公式）计算圆周率？

# ## 3.5 组合数据类型

# In[37]:


# 组合数据类型的应用
# 根据用户输入计算相应的数据特征

def getNum():       #获取用户不定长度的输入
    nums = []
    iNumStr = input("请输入数字(回车退出): ")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出): ")
    return nums
 
def mean(numbers):  #计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)
 
 
n =  getNum() #主体函数
m =  mean(n)

print("平均值:{},方差: ,中位数: .".format(m))


# **思考和扩展**
# 
# 1 如何控制输出时保留的小数位？
# 
# 2 如何增加方差和中位数的计算？

# ## 3.6 文本词频统计

# In[39]:


# 英文文本词频统计
# 哈姆雷特单词统计

def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
 
hamletTxt = getText()
words  = hamletTxt.split()
counts = {}
for word in words:           
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)   #对列表进行排序
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))


# In[3]:


# 中文文本词频统计
# 《三国演义》人物

import jieba

excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))


# **思考和扩展**
# 
# 1 将词频与人物相关联，面向问题，对结果进行优化

# In[17]:


# 制作云图

import jieba
import wordcloud
import matplotlib.pyplot as plt

f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)

for ch in ['\n', '\u3000', '的', '和']:
    txt = txt.replace(ch,"")

    w = wordcloud.WordCloud(font_path = "msyh.ttf",                       width = 1000, height = 700, background_color = "white",                       )    #生成词云对象
w.generate(txt)

plt.imshow(w)  
plt.axis('off')  
plt.show()  

w.to_file("grwordcloud.png")


# ## 3.7 Python爬虫应用

# In[30]:


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import requests
import os
import traceback


def getArticleInf(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("创建标题时出现http错误")
        return None

    bsObj = BeautifulSoup(html, 'html.parser')

    try:
        title = bsObj.find('title').get_text()
    except AttributeError as e:
        print("创建标题时出现Attribute错误")
        return None

    try:
        date = bsObj.find('meta', {'name': "dc.date"})['content']
    except AttributeError as e:
        print("创建标题时出现Attribute错误")
        return None

    try:
        message_tag = {'class': 'c-status-message c-status-message--warning c-status-message--boxed'}
        if bsObj.find_all('p', message_tag):
            downloadURL = url + '_reference.pdf'
        else:
            downloadURL = url + '.pdf'
    except:
        print('构建链接失败')
        return None

    articleInf = [title, date, downloadURL]
    return articleInf

def getArticlePage(page):
    html = urlopen('https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&type=article&page='+str(page))
    bs = BeautifulSoup(html, 'html.parser')
    articlePages = []
    for link in bs.find_all(
            'a', href=re.compile('^(/articles/).*$')):
        if 'href' in link.attrs:
            articlePages.append('https://www.nature.com' + link.attrs['href'])

articles = getArticlePage(1)
articles


# # 4 python计算生态概览
# 
# 
# ## 4.1 Python库之数据分析
# 
# **Numpy：表达N维数组的最基础库**
# 
# - Python接口使用，C语言实现，计算速度优异
# - Python数据分析及科学计算的基础库，支持Pandas等
# - 提供直接的矩阵运算、广播函数、线性代数等功能
# 
# [**http://www.numpy.org**](http://www.numpy.org)
# 
# **Pandas：Python数据分析高层次应用库**
# 
# - 提供了简单易用的数据结构和数据分析工具
# - 理解数据类型与索引的关系，操作索引即操作数据
# - Python最主要的数据分析功能库，基于Numpy开发
# 
# Series = 索引+一维数据
# DataFrame = 行列索引+二维数据
# [**http://pandas.pydata.org**](http://pandas.pydata.org)
# 
# **SciPy：数学、科学和工程计算功能库**
# 
# - 提供了一批数学算法及工程数据运算功能
# - 类似Matlab，可用于傅里叶变换、信号处理等应用
# - Python最主要的科学计算功能库，基于Numpy开发
# 
# [**http://www.scipy.org**](http://www.scipy.org)
# 
# ## 4.2 Python库之数据可视化
# 
# **Matplotlib：高质量的二维数据可视化功能库**
# 
# - 提供超过100中数据可视化显示效果
# - 通过matplotlib。pyplot子库调用各种可视化效果
# - Python最主要的数据可视化功能库，基于Numpy开发
# 
# [**http://matplotlib.org**](http://matplotlib.org)
# 
# **Seaborn：统计类数据可视化功能库**
# 
# - 提供了一批高层次的统计类数据可视化展示效果
# - 主要展示数据间分布、分类和线性关系等内容
# - 基于Matplotlib开发，支持Numpy和Pandas
# 
# [**http://seaborn.pydata.org/**](http://seaborn.pydata.org/)
# 
# **Mayavi：三维科学数据可视化功能库**
# 
# - 提供了一批简单易用的3D科学计算数据可视化展示效果
# - 目前版本是Mayavi2，三维可视化最主要的第三方库
# - 支持Numpy、TVTK、Traits、Envisage等第三方库
# 
# [**http://docs.enthought.com/mayavi/mayavi/**](http://docs.enthought.com/mayavi/mayavi/)
# 
# ## 4.3 Python库之文本处理
# 
# **PyPDF2：用来处理pdf文件的工具集**
# 
# - 提供了一批处理PDF文件的计算功能
# - 支持获取信息、分隔/整合文件、加密解密等
# - 完全Python语言实现，不需要额外以来，功能稳定
# 
# 
# [**http://mstamy2.github.io/PyPDF2**](http://mstamy2.github.io/PyPDF2)
# 
# **NLTK：自然语言文本处理第三方库**
# 
# - 提供了一批简单易用的自然语言文本处理功能
# - 支持语言文本分类、标记、语法句法、语义分析等
# - 最优秀的Python自然语言处理库
# 
# [**http://www.nltk.org/**](http://www.nltk.org/)
# 
# **Python-docx：创建或更新Microsoft Word文件的第三方库**
# 
# - 提供创建或更新.doc .docx等文件的计算功能
# - 增加并配置段落、图片、表格、文字等，功能全面
# 
# [**http://python-docx.readthedocs.io/en/latest/index.html**](http://python-docx.readthedocs.io/en/latest/index.html)
# 
# ## 4.4 Python库之机器学习
# 
# **Scikit-learn：机器学习方法工具集**
# 
# - 提供一批统一化的机器学习方法功能接口
# - 提供聚类、分类、回归、强化学习等计算功能
# - 机器学习最基本且最优秀的Python第三方库
# 
# [scikit-learn: machine learning in Python — scikit-learn 0.16.1 documentation](http://scikit-learn.org/)
# 
# **TensoFlow：AlphaGo背后的机器学习计算框架**
# 
# - 谷歌公司推动的开源机器学习框架
# - 将数据流图作为基础，图节点代表运算，边代表张量
# - 应用机器学习方法的一种方式，支撑谷歌人工智能应用
# 
# [**https://www.tensorflow.org/**](https://www.tensorflow.org/)
# 
# **MXNet：基于神经网络的深度学习计算框架**
# 
# - 提供可扩展的神经网络及深度学习计算功能
# - 可用于自动驾驶、机器翻译、语音识别等众多领域
# - Python最重要的深度学习计算框架
# 
# [**https://mxnet.incubator.apache.org/**](https://mxnet.incubator.apache.org/)
# 
# 
# ## 4.5 从Web解析到网络空间
# 
# ### 一、Python库之网络爬虫
# 
# **Request：最友好的网络爬虫功能库**
# 
# - 提供了简单易用的类HTTP协议网络爬虫功能
# - 支持连接池、SSL、Cookies、HTTPS(S)代理等
# - Python最主要的页面级网络爬虫功能库
# 
# [**http://www.python-requests.org/**](http://www.python-requests.org/)
# 
# **Scrapy:优秀的网络爬虫框架**
# 
# - 提供了构建网络爬虫系统的框架功能，功能半成品
# - 支持批量和定时网页爬取、提供数据处理流程等
# - Python最主要且最专业的网络爬虫框架
# 
# [**https://scrapy.org**](https://scrapy.org)
# 
# **pyspider：强大的Web页面爬取系统**
# 
# - 提供了完整的页面爬取系统构建功能
# - 支持数据库后端、消息队列、优先级、分布式架构等
# - Python重要的网络爬虫类第三方库
# 
# [**http://docs.pyspider.org**](http://docs.pyspider.org)
# 
# ### 二、Python库之Web信息提取
# 
# **Beautiful Soup： HTML和XML的解析库**
# 
# - 提供了解析HTML和XML等Web信息的功能
# - 又名beautifulsoup4或bs4，可以加载多种解析引擎
# - 常与网络爬虫库搭配使用，如Scrapy、requests
# 
# [**https://www.crummy.com/software/BeautifulSoup/bs4**](https://www.crummy.com/software/BeautifulSoup/bs4)
# 
# **Re：正则表达式解析和处理功能库**
# 
# - 提供了定义和解析正则表达式的一批通用功能
# - 可用于各类场景，包括顶点的Web信息提取
# - Python最主要的标准库之一，无需安装
# 
# [**https://docs.python.org/3.6/library/re.html**](https://docs.python.org/3.6/library/re.html)
# 
# **Python-Goose：提供文章类型Web页面的功能库**
# 
# - 提供了对Web页面中文章信息、视频等元数据的提取功能
# - 针对特定类型Web页面，应用覆盖面较广
# - Python最主要的Web信息提取库
# 
# [**https://github.com/grangier/python-goose**](https://github.com/grangier/python-goose)
# 
# ### 三、Python库之Web网站开发
# 
# **Django：最流行的Web应用框架**
# 
# - 提供了构建Web系统的基本应用框架
# - MTV模式：模型（model）、模板（Template）、视图（Views）
# - Python最重要的Web应用框架，略微复杂的应用框架
# 
# [**https://www.djangoproject.com**](https://www.djangoproject.com)
# 
# **Pyramid：规模适中的Web应用框架**
# 
# - 提供了简单方便构建Web系统的应用框架
# - 不大不小，规模适中。适合快速构建并适度扩展类应用
# - Python产品级Web应用框架，起步简单可扩展性好
# 
# [**https://trypyramid.com/**](https://trypyramid.com/)
# 
# **Flask：Web应用开发框架**
# 
# - 提供了最简单构建Web系统的应用框架
# - 特点是：简单、规模小、快速
# - Django > Pyramid > Flask
# 
# [**http://flask.pocoo.org**](http://flask.pocoo.org)
# 
# ### 四、Python库之网络应用开发
# 
# **WeRoBot：微信公众号开发框架**
# 
# - 提供了解析微信服务器消息及反馈消息的功能
# - 建立微信机器人的重要技术手段
# 
# [**https://github.com/offu/WeRoBot**](https://github.com/offu/WeRoBot)
# 
# **aip：百度AI开放平台接口**
# 
# - 提供了访问百度AI服务的Python功能接口
# - 语音、人脸、OCR、NLP、知识图谱、图像搜索等领域
# - Python百度AI应用的最主要方式
# 
# [**https://github.com/Baidu-AIP/python-sdk**](https://github.com/Baidu-AIP/python-sdk)
# 
# **MyQR：二维码生成第三方库**
# 
# - 提供了生成二维码的系列功能
# - 基本二维码、艺术二维码和动态二维码
# 
# [**https://github.com/sylnsfar/qrcode**](https://github.com/sylnsfar/qrcode)
# 
# ## 4.6从人机交互到艺术设计
# 
# ### 一、Python库之图形用户界面
# 
# **PyQt5：Qt开发框架的Python接口**
# 
# - 提供了创建Qt5程序的Python API接口
# - Qt是非常成熟的跨平台桌面应用开发系统，完备GUI
# - 推荐的Python GUI开发第三方库
# 
# [**https://www.riverbankcomputing.com/software/pyqt**](https://www.riverbankcomputing.com/software/pyqt)
# 
# **wxPython：跨平台GUI开发框架**
# 
# - 提供了专用于Python的跨平台GUI开发框架
# - 理解数据类型与索引的关系，操作索引即操作数据
# - Python最主要的数据分析功能库，基于Numpy开发
# 
# [**https://www.wxpython.org**](https://www.wxpython.org)
# 
# **PyGObject：使用GTK+开发GUI的功能库**
# 
# - 提供了整合GTK+、WebKitGTK+等库的功能
# - GTK+：跨平台的一种用户图形界面GUI框架
# - 实例：Anaconda采用该库构建GUI
# 
# [**https://pygobject.readthedocs.io**](https://pygobject.readthedocs.io)
# 
# ### 二、Python库之游戏开发
# 
# **PyGame：简单的游戏开发功能库**
# 
# - 提供了基于SDL的简单游戏开发功能及实现引擎
# - 理解游戏对外部输入的响应机制及角色构建和交互机制
# - Python游戏入门最主要的第三方库
# 
# [**http://www.pygame.org**](http://www.pygame.org)
# 
# **Panda3D：开源、跨平台的3D渲染和游戏开发库**
# 
# - 一个3D游戏引擎，提供Python和C++两种接口
# - 支持很多先进特性：法线贴图、光泽贴图、卡通渲染等
# - 由迪士尼和卡尼吉梅隆大学共同开发
# 
# [**http://www.panda3d.org**](http://www.panda3d.org)
# 
# **cocos2d：构建2D游戏和图形界面交互式应用的框架**
# 
# - 提供了基于OpenGL的游戏开发图形渲染功能
# - 支持GPU加速，采用树形结构分层管理游戏对象类型
# - 适用于2D专业级游戏开发
# 
# [**http://python.cocos2d.org/**](http://python.cocos2d.org/)
# 
# ### 三、Python库之虚拟现实
# 
# **VR Zero：在树莓派上开发VR应用的Python库**
# 
# - 提供了大量与VR开发相关的功能
# - 针对树莓派的VR开发库，支持设备小型化，配置简单化
# - 非常适合初学者实践VR开发及应用
# 
# [**https://github.com/WayneKeenan/python-vrzero**](https://github.com/WayneKeenan/python-vrzero)
# 
# **pyovr：Oculus Rift的Python开发接口**
# 
# - 针对Oculus VR设备的Python开发库
# - 基于成熟的VR设备，提供全套文档，工业级应用设备
# - Python+虚拟现实领域探索的一种思路
# 
# [**https://github.com/cmbruns/pyovr**](https://github.com/cmbruns/pyovr)
# 
# **Viazrd：基于Python的通用VR开发引擎**
# 
# - 专业的企业级虚拟现实开发引擎
# - 提供详细的官方文档
# - 支持多种主流的VR硬件设备，具有一定的通用性
# 
# [**http://www.worldviz.com/vizard-virtual-reality-software**](http://www.worldviz.com/vizard-virtual-reality-software)
# 
# ### 四、Python库之图形艺术
# 
# **Quads：迭代的艺术**
# 
# - 对图片进行四分迭代，形成像素风
# - 可以生成动图或静图图像
# - 简单易用，具有很高的展示度
# 
# [**https://github.com/fogleman/Quads**](https://github.com/fogleman/Quads)
# 
# **ascii_art：ASCII艺术库**
# 
# - 将普通图片转为ASCII艺术风格
# - 输出可以是纯文本或彩色文本
# - 可采用图片格式输出
# 
# [**https://github.com/jontonsoup4/ascii_art**](https://github.com/jontonsoup4/ascii_art)
# 
# **turtle：海龟绘图体系**
# [**https://docs.python.org/3/library/turtle.html**](

# In[ ]:




