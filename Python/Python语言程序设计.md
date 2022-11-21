# 第1章 Python基本语法元素
## 1.1 程序设计基本方法
### 一、计算机与程序设计
#### 计算机的概念
计算机是根据指令操作数据的设备

- 功能性
- 可编程性
#### 计算机的发展
计算机的发展参照摩尔定律，表现为指数方式
#### 程序设计
程序设计是计算机可编程性的体现
#### 程序设计语言
程序设计语言是一种用于交互（交流）的人造语言
编程语言种类很多，但生命力强劲的却不多

- C语言诞生于1972年，它是第一个被广泛使用的编程语言
- Python语言诞生于1990年，它是最流行最好用的编程语言
### 二、编译和解释
#### 编程语言的执行方式
计算机执行源程序的两种方式：编译和解释

- 源代码：采用某种编程语言编写的计算机程序，人类可读
- 目标代码：计算机可直接执行，人类不可读
#### 编译
将源代码一次性转换成目标代码的过程，执行编译过程的程序叫作编译器
#### 解释
将源代码逐条转换成目标代码同时逐条运行的过程，执行解释过程的程序叫作解释器
#### 编译和解释
编译：一次性翻译，之后不再需要源代码
解释：每次程序运行时随翻译随执行
#### 静态语言和脚本语言
根据执行方式不同，编程语言分为两类

- 静态语言：使用编译执行的编程语言 
   - C/C++语言、Java语言
   - 编译器一次性生成目标代码，优化更充分，程序运行速度更快
- 脚本语言：使用解释执行的编程语言 
   - Python语言，JavaScript语言、PHP语言
   - 执行程序时需要源代码，维护更灵活，源代码在维护灵活、跨多个操作系统平台
### 三、程序的基本编写方法
#### IPO
程序的基本编写方法：
I：Input 输入，程序的输入
P：Process 处理，程序的主要逻辑
O：Output 输出，程序的输出
**输入**
程序的输入：文件输入、网络输入、控制台输入、交互界面输入、内部参数输入等
**输出**
程序的输出：控制台输出、图形输出、文件输出、网络输出、操作系统内部变量输出等
**处理**
处理是程序对输入数据进行计算产生输出结果的过程
处理方法统称为算法，它是程序最重要的部分
算法是一个程序的灵魂
#### 问题的计算部分
一个待解决问题中，可以用程序辅助完成的部分
#### 程序解决问题的步骤

1. 分析问题：分析问题的计算部分，**想清楚**
2. 划分边界：划分问题的功能边界，**规划IPO**
3. 设计算法：设计问题的求解算法，**关注算法**
4. 编写程序：编写问题的计算程序，**编程序**
5. 调试测试：调试程序使正确使用，**运行调试**
6. 升级维护：适应问题的升级维护，**更新完善**
### 四、计算机编程

## 1.2 Python开发环境配置
### 一、Python语言概述
### 二、Python基本开发环境IDLE
### 三、Python程序编写与运行

- 交互式：对每个输入语句即时运行结果，适合语法练习
- 文件式：批量执行一组语句并运行结果，编程的主要方式
### 四、Python高级开发环境VSCode

## 1.3 实例1：温度转换
### 一、问题分析
分析问题：直接将温度值进行转换
划分边界：输入：温度；处理：选择算法；输出：转换后温度
设计算法
### 二、代码实例
```python
#TempConvert.py
TempStr = input("请输入带有符号的温度值")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
```
### 三、举一反三

- Python语法元素理解
- 输入输出格式的改变
- 计算问题的扩展

## 1.4 Python程序语法分析
### 一、程序的格式框架
#### 缩进
**一行代码开始前的空白区域，表示程序的格式框架**

- 严格明确：缩进是语法的一部分
- 所属关系：表达代码间包含和层次关系的唯一手段
- 长度一致：程序内一致即可，一般用4个空格或1个TAB
#### 注释
用于提高代码可读性的辅助性文字，不被执行
**单行注释：以#开头，其后内容为注释**
```python
# 单行注释
```
**多行注释：以```开头或者结尾**
```python
''' 多行注释第一行
    多行注释第二行 '''
```
### 二、命名与保留字
#### 变量
**程序中用于保存和表示数据的占位符号**

- 变量采用标识符（名字）来表示，关联标识符的过程叫**命名**

	_TempStr是变量名字_

- 可以用等号（=）向变量赋值或修改值，=被称为赋值符号

	_TempStr = "82F”#向变量TempStr赋值 "82f"_

- 使用变量之前要先声明
#### 命名
**关联标识符的过程**

- 命名规则：大小写字母、数字、下划线和中文等字符及组合
- 注意事项：大小写敏感、首字符不能是数字、不与保留字相同
#### 保留字
**被编程语言内部定义并保留使用的标识符**

- Python语言有35个保留字
- 保留字是编程语言的基本单词，大小写敏感
| and | elif | import | raise | global |
| --- | --- | --- | --- | --- |
| as | else | in | return | nonlocal |
| assert | except | is | try | True |
| break | finally | lambda | while | False |
| class | for | not | with | None |
| continue | from | or | yield | async |
| def | if | pass | del | await |

### 三、数据类型
**数据类型**：字符串、整数、浮点数、列表
例如：10，011，101
	整数类型：10011101
	字符串类型："10,011,101"
	列表类型：[10,011,101]
#### 字符串

1. **由0个或多个字符组成的有序字符序列**
- 字符串由一对单引号或一对双引号表示
- 字符串是字符的有序序列，可以对其中的字符进行索引
2. **字符串的序号**
- **正向递增序号和反向递减序号**
3. **字符串的使用**
- **使用[ ]获取字符串中的一个或多个字符**
4. **索引**：返回字符串中单个字符	<字符串>[M]
```python
"请输入带有符号的温度值："[0]
TempStr[-1]
```

5. **切片**：返回字符串中一段字符子串	<字符串>[M:N]

从M开始但是不到N
```python
"请输入带有符号的温度值"[1:3]
TempStr[0:-1]
```
#### 数字类型
**整数和浮点数都是数字类型**
**整数**：数学中的整数
**浮点数**：数学中的实数，带有小数部分
#### 列表类型
**由0个或多个数据组成的有序序列**
列表使用[ ]表示，采用逗号分隔各元素
	['F', 'f']表示两个元素 'F' 和 'f'
使用保留字in判断一个元素是否在列表中
	TempStr[-1] in ['C', 'c'] 判断前者是否与列表中某个元素相同
### 四、语句与函数
#### 赋值语句
**由赋值符号构成的一行代码**

- 赋值语句用来给变量赋予新的数据值
- 赋值语句右侧的数据类型同时作用于变量
#### 分支语句
**由判断条件决定程序运行方向的语句**

- 使用保留字 if elif else 构成条件判断的分支结构
- 每个保留字所在行的最后存在一个冒号，是语法的一部分，表示后续语句与条件的所属关系
#### 函数
**根据输入参数产生不同输出的功能过程**
函数采用 <函数名>(<参数>)方式使用

### 五、Python 程序的输入输出
#### 输入函数input()
使用格式：
```python
<变量> = input(<提示信息字符串>)
```

用户输入的信息以字符串类型保存在<变量>中
#### 输出函数print()
使用格式：
```python
print(<拟输出字符串或字符串变量>)
```
字符串类型的一堆引号仅在程序内部使用，输出无引号
格式化：
```python
print("转换后的温度是{:.2f}C".format(C))

#{ }表示槽。后续变量填充到槽中
#{:.2f}表示将变量C填充到这个位置时取小数点后2位
```
end=""表示输出以什么结尾
```python
print(n,end=",")
```
#### 评估函数eval()
使用格式：
```python
eval(<字符串或字符串变量>)
```
去掉参数最外侧引号并执行余下语句的函数

# 第2章 Python基本图形绘制
## 2.1 深入理解Python语言
### 一、计算机技术的演进
计算机系统结构时代（1946-1981）
网络和视窗时代（1981-2008）
复杂信息系统时代（2008-2016）
人工智能时代
### 二、编程语言的多样初心
### 三、Python语言的特点
### 四、“超级语言”的诞生
**编程语言的种类**

1. 机器语言
2. 汇编语言
3. 高级语言
4. 超级语言
## 2.2 实例2：Python蟒蛇绘制
```python
#PythonDraw.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
```
## 2.3 模块1：turtle库的使用
### 一、turtle库基本介绍
turtle库是turtle绘图体系的Python体现
Python计算生态 = 标准库+第三方库

- 标准库：随解释器直接安装到操作系统中的功能模块
- 第三方库：需要经过安装才能使用的功能模块
- 库Library、包Package、模块Module，统称模块
### 二、turtle绘图窗体布局
```python
turtle.setup(width,height,startx,starty)	#设置窗体大小
```

- setup()设置窗体大小及位置
- 4个参数中后两个可选
- setup()不是必须的
### 三、turtle空间坐标体系
绝对坐标
以画布中央为（0，0）
```python
turtle.goto(x,y)  #前往坐标(x,y)
turtle.bk(d)      #后退d距离
turtle.fd(d)      #前进d距离
turtle.circle(r,angle) #以r为半径转angle角度
```
#### turtle角度坐标体系
绝对角度

- 以turtle的朝向为0/360度
```python
turtle.seth(angle)
```

- seth()改变海龟的行进方向
- angle为绝对度数
- seth()只改变方向但不行进
- 范围从（-360° ~ 360°）
```python
turtle.left(angle)
turtle.right(angle)
```
### 四、RGB色彩体系
RGB色彩模式
**由三种颜色构成的万物色**

- RGB指红蓝绿三个通道的颜色组合
- 覆盖视力所能感知的所有颜色
- RGB每色取值范围0-255整数或0-1小数
| 英文名称 | RGB整数值 | RGB小数值 | 中文名称 |
| --- | --- | --- | --- |
| white | 255,255,255 | 1,1,1 | 白色 |
| yellow | 255,255,0 | 1,1,0 | 黄色 |
| magenta | 255,0,255 | 1,0,1 | 洋红 |
| cyan | 0,255,255 | 0,1,1 | 青色 |
| blue | 0,0,255 | 0,0,1 | 蓝色 |
| black | 0,0,0 | 0,0,0 | 黑色 |
| seashell | 255,245,238 | 1,0.96,0.93 | 海贝色 |
| gold | 255,215,0 | 1,0.84,0 | 金色 |
| pink | 255,192,203 | 1,0.75,0.80 | 粉红色 |
| brown | 165,42,42 | 0.65,0.16,0.16 | 棕色 |
| purple | 160,32,240 | 0.63,0.13,0.94 | 紫色 |
| tomato | 255,99,71 | 1,0.39,0.28 | 番茄色 |

默认采用小数值，可切换为整数值
```python
turtle.color(mode)
```
1.0：RGB小数值模式
255：RGB整数值模式
## 2.4 turtle程序语法元素分析
### 一、库引用与import
扩充Python程序功能的方法：
#### 1.完整库引用
使用**import**保留字完成，采用.**()编码风格**
```python
import <库名>
<库名>.<函数名>(<函数参数>)

import turtle
turtle.pencolor(red)
```
#### 2.简略库引用
使用**from**和**import**保留字共同完成
```python
from <库名> import <库名>
from <库名> import *
<函数名>(<函数参数>)
```
```python
from turtle import *
setup(650,350)
penup
# 这种方法可能出现函数重名的问题
```
### 3.关联库别名
使用**import**和**as**保留字共同完成
```python
import <库名> as <库别名>
<库别名>.<函数名>(<函数参数>)
```

```python
import turtle as t
t.setup(650,350)
t.penup

```
## 二、turtle画笔控制函数
```python
turtle.penup()	别名	turtle.pu()	#抬起画笔
turtle.pendown()	别名	turtle.pd()	#落下画笔
turtle.pensize(width)	别名	turtle.width(width)	#画笔宽度
turtle.pencolor(color)	#画笔颜色，color为颜色字符串或RGB值
```
颜色color可以有三种形式：
```python
turtle.pencolor("purple")
turtle.pencoloe(0.63, 0.13, 0.94)
turtle.pencolor((0.63, 0.13, 0.94))
```
## 三、turtle运动控制函数
```python
turtle.forward(d)	别名	turtle.fd(d)	#向前行进，d为行进距离，可以为负数
turtle.circle(r, extent=None)	#根据半径r绘制extent角度的弧形
```
circle函数参数：
r：默认圆心在海龟左侧r距离的位置
extent：绘制角度，默认是360度整圆
## 四、turtle方向控制函数
```python
turtle.setheading(angle)	别名	turtle.seth(angle)	#改变行进方向，angle为行进方向绝对角度
turtle.left(angle)	#海龟向左转
turtle.right(angle)	#海龟向右转
```
## 五、循环语句与range()函数
### 循环语句
按照一定次数循环执行一组语句：
```python
for <变量> in range(<次数>):
    <被循环语句>
```
变量表示每次循环的计数，0到<次数> - 1
### range()函数
产生循环计数序列
```python
range(N) #产生0到N-1的整数序列，共N个
```
```python
range(M,N) #产生M到N-1的整数序列，共N-M个
```

# 第3章 基本数据类型
## 3.1 数字类型及操作
### 一、整数类型

- 可正可负，没有取值范围限制
- pow(x,y)函数：计算xy

**四种进制表示形式**

- 十进制：1010，99，-217
- 二进制：**以0b或0B开头**：0b010
- 八进制：**以0o或0O开头**：0o123
- 十六进制：**以0x或0X开头**：0x9a
### 二、浮点数类型

- 带有小数点及小数的数字
- 浮点数取值范围和小数精度都存在限制，但常规计算可以忽略
- 取值范围数量级越-10307至10308，精度数量级10-16

浮点数间运算存在不确定尾数

- round(x,d)：对x四舍五入，d是小数截取位数
- 浮点数间运算与比较用round()函数辅助
- 不确定位数一般发生在10-16左右，round()十分有效

浮点数可以采用科学计数法表示
使用字母e或E作为幂的符号，以10为基数：
e**	表示a*10b**
### 三、复数类型
实例：
z = 1.23e-4+5.6e+89**j**
实部：z.real
虚部：z.imag
### 四、数值运算操作符
#### 操作符符号
操作符符号体系：

| 操作符及使用 | 描述 |
| --- | --- |
| x + y | 加，x与y之和 |
| x - y | 减，x与y之差 |
| x * y | 乘，x与y之积 |
| x / y | 除，x与y之商 |
| x  y | 整数除，x与y之整数商 |
| + x | x本身 |
| - y | x的负值 |
| x % y | 余数，模运算· |
| x  y | 幂运算，或者开方 |

二元操作符有对应的增强赋值操作符
x op = y
等价于：x = x op y
#### 数字类型的关系
类型间可进行混合运算，生成结果为“最宽”类型
整数 -> 浮点数 -> 复数
### 五、数值运算函数
| 函数及使用 | 描述 |
| --- | --- |
| abs(x) | 绝对值，x的绝对值 |
| divmod(x,y) | 商余，（xy, x%y)，同时输出商和余数 |
| pow(x,y[,z]) | 幂余，(xy)%z，[..]表示参数z可省略 |
| round(x[,d]) | 四舍五入，d是保留小数位数，默认值为0 |
| max(x1, x2, ..., xn) | 最大值 |
| min(x1, x2, ..., xn) | 最小值 |
| int(x) | 将x变为整数，舍弃小数部分 |
| float(x) | 将x变为浮点数，增加小数部分 |
| complex(x) | 将x变为复数，增加虚数部分 |

## 3.2 实例3：天天向上的力量
问题一：1‰的力量
```python
#DayDayUpQ1.py
dayup = pow(1.001,365)
daydown = pow(0.999,365)
printf("向上：{:.2f}，向下：{:.2f}".format(dayup,daydown))
```
问题二：5‰和1%的力量
```python
#DayDayUpQ2.py
dayfactor = 0.005	#使用变量的好处：一处修改即可
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup,daydown))
```
问题三：工作日的力量
```python
#DayDayUpQ3.py
dayup = 1.0
dayfactor = 0.01
for i in range(356):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
		else:
        dayup = dayup*(1+dayfactor)
print("工作日的力量：{:.2f}".format(dayup))
```
问题四：工作日的努力
```python
#DayDayUpQ4.py
def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))
```
## 3.3 字符串类型及操作
### 一、字符串类型的表示
#### 字符串
由0个或多个字符组成的有序字符序列

- 字符串由一对单引号或一对双引号表示
- 字符串是字符的有序序列，可以对其中的字符进行索引

字符串的表示方式：

- 由一对单引号或者双引号表示，仅表示单行字符串
- 由一对三单引号或三双引号表示，可表示多行字符串
- 如果希望在字符串中包含双引号或单引号则表示字符串时用另外一种引号表示方法
#### 字符串的序号
正向递增序号 和 反向递减序号
#### 字符串的使用
使用[ ]获取字符串中的一个或多个字符
**索引**：返回字符串中单个字符	<字符串>[M]
```python
"请输入带有符号的温度值："[0]
TempStr[-1]
```
**切片**：返回字符串中一段字符子串	<字符串>[M:N]
从M开始但是不到N
```python
"请输入带有符号的温度值"[1:3]
TempStr[0:-1]
```
**高级切片**：使用[M: N: K]根据步长对字符串切片
<字符串>[M: N]，M缺失表示至开头，N缺失表示至结尾
<字符串>[M: N: K]，根据步长K对字符串切片
##### 转义符
转义符 \ 表达特定字符的本意
转义符形成一些组合，表达一些不可打印的含义
\b 回退
\n 换行
\r 回车（光标移动到本行首）
### 二、字符串操作符
| 操作符及使用 | 描述 |
| --- | --- |
| x + y | 连接两个字符串x和y |
| n _ x 或 x _ n | 复制n次字符串x |
| x in s | 如果x是s的子串，返回True，否则返回False |

```python
#WeekNamePrintV1.py
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字（1-7）："))
pos = (weekId - 1) * 3
print(weekStr[pos:pos+3])
```
```python
＃WeekNamePrintV2.py
weekStr = "一二三四五六日"
weekId = eval(input("请输入星期数字（1-7）："))
print("星期"+weekStr[weekId-1])
```
### 三、字符串处理函数
#### 字符串处理功能
| 函数及使用 | 描述 |
| --- | --- |
| len(x) | 长度，返回字符串x的长度 |
| str(x) | 任意类型x所对应的字符串形式 |
| hex(x) 或 oct(x) | 整数x的十六进制或八进制小写形式字符串 |
| chr(u) | x为Unicode编码，返回其对应的字符 |
| ord(x) | x为字符，返回其对应的Unicode编码 |

#### Unicode编码

- 统一字符编码，覆盖几乎所有字符的编码方式
- 从0到1114111（0x10FFFF）空间，每个编码对应一个字符
- Python字符串中每个字符都是Unicode编码字符
### 四、字符串处理方法
”方法“在编程中是一个专有名词

- ”方法“特指.**()风格中的函数()**
- 方法本身也是函数，但与有关
- 字符串或字符串变量是，存在一些可用的方法
| 方法及使用 | 描述 |
| --- | --- |
| str.lower 或 str.upper() | 返回字符串的副本，全部字符小写/大写 |
| str.split(sep=None) | 返回一个列表，由str根据sep被分隔的部分组成，**符号要用双引号** |
| str.count(sub) | 返回子串sub在str中出现的次数 |
| str.replace(old,new) | 返回字符串str副本，所有old子串被替换为new |
| str.center(width[,fillchar]) | 字符串str根据宽度width居中，fillchar可选 |
| str.strip(chars) | 从str中去掉在其左侧和右侧chars中列出的字符 |
| str.join(iter) | 在iter变量除最后元素外每个元素后增加一个str |

### 五、字符串类型的格式化
#### 字符串类型的格式化
使用.format()方法
`<模板字符串>.format(<逗号分隔的参数>)`
默认顺序：
自定顺序：
槽内部对格式化的配置方法
## 3.4 模块2：time库的使用
### 一、time库基本介绍
time库是Python中处理时间的标准库

- 计算机时间的表达
- 提供获取系统时间并格式化输出功能
- 提供系统级精确计时功能
```python
import time
time.<b>()
```
### 二、时间获取
| 函数 | 描述 |
| --- | --- |
| time() | 获取当前时间戳，即计算机内部时间值，浮点数 |
| ctime() | 获取当前时间并以易读方式返回，返回字符串 |
| gmtime() | 获取当前时间，表示为计算机可处理的时间格式 |

### 三、时间格式化
| 函数 | 描述 |
| --- | --- |
| strftime(tpl,ts) | tpl是模式化模板字符串，用来定义输出效果；ts是计算机内部时间类型变量 |

#### 格式化控制符
| 格式化字符串 | 日期/时间说明 | 值范围和实例 |
| --- | --- | --- |
| %Y | 年份 | 0000~9999 |
| %m | 月份 | 01~12 |
| %B | 月份名称 | January~December |
| %b | 月份名称缩写 | Jan~Dec |
| %d | 日期 | 01~31 |
| %A | 星期 | Monday~Sunday |
| %a | 星期缩写 | Mon~Sun |
| %H | 小时（24h） | 00~23 |
| %I | 小时（12h） | 01~12 |
| %p | 上/下午 | AM, PM |
| %M | 分钟 | 00~59 |
| %S | 秒 | 00~59 |

```python
t = time.gmtime()
time.strftime("%Y-%m-%d %H:%M:%S",t)

timeStr = "2018-01-26 12:55:20"
time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
```
| 函数 | 描述 |
| --- | --- |
| strptime(str,tpl) | str是字符串形式的时间值；tpl是格式化模板字符串，用来定义输入效果 |

### 四、程序计时应用
测量起止动作所经历的时间过程

| 函数 | 描述 |
| --- | --- |
| perf_counter() | 返回一个CPU级别的精确时间计数值，单位为秒 |

由于这个计数值起点不确定，连续调用差值才有意义
```python
start = time.perf_counter()
end = time.perf_counter()
end - start
```
| 函数 | 描述 |
| --- | --- |
| sleep() | s拟休眠时间，单位是秒，可以是浮点数 |

```python
def wait():
    time.sleep(3.3)
wait()	#程序将等待3.3秒之后再退出
```
## 3.5 实例4：文本进度条
### 一、问题分析
文本进度条：
采用字符串方式打印可以动态变化的文本进度条
进度条需要能在一行中逐渐变化
如何变化时间：
采用sleep()模拟一个持续的进度
### 二、代码分析
#### 简单的开始
```python
#TextProBarV1.py
import time 
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")
```
#### 单行动态刷新
刷新的关键是\r
* 刷新的本质是：用之后打印的字符覆盖之前的字符
* 不能换行：print()需要被控制
* 要能回退：打印后光标退回到之前的位置\r
```python
#TextProBarV2.py
import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)
```

#### 完整效果

```python
#TextProBarV3
import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = "." * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))
```
# 第4章 程序的控制结构
## 4.1 程序的分支结构
### 一、单分支结构
根据判断条件结果而选择不同向前路径的运行方式
```python
if <条件>:
    <语句块>
```## 二、二分支结构
```python
if <条件>:
    <语句块1>
else:
    <语句块2>
```
紧凑形式：适用于简单表达式的二分支结构
```python
<表达式1> if <条件> else <表达式2>
```
```python
guess = eval(input())
print("猜{}了".format("对" if guess==99 else "错"))
```
### 三、多分支结构
```python
if <条件1>:
    <语句块1>
elif <条件2>:
    <语句块2>
    ......
else:
    <语句块N>
```
### 四、条件判断及组合
| 操作符 | 描述 |
| --- | --- |
| < | 小于 |
| <= | 小于等于 |
| >= | 大于等于 |
| > | 大于 |
| == | 等于 |
| != | 不等于 |

| 操作符及使用 | 描述 |
| --- | --- |
| x and y | 两个条件x和y的逻辑**与** |
| x or y | 两个条件x和y的逻辑**或** |
| not x | 条件x的逻辑**非** |

```python
guess = eval(input())
if guess > 99 or guess < 99:
    print("猜错了")
else:
    print("猜对了")
    
if not True:
    print("语句块2")
else:
    print("语句块1")
```
### 五、程序的异常处理
```python
try:
    <语句块1>
except:
    <语句块2>
```
```python
try:
    <语句块1>
except <异常处理>:
    <语句块2>		#标注异常类型后，仅响应此类异常，异常类型名字等同于变量名
```
```python
try:
    <语句块1>		＃异常处理的高级用法
except:
    <语句块2>
else:
    <语句块3>		＃else对应句块3在不发生异常时执行
finally:
    <语句块4>		＃finally对应语句块4一定执行
```
## 4.2 实例5：身体质量指数BMI
### 一、问题分析
**问题需求：**
输入：给定体重和身高值
输出：BMI指标分类信息
### 二、代码实例
**思路方法**
思路1：分别计算并给出国际和国内BMI分类
思路2：混合计算并给出国际和国内BMI分类
```python
#CalBMIv1.py
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
```
```python
＃CalBMIv2.py
height, weight = eval(input("请输入身高(米)和体重\(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
nat = ""
if bmi < 18.5:
    nat = "偏瘦"
elif 18.5 <= bmi < 24:
    nat = "正常"
elif 24 <= bmi < 28:
    nat = "偏胖"
else:
    nat = "肥胖"
print("BMI 指标为:国内'{0}'".format(nat))
```
```python
#CalBMIv3.py
height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI 指标为:国际'{0}', 国内'{1}'".format(who, nat))
```
## 三、举一反三
关注多分支条件的组合
## 4.3 程序的循环结构
### 一、遍历循环

1. **遍历某个结构形成的循环运行方式**
```python
for <循环变量> in <遍历结构>:
    <语句块>
```
由保留字for 和 in 组成，完整遍历所有元素后结束
每次循环，所获得元素放入循环变量，并执行一次语句块

2. **计数循环**
```python
for i in range(N):
    <语句块>
```
遍历由range()函数产生的数字序列，产生循环：从0到N-1
```python
for i in range(M,N,K):
    <语句块>
```
遍历由range()函数产生的数字序列，产生循环：从M到N-1以K为步长

3. **字符串遍历循环**
```python
for c in s:
    <语句块>
```
s是字符串，遍历字符串每个字符，产生循环
例如：
```python
for i in "Python123":
    print(c, end=",")
```
输出：P,y,t,h,o,n,1,2,3,

4. **列表遍历循环**
```python
for item in ls:
    <语句块>
```
ls是一个列表，遍历其每个元素，产生循环

5. **文件遍历循环**
```python
for line in fi:
    <语句块>
```
fi是一个文件标识符，遍历其每行，产生循环
### 二、无限循环
**由条件控制的循环运行方式**
```python
while <条件>:
    <语句块>
```
### 三、循环控制保留字
**break 和 continue**
break 跳出并结束当前整个循环，执行循环后的语句。break仅跳出当前最内层循环
continue结束当次循环，继续执行后续次数循环
break 和 continue 可以与for 和while 循环搭配使用
```python
for c in "PYTHON":
    if c=="T":
        continue
    print(c,end="")		#输出：PYHON
```
```python
for c in "PYTHON":
    if c=="T":
        continue
    print(c,end="")		＃输出：PY
```
### 四、循环的高级用法
**循环与else**
```python
for <变量> in <遍历结构>:
    <语句块1>
else:
    <语句块2>
```
```python
while <条件>:
    <语句块>
else:
    <语句块2>
```
当循环没有被break语句退出时，执行else语句块
else语句块作为”正常“完成循环的奖励
这里else的用法与异常处理中else用法相似
## 4.4 模块3：random库的使用
### 一、random库基本介绍
random库时使用随机数的Python标准库
伪随机数：采用梅森旋转算法生成的伪随机序列中元素
random库主要用于生成随机数
### 二、基本随机函数
| 函数 | 描述 |
| --- | --- |
| seed(a=None) | 初始化给定的随机数种子，默认为当前系统时间 |
| random() | 生成一个[0.0,1.0) 之间的随机小数 |

### 三、扩展随机数函数
| 函数 | 描述 |
| --- | --- |
| randint(a,b) | 生成一个[a,b]之间的整数 |
| randrange(m, n[,k]) | 生成一个[m,n) 之间以k为步长的随机整数 |
| getrandbits(k) | 生成一个k比特长的随机整数 |
| uniform(a,b) | 生成一个[a,b]之间的随机小数 |
| choice(seq) | 从序列seq中随机选择一个元素 |
| shuffle(seq) | 将序列seq中元素随机排列，返回打乱后的顺序 |

## 4.5 实例6：圆周率的计算
### 一、问题分析
圆周率的近似计算公式
蒙特卡罗方法
### 二、代码示例
**近似计算公式**
```python
#CalPiV1.py
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("圆周率值时：{}".format(pi))
```
**蒙特卡罗方法**
```python
#CalPiV2.py
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
print("圆周率的值时：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start)
```
### 三、举一反三
数学思维：找到公式，利用公式求解
计算思维：抽象一种过程，用计算机自动化求解
程序运行时间分析：
使用time库的计时方法获得程序运行时间
改变撒点数量，理解程序运行时间的分布
# 第5章 函数和代码复用
## 5.1 函数的定义与使用
### 一、函数的理解和定义
函数是一段代码表示
```python
def <函数名>(<参数（0个或多个>):
    <函数体>
    return <返回值>
```
函数定义时，所指定的参数是一种**占位符**
函数定义后，如果不经过调用，不会被执行
函数定义时，参数是输入、函数体是处理、结果是输出（IPO）
### 二、函数的使用及调用过程
调用是运行函数代码的方式

- 调用时要给出实际参数
- 实际参数替换定义中的参数
- 函数调用后得到返回值
### 三、函数的参数传递
**参数个数**
函数可以有参数，也可以没有，但是必须保留括号
```python
def <函数名>():
    <函数体>
    return <返回值>
```
**可选参数传递**
函数定义时可以为某些参数指定默认值，构成可选参
```python
def <函数名>(<非可选参数>,<可选参数>):
    <函数体>
    renturn <返回值>
```
例如：
```python
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m
```
> fact(10)	输出：3628800fact(10,5)	输出：725760### 可变参数传递
函数定义时可以设计可变数量参数，既不确定参数总数量

```python
def <函数名>(<参数>,*b):
    <函数体>
    return <函数值>
```
**参数传递的两种方式**
函数调用时，参数可以按照位置或名称方式传递
```python
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m
```
> fact(10,5)	位置传递fact(m=5, n=10)	名称传递## 四、函数的返回值
函数可以返回0个或多个结果

- return保留字用来传递返回值
- 函数可以有返回值，也可以没有，可以有return，也可以没有
- return可以传递0个返回值，也可以传递任意多个返回值

函数调用时，参数可以按照位置或名称方式传递
```python
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m,n,m
```
> fact(10,5)	输出：(725760,10,5)	元组类型> a, b, c = fact(10,5)print(a,b,c)	输出：725760 10 5

### 五、局部变量和全局变量
**规则一：局部变量和全局变量是不同变量**
局部变量是函数内部的占位符，与全局变量可能重名但不同
函数运算结束后，局部变量被释放
可以使用**global**保留字在函数内部使用全局变量
**规则二：局部变量为组合数据类型为组合数据类型，等同于全局变量**
```python
ls = ["F","f"]			#通过使用[]真实创建了一个全局变量列表ls
def func(a):
    ls.append(a)		#此处ls是列表类型，未真实创建，则等同于全局变量
    return
func("c")				#全局变量ls被修改
print(ls)				#输出：['F','f','c']
```
```python
ls = ["F","f"]			＃通过使用[]真实创建了一个全局变量列表ls
def func(a):
    ls = []
    ls.append(a)		＃此处ls是列表类型，真实创建，ls是局部变量
    return
func("c")				＃局部变量ls被修改
print(ls)				＃输出：['F','f']
```
**使用规则**

- 基本数据类型，无论是否重名，局部变量与全局变量不同
- 可以通过global保留字在函数内部声明全局变量
- 组合数据类型，如果局部变量未真实创建，则是全局变量
### 六、lambda函数
**lambda函数返回函数名作为结果**

- lambda函数是一种匿名函数，即没有名字的函数
- 使用**lambda**保留字定义，函数名是返回结果
- lambda函数用于定义简单的、能够在一行内表示的函数
```python
<函数名> = lambda <参数>:<表达式>
```
等价于
```python
def <函数名>(<参数>):
    <函数体>
    return <返回值>
```
例如：
```python
f = lambda x,y:x+y
```
> f(10,15)	输出：25

## 5.2 实例7：7段数码管的绘制
### 基本思路

1. 步骤1：绘制单个数字对应的数码管
2. 步骤2：获得一串数字，绘制对应的数码管
3. 步骤3：获得当前系统时间，绘制对应的数码管
### 程序代码

1. **绘制单个数字对应的数码管**
```python
import turtle
def drawLine(draw):   #绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(digit): #根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup() #为绘制后续数字确定位置
    turtle.fd(20) #为绘制后续数字确定位置
```

2. **获得一串数字，绘制对应的数码管**
```python
def drawData(data): #获得要输出的数字
    for i in date:
        drawDigit(eval(1)) #通过eval()函数将数字变为整数
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20181010')
    turtle.hideturtle()
    turtle.down
main()
```

3. **获得当前系统时间，绘制对应的数码管**
- 绘制数码管间隔
```python
import turtle
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
```

- 获取系统时间
```python
def drawDate(date): #date为日期，格式为'%Y-%m=%d+'
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == "+":
            turtle.write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
```
```python
import time
drawDate(time.strftime('%Y-%m=%d+',time.gmtime())) ＃获取系统时间
```
### 举一反三
**理解方法思维**

- 模块化思维：确定模块接口，封装功能
- 规则化思维：抽象过程为规则，计算机自动执行
- 化繁为简：将大功能变为小功能组合，分而治之

**应用问题扩展**
绘制带小数点的七段数码管
带刷新时间倒计时效果
绘制高级数码管
## 5.3 代码复用与函数递归
### 一、代码的复用和模块化设计
**代码复用**
**把代码当成资源进行抽象**

- 代码资源化：程序代码是一种用来表达计算的“资源”
- 代码抽象化：使用函数等方法对代码赋予更高级别的定义
- 代码复用：同一份代码在需要时可以被重复使用

**函数和对象是代码复用的两种主要形式**
函数：将代码命名，在代码层面建立了初步抽象
对象：属性和方法，在函数之上再次组织进行抽象
**模块化设计**
分而治之：

- 通过函数或对象封装将程序划分为模块及模块间的表达
- 包括主程序、分程序和分程序之间的关系
- 分而治之

**紧耦合 松耦合**

- 紧耦合：两个部分之间交流很多，无法独立存在
- 松耦合：两个部分之间交流较少，可以独立存在
- 模块内部紧耦合、模块之间松耦合
### 二、函数递归的理解
**函数定义中调用函数自身的方法**
两个换件特征：

1. 链条：计算过程存在递归链条
2. 基例：存在一个或多个不需要再次递归的基例

_类似数学归纳法_
### 三、函数递归的调用过程
**函数+分支语句**
递归本身是一个函数
函数内部用分支语句对输入参数进行判断
基例和链条，分别编写对应代码
```python
def fact(5):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
```
### 四、函数递归的应用
**字符串反转**
**将字符串s反转后输出**
自带切片操作：
`s[::-1]`
利用递归：
```python
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]
```
**斐波那契数列**
斐波那契数列天生有基例和链条，n为1和2的时候为基例，n大于2的时候为链条
```python
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)
```
**汉诺塔问题**
函数+分支结构
递归链条
递归基例
```python
count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src.mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count +=1
        hanoi(n-1,mid,dst,src)
hanoi(3,"A","C","B")
print(count)
```
## 5.4 PyInstaller库的使用
### 一、基本介绍
将.py源代码转换成无需源代码的可执行文件
PyInstaller库是第三方库，通过pip指令安装：**（cmd命令行）pip install pystaller**
### 二、PyInstaller库使用说明
通过命令行转换文件：**（cmd命令行）pyinstaller -F <文件名.py>**
在“dist”文件夹中是我们需要的可执行文件
**常用参数**

| 参数 | 描述 |
| --- | --- |
| -h | 查看帮助 |
| --clean | 清理打包过程中的临时文件 |
| -D, --onedir | 默认值，生成dist文件夹 |
| -F, --onefile | 在dist文件夹中只生成独立的打包文件 |
| -i <图标文件名.ico> | 指定打包程序使用的图标文件 |

**图标使用举例：pyinstaller -i curve.ico -F SevenDigitsDrawV2.py**
## 5.5 实例8：科赫雪花小包裹
### 一、问题分析
科赫曲线
### 二、科赫曲线的绘制
```python
#KochDrawV1.py
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hindturtle
main()
```
# 第6章 组合数据类型
## 6.1 集合类型及操作
### 一、集合类型定义
集合是多个元素的无序组合，每个元素唯一，元素不可变（不能修改）
集合用大括号{}表示，元素之间用逗号分隔
建立集合类型用{}或set()
建立空集合类型，必须使用set()
`A = {"python", 123, ("python",123)}`
`B = set("pypy123")`  相同元素会被去除，元素没有顺序
### 二、集合操作符
**基本操作符**

| 操作符及应用 | 描述 |
| --- | --- |
| S | T |
| S - T | 返回一个新集合，包括在集合S但不在T中的所有元素 |
| S & T | 返回一个新集合，包括同时在集合S和T中的所有元素 |
| S ^ T | 返回一个新集合，包括在集合S和T中的非相同元素 |
| S <= T 或 S < T | 返回True/False， 判断S和T的子集关系 |
| S >= T 或 S > T | 返回True/False，判断S和T的包含关系 |

**增强操作符**

| 操作符及应用 | 描述 |
| --- | --- |
| S | = T |
| S -= T | 更新集合S，包括在集合S但不在T中的元素 |
| S &= T | 更新集合S，包括同时在集合S和T中的元素 |
| S ^= T | 更新集合S，包括集合S和T中的非相同元素 |

### 三、集合的处理方法
| 操作函数或方法 | 描述 |
| --- | --- |
| S.add(x) | 如果x不在集合S中，将x增加到S |
| S.discard(x) | 移除S中元素x，如果x不在集合S中，不报错 |
| S.remove(x) | 移除S中元素x，如果x不在集合S中，产生KeyError异常 |
| S.clear() | 移除S中所有元素 |
| S.pop() | 随机返回S中的一个元素，更新S，若S为空产生KeyError异常 |
| S.copy() | 返回集合S的一个副本 |
| len(S) | 返回集合S的元素个数 |
| x in S | 判断S中元素x，x在集合S中，返回True，否则返回False |
| x not in S | 判断S中元素x，x不在集合S中，返回True，否则返回False |
| set(x) | 将其他类型变量x转变为集合类型 |

**例子：遍历集合的方式**

1. for in 方法遍历
```python
A = {"p","y","123"}
for item in A:
    print(item,end="")
```
	输出：p123y
2. while 方法遍历
```python
try:
    while True:
        print(A.pop(),end="")
except:
    pass
```
	输出：p123y
### 四、集合类型应用场景

1. 包含关系比较
```python
"p" in {"p","y",123}
#True

{"p","y"} >= {"p","y",123}
#False
```1. 数据去重
```python
1s = ["p", "p", "y", "y", 123]
s = set(1s)   #利用了集合无重复元素的特点 {'p','y',123}
lt = list(s)   #将集合转换为列表 ['p','y',123]
```
## 6.2 序列类型及操作
### 一、序列类型定义
**序列是具有先后关系的一组元素**

- 序列是一维元素向量，元素类型可以不同
- 类似数学元素序列
- 元素间由序号引导，通过下标访问序列的特定元素

**序列类型分为：字符串类型、元组类型、列表类型**
**序号的定义：**

- 正向递增序号：从0开始递增
- 反向递减序号：从-1开始递减
### 二、序列处理函数及方法
**系列类型通用操作符**

| 操作符及应用 | 描述 |
| --- | --- |
| x in s | 如果x是序列s的元素，返回True，否则返回False |
| x not in s | 如果x是序列s的元素，返回False，否则返回True |
| s + t | 连接两个序列s和t |
| s**n 或 n**s | 将序列s复制n次 |
| s[i] | 索引，返回s中的第i个元素，i是序列的序号 |
| s[i:j]或s[i:j:k] | 切片，返回序列s中第i到j以k为步长的元素子序列 |

实例：以-1为步长
```python
ls = ["python",123,".io"]
ls[::-1]         #输出:['.io',123,'python']

s = "python123.io"
s[::-1]          #输出:'oi.321nohtyp'
```
**序列类型通用函数和方法**

| 函数和方法 | 描述 |
| --- | --- |
| len(s) | 返回序列s的长度，即元素个数 |
| min(s) | 返回序列s的最小元素，s中元素需要可比较 |
| max(s) | 返回序列s的最大元素，s中元素需要可比较 |
| s.index(x) 或 s.index(x,i,j) | 返回序列s从i开始到j位置中第一次出现元素x的位置 |
| s.count(x) | 返回序列s中出现x的总次数 |

```python
ls = ["python",123,".io"]
len(ls)   #output:3

s = "python123.io"
max(s)   #output:'y'
```
### 三、元组类型及操作
**元组类型定义**
**元组是序列类型的一种扩展**

- 元组是一种序列类型，一旦创建就不能被修改
- 使用小括号（）或tuple（）创建，元素间用逗号分隔
- 可以使用或不使用小括号
```python
creature = "cat","dog","tiger","human"
creature
coloe = (0x001100,"blue",creature)
# (4532,'blue',('cat','dog','tiger','human'))
```
**元组类型操作**
**元组继承序列类型的全部通用操作**

- 元组继承了序列类型的全部通用操作
- 元组因为创建后不能修改，因此没有特殊操作
- 使用或不使用小括号
```python
creature = "cat","dog","tiger","human"
creature[::-1]
#('human','tiger','dog','cat')
color = (0x001100,"blue",creature)
color[-1][2]
#'tiger'
```
### 四、列表类型及操作
**列表类型定义**
**列表是序列类型的一种扩展，十分常用**

- 列表是一种序列类型，创建后可以随意被修改
- 使用方括号[]或list()创建，元素之间用逗号分隔
- 列表中各元素类型可以不用，无长度限制
```python
ls = ["cat","dog","tiger",1024]
lt=ls  #方括号[]真正创建一个列表，赋值仅传递引用
```
| 函数或方法 | 描述 |
| --- | --- |
| ls[i] = x | 替换列表ls第i元素为x |
| ls[i:j:k] = lt | 用列表lt替换ls切片后所对应元素子列表 |
| del ls[i] | 删除列表ls中第i元素 |
| del ls[i:j:k] | 删除列表ls中第i到第j以k为步长的元素 |
| ls +=lt | 更新列表ls，将列表lt元素增加到列表ls中 |
| ls *= n | 更新列表ls，其元素重复n次 |

| 函数或方法 | 描述 |
| --- | --- |
| ls.append(x) | 在列表ls最后增加一个元素x |
| ls.clear() | 删除列表ls中所有元素 |
| ls.copy() | 生成一个新列表，赋值ls中所有元素 |
| ls.insert(i,x) | 在列表ls的第i位置增加元素x |
| ls.pop(i) | 将列表ls中第i位置元素取出并删除该元素 |
| ls.remove(x) | 将列表ls中出现的第一个元素x删除 |
| ls.reverse | 将列表ls中的元素反转 |

### 五、序列类型应用场景
**数据表示：元组 和 列表**

- 元组用于元素不改变的应用场景，更多用于固定搭配场景
- 列表更加灵活，它是最常用的序列类型
- 最主要作用：表示一组有序数据，进而操作他们

**元素遍历**
```python
for item in ls:
    <语句块>
for item in tp:
    <语句块>
```
**数据保护**
**_如果不希望数据被程序所改变，转换为元组类型_**
## 6.3 实例9：基本统计值计算
### 一、问题分析

- 总个数：len()
- 求和：for...in
- 平均值：求和/总个数
- 方差：各数据与平均数差的平方和的平均数
- 中位数：排序，然后奇数找中间1个，偶数找中间2个取平均
### 二、代码示例
```python
#CalStatisticsV1.py
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
 
def dev(numbers, mean): #计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)
 
def median(numbers):    #计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med
 
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{},方差:{:.2},中位数:{}.".format(m, dev(n,m),median(n)))
```
## 6.4 字典类型及操作
### 一、字典类型定义

- 理解映射：映射是一种键（索引）和值（数据） 的对应
- 字典类型是典型的“映射”的体现
键值对：键是数据索引的扩展
- 字典是键值对的集合，键值对之间无序
- 采用大括号{}和dict()创建，键值对用冒号：表示
- **{<键1> : <值1>, <键2> : <值2>,  ... , <键n> : <值n>}**
- 在字典变量中，通过键获得值
- <字典变量> = {<键1> : <值1>, <键2> : <值2>,  ... , <键n> : <值n>}
- <值> = <字典变量>[<键>]
- <字典变量>[<键>] = <值>
- **[ ]用来向字典变量中索引或增加元素**
```python
d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
d		#输出：{'中国': '北京', '美国': '华盛顿', '法国': '巴黎'}
d["中国"]		#'北京'
de = {} ; type(de)		#<class 'dict'>
```
type(x)	返回变量x的类型
### 二、字典处理函数及方法
| 函数或方法 | 描述 |
| --- | --- |
| del d[k] | 删除字典d中键k对应的数据值 |
| k in d | 判断键k是否在字典d中，如果在返回True，否则返回False |
| d.keys() | 返回字典d中所有键信息 |
| d.values() | 返回字典d中所有的值信息 |
| d.items() | 返回字典d中说有的键值对信息 |

```python
>>>d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
>>> "中国" in d 
True
>>> d.keys()
dict_keys(['中国', '美国', '法国'])
>>> d.values()
dict_values(['北京', '华盛顿', '巴黎'])
```
| 函数或方法 | 描述 |
| --- | --- |
| d.get(k,) | 键k存在，则返回相应值，不在则返回值 |
| d.pop(k,) | 键k存在，则取出相应值，不在则返回值 |
| d.popitem() | 随即从字典d中取出一个键值对，以元组形式返回 |
| d.clear() | 删除所有的键值对 |
| len(d) | 返回字典d中元素的个数 |

```python
>>> d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
>>> d.get("中国","伊斯兰堡") 
'北京'
>>> d.get("巴基斯坦","伊斯兰堡") 
'伊斯兰堡' 
>>> d.popitem()
('美国', '华盛顿')
```
### 三、字典类型应用场景
**映射的表达**
映射无处不在，例如统计数据出现的次数，数据是键，次数是值
最主要作用：表达键值对数据，进而操作它们
遍历字典：
```python
for k in d : 
    <语句块>
```
## 6.5 模块5：jieba库的使用
### 一、jieba库基本介绍
jieba库的安装：（cmd命令行） pip install jieba
jieba分词依靠中文词库：

- 利用一个中文词库，确定中文字符之间的关联概率
- 中文字符间概率大的组成词组，形成分词结果
- 除了分词，用户还可以添加自定义的词组
### 二、jieba库使用说明
### 三种模式

- 精确模式：把文本精确的切分开，不存在冗余单词
- 全模式：把文本中所有可能的词语都扫描出来，有冗余
- 搜索引擎模式：在精确模式基础上，对长词再次切分
| 函数 | 描述 |
| --- | --- |
| jieba.lcut(s) | 精确模式，返回一个列表类型的分词结果 |
| jieba.lcut(s,cut_all=True) | 全模式，返回一个列表类型的分词结果，存在冗余 |

```python
>>>jieba.lcut("中国是一个伟大的国家")
['中国', '是', '一个', '伟大', '的', '国家']

>>>jieba.lcut("中国是一个伟大的国家",cut_all=True)
['中国', '国是', '一个', '伟大', '的', '国家']
```
| 函数 | 描述 |
| --- | --- |
| jieba.lcut_for_search(s) | 搜索引擎模式，返回一个列表类型的分词结果，存在冗余 |
| jieba.add_word(w) | 向分词词典增加新词w |

```python
>>>jieba.lcut_for_search(“中华人民共和国是伟大的")
['中华', '华人', '人民', '共和', '共和国', '中华人民共
和国', '是', '伟大', '的']
 
 >>>jieba.add_word("蟒蛇语言")
```
## 6.6 实例10：文本词频统计
### 一、问题分析
### 二、代码示例
**哈姆雷特词频统计**
文本去噪及归一化
使用字典表达词频
```python
#CalHamletV1.py
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
```
**《三国演义》人物出场统计**
```python
#CalThreeKingdomsV1.py
import jieba
txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
```
改进：将词频与人物相关联，面向问题，对结果进行优化
```python
#CalThreeKingdomsV2.py
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
```
# 第7章 文件和数据格式化
## 7.1 文件的使用
### 一、文件的类型
#### 文件的理解
#### 文件是数据的抽象和集合

- 文件是储存在辅助储存器上的数据序列
- 文件是数据储存的一种形式
- 文件展现形态：文本文件和二进制文件
#### 文本文件和二进制文件

- 文本文件和二进制文件只是文件的展示方式
- 本质上，所有文件都是二进制形式储存
- 形式上，所有文件采用两种方式展示

**文本文件**
由单一特定编码组成的文件，如UTF-8编码
由于存在编码，也被看成储存着的长字符串
适用于.txt文件、.py文件
```python
#文本形式打开文件
tf = open("f.txt", "rt")
print(tf.readline())
tf.close()
>>>
中国是个伟大的国家!
```
**二进制文件**
直接由比特0和1组成，没有统一字符编码
一般存在二进制0和1的组织结构，即文件格式
适用于.png文件、.avi文件
```python
#二进制形式打开文件
bf = open("f.txt", "rb")
print(bf.readline())
bf.close()
>>>
b'\xd6\xd0\xb9\xfa\xca\xc7\xb8\xf6\xce\xb0
\xb4\xf3\xb5\xc4\xb9\xfa\xbc\xd2\xa3\xa1
```
### 二、文件的打开和关闭
文件处理的步骤：打开-操作-关闭
文件的打开
```python
<变量名> = open(<文件名>, <打开模式>)
```
image-20200908231855656
**打开模式**

| 文件的打开模式 | 描述 |
| --- | --- |
| 'r' | 只读模式，默认值，如果文件不存在，返回FileNotFoundError |
| 'w' | 覆盖写模式，文件不存在则创建，存在则完全覆盖 |
| 'x' | 创建写模式，文件不存在则创建，存在则返回FileExistsError |
| 'a' | 追加写模式，文件不存在则创建，存在则在文件最后追加内容 |
| 'b' | 二进制文件模式 |
| 't' | 文本文件模式，默认值 |
| '+' | 与r_w_x/a一同使用，在原功能基础上增加同时读写功能 |

**文件的关闭**
```python
<变量名>.close()
```
### 三、文件内容的读取
| 操作方法 | 描述 |
| --- | --- |
| .read(size=-1) | 读入全部内容，如果给出参数，读入前size长度 |
| .readline(size=-1) | 读入一行内容，如果给出参数，读入该行前size长度 |
| .readlines(hint=-1) | 读入文件所有行，以每行为元素形成列表。如果给出参数，读入前hint行 |

```python
>>>s = f.read(2)
中国

>>>s = f.readline()
中国是一个伟大的国家！

>>>s = f.readlines()
['中国是一个伟大的国家！']
```
**文件的全文本操作**
**遍历全文本方法一：一次读入，统一处理**
```python
fname = input("请输入要打开的文件名称:")
fo = open(fname,"r")
txt = fo.read()
#对全文txt进行处理
fo.close()
```
**遍历全文本方法二：按数量读入，逐步处理**
```python
fname = input("请输入要打开的文件名称:")
fo = open(fname,"r")
txt = fo.read(2)
while txt != "":
    #对txt进行处理
	txt = fo.read(2)
fo.close()
```
**逐行遍历文件方法一：一次读入，分行处理**
```python
fname = input("请输入要打开的文件名称:")
fo = open(fname,"r")
for line in fo.readlines():
	print(line)
fo.close()
```
**逐行遍历文件方法二：分行读入，逐行处理**
```python
fname = input("请输入要打开的文件名称:")
fo = open(fname,"r")
for line in fo:
	print(line)
fo.close()
```
### 四、数据的文件写入
| 操作方法 | 描述 |
| --- | --- |
| .write(s) | 向文件写入一个字符串或字节流 |
| .writelines(lines) | 将一个元素全为字符串的列表写入文件 |
| .seek(offset) | 改变当前文件操作指针的位置，offset含义如下：0 – 文件开头； 1 – 当前位置； 2 – 文件结尾 |

```python
>>>f.write("中国是一个伟大的国家!")

>>>ls = ["中国", "法国", "美国"]
>>>f.writelines(ls)
中国法国美国

>>>f.seek(0) #回到文件开头
```
**注意写入时文件操作指针的位置**
```python
fo = open("output.txt","w+")
ls = ["中国", "法国", "美国"]
fo.writelines(ls)
for line in fo: 
	print(line)
>>> fo.close()	#没有任何输出
```
```python
fo = open("output.txt","w+")
ls = ["中国", "法国", "美国"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
	print(line)
fo.close()	＃输出：中国法国美国
```
## 7.2 实例11：自动轨迹绘制
### 一、问题分析
需求：根据脚本来绘制图形
不通过写代码而通过写数据绘制轨迹
数据脚本是自动化最重要的一步
### 二、代码实例
基本思路：

1. 步骤一：定义数据文件格式（接口）
2. 步骤二：编写程序，根据文件接口解析参数绘制图形
3. 步骤三：编制数据文件
```python
#AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("data.txt")
for line in f:
	line = line.replace("\n","")
	datals.append(list(map(eval, line.split(","))))
f.close()
#自动绘制
for i in range(len(datals)):
	t.pencolor(datals[i][3],datals[i][4],datals[i][5])
	t.fd(datals[i][0])
	if datals[i][1]:
		t.right(datals[i][2])
	else:
		t.left(datals[i][2])
```
### 三、举一反三
自动化思维：数据和功能分离，数据驱动的自动运行
接口化设计：格式化设计接口，清晰明了
二维数据应用：应用维度组织数据，二维数据最常用
## 7.3 一维数据的格式化和处理
### 一、数据组织的维度
**一维数据**
由对等关系的有序或无序数据构成，采用线性方式组织
对应列表、数组和集合等概念
**二维数据**
由多个一维数据构成，是一维数据的组合形式
表格是典型的二维数据，其中，表头是二维数据的一部分
**多维数据**
由一维或二维数据在新维度上扩展形成
**高维数据**
仅利用最基本的二元关系展示数据间的复杂结构
**数据的操作周期**
存储——表示——操作
### 二、一维数据的表示
**如果数据间有序：使用列表类型**
列表类型可以表达一维有序数据
for循环可以遍历数据，进而对每个数据进行处理
**如果数据间无序：使用集合类型**
集合类型可以表达一维无序数据
for循环可以遍历数据，进而对每个数据进行处理
### 三、一维数据的存储
**存储方式一：空格分隔**
使用一个或多个空格分隔进行存储，不换行
缺点：数据中不能存在空格
**存储方式二：逗号分隔**
使用英文半角逗号分隔数据进行存储，不换行
缺点：数据中不能有英文逗号
**储存方式三：其他方式**
使用其他符号或符号组合进行分隔，建议采用特殊符号
缺点：需要根据数据特点定义，通用性较差
### 四、一维数据的处理
将存储的数据读入程序
将程序表示的数据写入文件
**读入处理**
```python
txt = open(fname).read()
ls = txt.split()	#以空格分隔
f.close

txt = open(fname).read()
ls = txt.split("$")	#以$分隔
f.close
```
**写入处理**
```python
ls = ['中国'，'美国'，'日本']
f = open(fname, 'w')
f.write(' '.join(ls))
f.close
```
## 7.4 二维数据的格式化和处理
### 一、二维数据的表示
**使用列表类型**

-  列表类型可以表达二维数据 
-  使用二维列表 

[[3.3, 3.4, 3.5], [1.2, 2.2, 2.3]]

-  使用两层for循环遍历每个元素 
-  外层列表中每个元素可以对应一行，也可以对应一列 
### 二、CSV格式与二维数据存储
CSV: Comma-Separated-Values

-  国际通用的一二维数据存储格式，一般为.csv扩展名 
-  每行一个一维数据，采用逗号分隔，无空行 
-  Excel和一般编辑软件都可以读入或另存为csv文件 
-  如果某个元素缺失，逗号仍要保留 
-  二维数据的表头可以作为数据存储，也可以另行存储 
-  逗号为英文半角逗号，逗号与数据之间无额外空格 
-  按行存或者按列存都可以，具体由程序决定 
-  一般索引习惯：ls[row][column]，先行后列 
-  根据一般习惯，外层列表每个元素是一行，按行存 
### 三、二维数据的处理
**从CSV格式的文件中读入数据**
```python
fo = open(fname)
ls = []
for line in fo.readlines():
    line = line.replace("\n","")
    ls.append(ling.split(","))
fo.close
```
**将数据写入CSV格式的文件**
```python
ls = [[],[],[]]	#二维列表
f= open(fname,'w')
for item in ls:
    f.write(','.join(item)+'\n')
f.close
```
**采用二层循环**
```python
ls = [[1,2],[3,4],[5,6]]
for row in ls:
    for column in row:
        print(column)
```
## 7.5 模块6：wordcloud库的使用
### 一、wordcloud库使用说明
**wordcloud库把词云当作一个WordCloud对象**
wordcloud.WordCloud()代表一个文本对应的词云
可以根据文本中词语出现的频率等参数绘制词云
词云的绘制形状、尺寸和颜色都可以设定
**wordcloud库常规方法**
**w = wordcloud.WordCloud()**
以WordCloud对象为基础
配置参数、加载文本、输出文件

| 方法 | 描述 |
| --- | --- |
| w.generate(txt) | 向WrodCloud对象w中加载文本txt |
| w.to_file(filename) | 将词云输出为图像文件，.png或.jpg格式 |

```python
import wordcloud
c = wordcloud.WordCloud()			#步骤1：配置对象参数
c.generate("wordcloud by Python")	#步骤2：加载词云文本
c.to_file("pywordcloud.png")		#步骤3：输出词云文件
```
### 配置对象参数
**w = wordcloud.WordCloud(<参数>)**

| 参数 | 描述 |
| --- | --- |
| width | 指定词云对象生成图片的宽度，默认400像素 |
| height | 指定词云对象生成图片的高度，默认200像素 |
| min_font_size | 指定词云中字体的最小字号，默认4号 |
| max_font_size | 指定词云中字体的最大字号，根据高度自动调节 |
| font_step | 指定词云中字体字号的步进间隔，默认为1 |
| font_path | 指定字体文件的路径，默认None |
| max_words | 指定词云显示的最大单词数量，默认200 |
| stop_words | 指定词云的排除词列表，即不显示的单词列表 |
| mask | 指定词云形状，默认为长方形，需要引用imread()函数 |
| backgound_color | 指定词云图片的背景颜色，默认为黑色 |

```python
>>>w=wordcloud.WordCloud(width=600)
>>>w=wordcloud.WordCloud(height=400)
>>>w=wordcloud.WordCloud(min_font_size=10)
>>>w=wordcloud.WordCloud(max_font_size=20)
>>>w=wordcloud.WordCloud(font_step=2)
>>>w=wordcloud.WordCloud(font_path="msyh.ttc")
>>>w=wordcloud.WordCloud(max_words=20)
>>>w=wordcloud.WordCloud(stop_words={"Python"})

>>>from scipy.misc import imread
>>>mk=imread("pic.png")
>>>w=wordcloud.WordCloud(mask=mk)

>>>w=wordcloud.WordCloud(background_color="white")
```
```python
import wordcloud
txt = "life is short, you need python"
w = wordcloud.WordCloud( background_color = "white")
w.generate(txt)
w.to_file("pywcloud.png")
```
```python
import jieba
import wordcloud
txt = "程序设计语言是计算机能够理解和\
识别用户操作意图的一种交互体系，它按照\
特定规则组织计算机指令，使计算机能够自\
动进行各种运算处理。"
w = wordcloud.WordCloud( width=1000,font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")
```
## 7.6 实例12：政府工作报告词云
### 基本思路：

1. 读取文件、分词整理
2. 设置并输出词云
3. 观察结果，优化迭代
### 代码
```python
#GovRptWordCloudV1.py
import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordClouD(font_path = "msyh.ttf",\
                       width = 1000, height = 700, background_color = "white",\
                       )    #生成词云对象
w.generate(txt)
w.to_file("grwordcloud.png")
```
```python
＃GovRptWordCloudV1.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("fivestart.png")    ＃读取图片
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordClous(font_path = "msyh.ttc",mask = mask\
                       width = 1000, height = 700, background_color = "white",\
                       )    ＃生成词云对象
w.generate(txt)
w.to_file("grwordcloud.png")
```
# 第8章 程序设计方法学
## 8.1 实例13：体育竞技分析
### 一、问题分析
体育竞技分析：

- 需求：毫厘是多少？如何科学分析体育竞技比赛？
- 输入：球员的水平
- 输出：可预测的比赛成绩

体育竞技分析：模拟N场比赛

- 计算思维：抽象+自动化
- 模拟：抽象比赛过程+自动化执行N场比赛
- 当N越大时，比赛结果分析会越科学
### 二、自顶向下和自底向上
**自顶向下（设计）**
解决复杂问题的有效方式

- 将一个总问题表达为若干个小问题组成的形式
- 使用同样方法进一步分解小问题
- 直至，小问题可以用计算机简单明了的解决

**自底向上（执行）**
逐步组建复杂系统的有效测试方法

- 分单元测试，逐步组装
- 按照自顶向下相反的路径操作
- 直至，系统各部分以组装的思路都经过测试和验证
### 三、代码实例
程序总体框架及步骤

1. 打印程序的介绍性信息
2. 获得程序运行参数：proA，proB，n
3. 利用球员A和B的能力值，模拟n局比赛
4. 输出球员A和B获胜比赛的场次及概率

**第一阶段：程序总体框架及步骤**
```python
def main():
    printIntro()
	probA, probB, n = getInputs()
	winsA, winsB = simNGames(n, probA, probB)
	printSummary(winsA, winsB)
```
```python
def printIntro():
	print("这个程序模拟两个选手A和B的某种竞技比赛")
	print("程序运行需要A和B的能力值(以0到1之间的小数表示)")	＃介绍性内容，提高用户体验
```
```python
def getInputs():
	a = eval(input("请输入选手A的能力值(0-1): "))
	b = eval(input("请输入选手B的能力值(0-1): "))
	n = eval(input("模拟比赛的场次: "))
	return a, b,
```
```python
def printSummary(winsA, winsB):
	n = winsA + winsB
	print("竞技分析开始，共模拟{}场比赛".format(n))
	print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
	print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n)
```
**第二阶段：模拟N局比赛**
```python
def simNGames(n, probA, probB):
	winsA, winsB = 0, 0
	for i in range(n):
		scoreA, scoreB = simOneGame(probA, probB)
		if scoreA > scoreB:
			winsA += 1
		else:
			winsB += 1
return winsA, winsB
```
**第三阶段：根据分数判断局的结束**
```python
def gameOver(a,b):
    return a==15 or b==15
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving="B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving="A"
    return scoreA, scoreB
```
**整体代码**
```python
＃MatchAnalysis.py
from random import random
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
def getInputs():
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    return a, b, n
def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB
def gameOver(a,b):
    return a==15 or b==15
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving="B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving="A"
    return scoreA, scoreB
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
main()
```
### 三、举一反三
**理解自顶向下和自底向上**

- 理解自顶向下的设计思维：分而治之
- 理解自底向上的执行思维：模块化集成
- 自顶向下是“系统”思维的简化
## 8.2 Python程序设计思维
### 一、计算思维与程序设计
**抽象和自动化**

- 计算思维：Computational Thinking
- 抽象问题的计算过程，利用计算机自动化求解
- 计算思维是基于计算机的思维方式
### 二、计算生态与Python语言
**计算生态**
#### 开源运动
#### 没有顶层设计、以功能为单位、具备三个特点

- 竞争发展
- 相互依存
- 迅速更迭

**计算生态的价值**
**创新：跟随创新、集成创新、原始创新**
**计算生态的运用**
### 三、用户体验与软件产品
**用户体验：**
实现功能到关注体验

- 用户体验指用户对产品建立的主观感受和认识
- 关心功能实现，更要关心用户体验，才能做出好产品
- 编程只是手段，不是目的，程序最终为人类服务

**提高用户体验的方法：**
**方法一：进度展示**

- 如果程序需要计算时间，可能产生等待
- 如果程序有若干步骤，需要提示用户
- 如果程序可能存在大量次数的循环

**方法二：异常处理**

- 当获得用户输入，对合规性需要检查
- 当读写文件时，对结果进行判断
- 当进行输入输出时，对运算结果进行判断

**其他类方法**
打印输出：特定位置，输出程序运行的过程信息
日志文件：对程序异常及用户使用进行定期记录
帮助信息：给用户多种方式提供帮助信息
### 四、基本的程序设计模式
**从IPO开始**

- 确定IPO：明确计算部分及功能边界
- 编写程序：将计算求解的设计变成现实
- 调试程序：确保程序按照正常逻辑能够正确运行

**自顶向下设计**
**模块化设计**

-  通过函数或对象封装将程序划分为模块及模块间的表达 
-  具体包括：主程序、子程序和子程序间关系 
-  分而治之：一种分而治之、分层抽象、体系化的设计思想 
-  紧耦合：两个部分之间交流很多，无法独立存在 
-  松耦合：两个部分之间交流较少，可以独立存在 
-  模块内部紧耦合、模块之间松耦合 

**配置化设计**

- 引擎+配置：程序执行和配置分离，将可选参数配置化
- 将程序开发变成配置文件编写，扩展功能二不修改程序
- 关键在于接口设计，清晰明了、灵活可扩展

**应用开发的四个步骤：**

1. 产品定义
2. 系统架构
3. 设计与实现
4. 用户体验

从应用需求到软件产品：

1. 产品定义：对应用需求充分理解和明确定义。产品定义，而不仅是功能定义，要考虑商业模式
2. 系统架构：以系统方式思考产品的技术实现。系统架构，关注数据流、模块化、体系架构
3. 设计与实现：结合结构完成关键设计及系统实现。结合可扩展性、灵活性等进行设计优化
4. 用户体验：从用户角度思考应用效果。用户至上，体验优先，以用户为中心
## 8.3 Python第三方库安装
### 一、看见更大的Python世界
**Python社区**
Pypi
**安装Python第三方库**

- 使用pip命令
- 集成安装方法
- 文件安装方法
### 二、第三方库的pip安装方法
**使用pip安装工具**
**常用的pip命令**
```
D:\>pip install <第三方库名>		#安装指定的第三方库
D:\>pip install -U <第三方库名>	#使用-U标签更新已安装的指定第三方库
D:\>pip uninstall <第三方库名>	#卸载指定的第三方库
D:\>pip download <第三方库名>	#下载但不安装指定的第三方库
D:\>pip show <第三方库名>		#列出某个指定第三方库的详细信息
D:\>pip search <关键词>		 #根据关键词在名称和介绍中搜索第三方库
D:\>pip list				   #列出当前系统已经安装的第三方库
```## 三、第三方库的集成安装方法
**集成安装：结合特定Python开发工具的批量安装**

Anaconda：
* 支持近800个第三方库
* 包含多个主流工具
* 适合数据计算领域开发
## 四、第三方库的文件安装方法
**http://www.lfd.uci.edu/~gohlke/pythonlibs/**
1. 在UCI页面上搜索wordcloud
2. 下载对应版本的文件
3. 使用pip install <文件名> 安装

# 8.4 模块7：os库的基本使用
## 一、os库基本介绍
os库提供通用的、基本的操作系统交互功能
* os库是Python标准库
* 常用路径操作、进程管理、环境参数等几类
	* 路径操作：os.path子库，处理文件路径及信息
	* 进程管理：启动系统中其他程序
	* 环境参数：获得系统软硬件信息等环境参数
## 二、os库之路径操作
**os.path子库以path为入口，用于操作和处理文件路径**

**import os.path	或	import os.path as op**

| 函数                   | 描述                                             |
| ---------------------- | ------------------------------------------------ |
| os.path.abspath(path)  | 返回path在当前系统中的绝对路径                   |
| os.path.normpath(path) | 归一化path的表示形式，统一用\分隔路径           |
| os.path.relpath(path)  | 返回当前程序与文件之间的相对路径 (relative path) |
```python
>>>os.path.abspath("file.txt")
'C:\\Users\\Tian Song\\Python36-32\\file.txt'

>>>os.path.normpath("D://PYE//file.txt")
'D:\\PYE\\file.txt'

>>>os.path.relpath("C://PYE//file.txt")
'..\\..\\..\\..\\..\\..\\..\\PYE\\file.txt'
```
| 函数 | 描述 |
| --- | --- |
| os.path.dirname(path) | 返回path中的目录名称 |
| os.path.basename(path) | 返回path中最后的文件名称 |
| os.path.join(path,*paths) | 组合path与paths，返回一个路径字符串 |

```python
>>>os.path.dirname("D://PYE//file.txt")
'D://PYE'

>>>os.path.basename("D://PYE//file.txt")
'file.txt'

>>>os.path.join("D:/", "PYE/file.txt")
'D:/PYE/file.txt'
```
| 函数 | 描述 |
| --- | --- |
| os.path.exists(path) | 判断path对应文件或目录是否存在，返回True或False |
| os.path.isfile(path) | 判断path所对应是否为已存在的文件，返回True或False |
| os.path.isdir(path) | 判断path所对应是否为已存在的目录，返回True或False |

```python
>>>os.path.exists("D://PYE//file.txt")
False

>>>os.path.isfile("D://PYE//file.txt")
True
>>>os.path.isdir("D://PYE//file.txt")
False

>>>os.path.isdir("D://PYE//file.txt")
False
```
| 函数 | 描述 |
| --- | --- |
| os.path.getatime(path) | 返回path对应文件或目录上一次的访问时间 |
| os.path.getmtime(path) | 返回path对应文件或目录最近一次的修改时间 |
| os.path.getctime(path) | 返回path对应文件或目录的创建时间 |

```python
>>>os.path.getatime("D:/PYE/file.txt")
1518356633.7551725

>>>os.path.getmtime("D:/PYE/file.txt")
1518356633.7551725

>>time.ctime(os.path.getctime("D:/PYE/file.txt"))
'Sun Feb 11 21:43:53 2018'
```
| 函数 | 描述 |
| --- | --- |
| os.path.getsize(path) | 返回path对应文件的大小，以字节为单位 |

```python
>>>os.path.getsize("D:/PYE/file.txt")
180768
```
### 三、os库之进程管理
**os.system(command)**

- 执行程序或命令command
- 在Windows系统中，返回值为cmd的调用返回信息
### 四、os库之环境参数
**获取或改变系统环境信息**

| 函数 | 描述 |
| --- | --- |
| os.chdir(path) | 修改当前程序操作的路径 |
| os.getcwd() | 返回程序的当前路径 |

```python
>>>os.chdir("D:")

>>>os.getcwd()
'D:\\'
```
**获取操作系统环境信息**

| 函数 | 描述 |
| --- | --- |
| os.getlogin() | 获取当前系统登录用户名称 |
| os.cpu_count() | 获取当前系统的CPU数量 |
| os.urandom(n) | 获取n个字节长度的随机字符串，通常用于加解密运算 |

```python
>>>os.getlogin()
'Tian Song'

>>>os.cpu_count()
8

>>>os.urandom(10)
b'7\xbe\xf2!\xc1=\x01gL\xb3'
```
## 8.5 实例14：第三方库自动安装脚本
### 一、问题分析

- 需求：批量安装第三方库需要人工干预，能否自动安装
- 自动执行pip逐一根据安装需求安装
### 二、代码实例
```python
#BatchInstall.py
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
		"jieba","beautifulsoup4","wheel","networkx","sympy",\
		"pyinstaller","django","flask","werobot","pyqt5",\
		"pandas","pyopengl","pypdf2","docopt","pygame"}
try:
	for lib in libs:
		os.system("pip install " + lib)
	print("Successful") 
except:
	print("Failed Somehow")
```
# 第9章 python计算生态概览
## 一、单元开篇

- 数据表示：采用合适方式用程序表达数据
- 数据清理：数据归一化、数据转换、异常值处理
- 数据统计：数据的该要理解，数量、分布、中位数等
- 数据可视化：直观展示数据内涵的方式
- 数据挖掘：从数据分析获得知识，产生数据外的价值
- 人工智能：数据_语言_图像/视觉等方面深度分析与决策
## 二、Python库之数据分析
**Numpy：表达N维数组的最基础库**

- Python接口使用，C语言实现，计算速度优异
- Python数据分析及科学计算的基础库，支持Pandas等
- 提供直接的矩阵运算、广播函数、线性代数等功能

[**http://www.numpy.org**](http://www.numpy.org)
**Pandas：Python数据分析高层次应用库**

- 提供了简单易用的数据结构和数据分析工具
- 理解数据类型与索引的关系，操作索引即操作数据
- Python最主要的数据分析功能库，基于Numpy开发

Series = 索引+一维数据
DataFrame = 行列索引+二维数据
[**http://pandas.pydata.org**](http://pandas.pydata.org)
**SciPy：数学、科学和工程计算功能库**

- 提供了一批数学算法及工程数据运算功能
- 类似Matlab，可用于傅里叶变换、信号处理等应用
- Python最主要的科学计算功能库，基于Numpy开发

[**http://www.scipy.org**](http://www.scipy.org)
## 三、Python库之数据可视化
**Matplotlib：高质量的二维数据可视化功能库**

- 提供超过100中数据可视化显示效果
- 通过matplotlib。pyplot子库调用各种可视化效果
- Python最主要的数据可视化功能库，基于Numpy开发

[**http://matplotlib.org**](http://matplotlib.org)
**Seaborn：统计类数据可视化功能库**

- 提供了一批高层次的统计类数据可视化展示效果
- 主要展示数据间分布、分类和线性关系等内容
- 基于Matplotlib开发，支持Numpy和Pandas

[**http://seaborn.pydata.org/**](http://seaborn.pydata.org/)
**Mayavi：三维科学数据可视化功能库**

- 提供了一批简单易用的3D科学计算数据可视化展示效果
- 目前版本是Mayavi2，三维可视化最主要的第三方库
- 支持Numpy、TVTK、Traits、Envisage等第三方库

[**http://docs.enthought.com/mayavi/mayavi/**](http://docs.enthought.com/mayavi/mayavi/)
## 四、Python库之文本处理
**PyPDF2：用来处理pdf文件的工具集**

- 提供了一批处理PDF文件的计算功能
- 支持获取信息、分隔/整合文件、加密解密等
- 完全Python语言实现，不需要额外以来，功能稳定
```python
from PyPDF2 import PdfFileReader, PdfFileMerger
merger = PdfFileMerger()
input1 = open("document1.pdf", "rb")
input2 = open("document2.pdf", "rb")
merger.append(fileobj = input1, pages = (0,3))
merger.merge(position = 2, fileobj = input2, pages = (0,1))
output = open("document-output.pdf", "wb")
merger.write(output)
```
[**http://mstamy2.github.io/PyPDF2**](http://mstamy2.github.io/PyPDF2)
**NLTK：自然语言文本处理第三方库**

- 提供了一批简单易用的自然语言文本处理功能
- 支持语言文本分类、标记、语法句法、语义分析等
- 最优秀的Python自然语言处理库

[**http://www.nltk.org/**](http://www.nltk.org/)
**Python-docx：创建或更新Microsoft Word文件的第三方库**

- 提供创建或更新.doc .docx等文件的计算功能
- 增加并配置段落、图片、表格、文字等，功能全面
```python
from docx import Document
document = Document()
document.add_heading('Document Title', 0)
p = document.add_paragraph('A plain paragraph having some ')
document.add_page_break()
document.save('demo.docx')
```
[**http://python-docx.readthedocs.io/en/latest/index.html**](http://python-docx.readthedocs.io/en/latest/index.html)
## 五、Python库之机器学习
**Scikit-learn：机器学习方法工具集**

- 提供一批统一化的机器学习方法功能接口
- 提供聚类、分类、回归、强化学习等计算功能
- 机器学习最基本且最优秀的Python第三方库

[scikit-learn: machine learning in Python — scikit-learn 0.16.1 documentation](http://scikit-learn.org/)
**TensoFlow：AlphaGo背后的机器学习计算框架**

- 谷歌公司推动的开源机器学习框架
- 将数据流图作为基础，图节点代表运算，边代表张量
- 应用机器学习方法的一种方式，支撑谷歌人工智能应用
```python
import tensorflow as tf
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
res = sess.run(result)
print('result:', res)
```
[**https://www.tensorflow.org/**](https://www.tensorflow.org/)
**MXNet：基于神经网络的深度学习计算框架**

- 提供可扩展的神经网络及深度学习计算功能
- 可用于自动驾驶、机器翻译、语音识别等众多领域
- Python最重要的深度学习计算框架

[**https://mxnet.incubator.apache.org/**](https://mxnet.incubator.apache.org/)
## 9.2 实例15：霍兰德人格分析雷达图
```python
#HollandRadarDraw
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
radar_labels = np.array(['研究型(I)','艺术型(A)','社会型(S)',\
                         '企业型(E)','常规型(C)','现实型(R)']) #雷达标签
nAttr = 6
data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                 [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                 [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                 [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                 [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                 [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]]) #数据值
data_labels = ('艺术家', '实验员', '工程师', '推销员', '社会工作者','记事员')
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles,data,'o-', linewidth=1, alpha=0.2)
plt.fill(angles,data, alpha=0.25)
plt.thetagrids(angles*180/np.pi, radar_labels,frac = 1.2)
plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='large')
plt.grid(True)
plt.savefig('holland_radar.jpg')
plt.show()
```
## 9.3 从Web解析到网络空间
### 一、Python库之网络爬虫
**Request：最友好的网络爬虫功能库**

- 提供了简单易用的类HTTP协议网络爬虫功能
- 支持连接池、SSL、Cookies、HTTPS(S)代理等
- Python最主要的页面级网络爬虫功能库
```python
import requests
r=requests.get('https://api.github.com/user',auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
```
[**http://www.python-requests.org/**](http://www.python-requests.org/)
**Scrapy:优秀的网络爬虫框架**

- 提供了构建网络爬虫系统的框架功能，功能半成品
- 支持批量和定时网页爬取、提供数据处理流程等
- Python最主要且最专业的网络爬虫框架

[**https://scrapy.org**](https://scrapy.org)
**pyspider：强大的Web页面爬取系统**

- 提供了完整的页面爬取系统构建功能
- 支持数据库后端、消息队列、优先级、分布式架构等
- Python重要的网络爬虫类第三方库

[**http://docs.pyspider.org**](http://docs.pyspider.org)
### 二、Python库之Web信息提取
**Beautiful Soup： HTML和XML的解析库**

- 提供了解析HTML和XML等Web信息的功能
- 又名beautifulsoup4或bs4，可以加载多种解析引擎
- 常与网络爬虫库搭配使用，如Scrapy、requests

[**https://www.crummy.com/software/BeautifulSoup/bs4**](https://www.crummy.com/software/BeautifulSoup/bs4)
**Re：正则表达式解析和处理功能库**

- 提供了定义和解析正则表达式的一批通用功能
- 可用于各类场景，包括顶点的Web信息提取
- Python最主要的标准库之一，无需安装
```python
re.search()
re.match()
re.findall()
r'\d{3}-\d{8}|\d{4}-\d{7}'
re.split()
re.finditer()
re.sub()
```
[**https://docs.python.org/3.6/library/re.html**](https://docs.python.org/3.6/library/re.html)
**Python-Goose：提供文章类型Web页面的功能库**

- 提供了对Web页面中文章信息、视频等元数据的提取功能
- 针对特定类型Web页面，应用覆盖面较广
- Python最主要的Web信息提取库
```python
from goose import Goose
url = 'http://www.elmundo.es/elmundo/2012/10/28/espana/1351388909.html'
g = Goose({'use_meta_language': False, 'target_language':'es'})
article = g.extract(url=url)
article.cleaned_text[:150]
```
[**https://github.com/grangier/python-goose**](https://github.com/grangier/python-goose)
### 三、Python库之Web网站开发
**Django：最流行的Web应用框架**

- 提供了构建Web系统的基本应用框架
- MTV模式：模型（model）、模板（Template）、视图（Views）
- Python最重要的Web应用框架，略微复杂的应用框架

[**https://www.djangoproject.com**](https://www.djangoproject.com)
**Pyramid：规模适中的Web应用框架**

- 提供了简单方便构建Web系统的应用框架
- 不大不小，规模适中。适合快速构建并适度扩展类应用
- Python产品级Web应用框架，起步简单可扩展性好
```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
def hello_world(request):
	return Response('Hello World!')
if __name__ == '__main__':
	with Configurator() as config:
		config.add_route('hello', '/')
		config.add_view(hello_world, route_name='hello')
		app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 6543, app)
	server.serve_forever()
```
[**https://trypyramid.com/**](https://trypyramid.com/)
**Flask：Web应用开发框架**

- 提供了最简单构建Web系统的应用框架
- 特点是：简单、规模小、快速
- Django > Pyramid > Flask
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World!'
```
[**http://flask.pocoo.org**](http://flask.pocoo.org)
### 四、Python库之网络应用开发
**WeRoBot：微信公众号开发框架**

- 提供了解析微信服务器消息及反馈消息的功能
- 建立微信机器人的重要技术手段
```python
import werobot
robot = werobot.WeRoBot(token='tokenhere') 
@robot.handler
def hello(message):
	return 'Hello World!'
```
[**https://github.com/offu/WeRoBot**](https://github.com/offu/WeRoBot)
**aip：百度AI开放平台接口**

- 提供了访问百度AI服务的Python功能接口
- 语音、人脸、OCR、NLP、知识图谱、图像搜索等领域
- Python百度AI应用的最主要方式

[**https://github.com/Baidu-AIP/python-sdk**](https://github.com/Baidu-AIP/python-sdk)
**MyQR：二维码生成第三方库**

- 提供了生成二维码的系列功能
- 基本二维码、艺术二维码和动态二维码

[**https://github.com/sylnsfar/qrcode**](https://github.com/sylnsfar/qrcode)
## 9.4 从人机交互到艺术设计
### 一、Python库之图形用户界面
**PyQt5：Qt开发框架的Python接口**

- 提供了创建Qt5程序的Python API接口
- Qt是非常成熟的跨平台桌面应用开发系统，完备GUI
- 推荐的Python GUI开发第三方库

[**https://www.riverbankcomputing.com/software/pyqt**](https://www.riverbankcomputing.com/software/pyqt)
**wxPython：跨平台GUI开发框架**

- 提供了专用于Python的跨平台GUI开发框架
- 理解数据类型与索引的关系，操作索引即操作数据
- Python最主要的数据分析功能库，基于Numpy开发
```python
import wx
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)
app.MainLoop()
```
[**https://www.wxpython.org**](https://www.wxpython.org)
**PyGObject：使用GTK+开发GUI的功能库**

- 提供了整合GTK+、WebKitGTK+等库的功能
- GTK+：跨平台的一种用户图形界面GUI框架
- 实例：Anaconda采用该库构建GUI
```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
window = Gtk.Window(title="Hello World")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
```
[**https://pygobject.readthedocs.io**](https://pygobject.readthedocs.io)
### 二、Python库之游戏开发
**PyGame：简单的游戏开发功能库**

- 提供了基于SDL的简单游戏开发功能及实现引擎
- 理解游戏对外部输入的响应机制及角色构建和交互机制
- Python游戏入门最主要的第三方库

[**http://www.pygame.org**](http://www.pygame.org)
**Panda3D：开源、跨平台的3D渲染和游戏开发库**

- 一个3D游戏引擎，提供Python和C++两种接口
- 支持很多先进特性：法线贴图、光泽贴图、卡通渲染等
- 由迪士尼和卡尼吉梅隆大学共同开发

[**http://www.panda3d.org**](http://www.panda3d.org)
**cocos2d：构建2D游戏和图形界面交互式应用的框架**

- 提供了基于OpenGL的游戏开发图形渲染功能
- 支持GPU加速，采用树形结构分层管理游戏对象类型
- 适用于2D专业级游戏开发

[**http://python.cocos2d.org/**](http://python.cocos2d.org/)
### 三、Python库之虚拟现实
**VR Zero：在树莓派上开发VR应用的Python库**

- 提供了大量与VR开发相关的功能
- 针对树莓派的VR开发库，支持设备小型化，配置简单化
- 非常适合初学者实践VR开发及应用

[**https://github.com/WayneKeenan/python-vrzero**](https://github.com/WayneKeenan/python-vrzero)
**pyovr：Oculus Rift的Python开发接口**

- 针对Oculus VR设备的Python开发库
- 基于成熟的VR设备，提供全套文档，工业级应用设备
- Python+虚拟现实领域探索的一种思路

[**https://github.com/cmbruns/pyovr**](https://github.com/cmbruns/pyovr)
**Viazrd：基于Python的通用VR开发引擎**

- 专业的企业级虚拟现实开发引擎
- 提供详细的官方文档
- 支持多种主流的VR硬件设备，具有一定的通用性

[**http://www.worldviz.com/vizard-virtual-reality-software**](http://www.worldviz.com/vizard-virtual-reality-software)
### 四、Python库之图形艺术
**Quads：迭代的艺术**

- 对图片进行四分迭代，形成像素风
- 可以生成动图或静图图像
- 简单易用，具有很高的展示度

[**https://github.com/fogleman/Quads**](https://github.com/fogleman/Quads)
**ascii_art：ASCII艺术库**

- 将普通图片转为ASCII艺术风格
- 输出可以是纯文本或彩色文本
- 可采用图片格式输出

[**https://github.com/jontonsoup4/ascii_art**](https://github.com/jontonsoup4/ascii_art)
**turtle：海龟绘图体系**
[**https://docs.python.org/3/library/turtle.html**](https://docs.python.org/3/library/turtle.html)
## 9.5 实例16：玫瑰花绘制
艺术之于编程，设计之于编程

- 艺术：思想优先，编程是手段
- 设计：想法和编程同等重要
- 工程：编程优先，思想次之
