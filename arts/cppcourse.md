title: 实践课程
date: 2012-06-25
published: true

# 更新历史

* 2012-07-16: **作业提交时间延长至七月底**; [垃圾邮件的问题](#垃圾邮件的问题)
* 2012-07-11: 离线C++手册打包(以避免在windows下显示不正常); 集中[作业样例](#作业样例)
* 2012-07-09: 添加第[四次作业样例](#作业样例)
* 2012-07-07: **离线版C++手册**; 作业三基本要求样例; [如何检验作业三的正确性](#如何检验结果的正确性); 作业三Tips
* 2012-07-06: 作业三高阶要求样例; 更新作业提交时间说明; 7月6号内容
* 2012-07-05: 7月5号内容; 第五次作业; **更新作业deadline**
* 2012-07-04: 7月4号内容
* 2012-07-03: 7月3号的内容; 6月29号, 7月2号和3号的代码
* 2012-07-02: 7月2号的内容; 第四次作业; 使用库算法更新字符串的代码
* 2012-07-01: 6月30号的内容
* 2012-06-29: 6月29号的课件; 自学指南; 每次课对应的课本章节

# 学习资源

## 教材

Accelerated C++

电子版:

* [中文版](http://www.ppurl.com/2011/05/accelerated-c-%e4%b8%ad%e6%96%87%e7%89%88.html)
* [英文版](http://www.ppurl.com/2009/12/accelerated-c.html)
* [源码](http://acceleratedcpp.com/)

## C++手册

张酉夫同学制作的[cplusplus.com]的[离线版本(chm)](http://dl.answeror.com/u/3450602/cppcourse/cppref_120711.rar).

[cplusplus.com]: http://www.cplusplus.com

## 自学指南

1. 阅读每章最后一节(小结), 从而有针对性地补充知识点.
2. 阅读附录熟悉语法.
3. 多用Google和[cplusplus.com], 从书上找不如在网上搜.
4. 有空就做做每章后面的习题.
5. 不懂就给我发邮件:)

# 内容及课件

## C++简介

[课件下载](http://dl.answeror.com/u/3450602/cppcourse/lecture.1.introduction.pdf)

1. 程序设计的基本概念.
2. C++程序的编译和链接.
3. 表达式, 函数, 名字, 作用域, 变量, 流等基础概念.

对应课本第0章.

## C++使用基础

[课件下载](http://dl.answeror.com/u/3450602/cppcourse/lecture.2.use-cpp.pdf)

1. 字符和字符串.
2. 控制结构.
3. 批量数据处理.
4. 容器.
5. 迭代器.
6. 算法.

对应课本第1~7章(概述).

## Qt编程

[课件下载](http://dl.answeror.com/u/3450602/cppcourse/lecture.3-4.qt.pdf)

## 基于对象的C++编程

date: 2012-06-29

[课件下载](http://dl.answeror.com/u/3450602/cppcourse/lecture.5.a-step-futher.pdf)

### 知识点

1. 复习容器和迭代器.
2. 封装的概念.
3. 成员函数.
4. 构造函数.
5. 运算符重载.
6. 断言.

对应课本第9章.

### 代码

1. [学生类](https://gist.github.com/3038581)

## 使用顺序容器并分析字符串

date: 2012-06-30

1. 将上节课的按学生姓名排序的程序分离编译.
2. 以筛选学生为例解释vector和list的使用.
3. 分割字符串.
4. 连接字符串.

对应课本第5章.

## 使用库算法

date: 2012-07-02

### 知识点

1. 容器, 算法, 迭代器, 适配器之间的关系, 以及分层思想.
2. 用find\_if实现分割字符串.
3. [lambda](http://www.codeproject.com/Articles/71540/Explicating-the-new-C-standard-C-0x-and-its-implem#LambdaExpressions).
4. 函数重载和默认参数.
6. 谓词.
7. 讲解第一次作业.
8. 用库算法实现url查找.
9. 静态存储.

对应课本第6章前半部分.

### 代码

1. [使用库算法分割字符串](https://gist.github.com/3033946)
2. [用库算法提取URL](https://gist.github.com/3036611)

## 使用关联容器

date: 2012-07-03

### 知识点

第6章的:

1. `remove_copy_if`, `remove_if`, `partition`
2. 标准库算法的分类: 质变/非质变
3. 标准库算法的后缀: if, copy
4. 算法和容器操作对迭代器的影响(可能会使已有的迭代器无效)
5. 使用`accumulate`拼接字符串

第7章的:

1. `pair`
2. [auto](http://www.codeproject.com/Articles/71540/Explicating-the-new-C-standard-C-0x-and-its-implem#AutoKeyword)
3. `map`的下标操作符
4. 函数(指针)作为函数参数(关于函数指针的详细解释在第10章)
5. 使用`unique`算法去除连续的重复元素
5. 容器的`front`和`back`成员函数
6. `map`的`find`成员函数以及为什么不能对常量`map`使用下标操作符
7. 递归, 及其与数学归纳法的关系
8. 快速排序
9. `operator ()`
10. 无构造函数的结构体成员的初始化(`some_type foo = { some_value, another_value }`)

### 代码

1. [用库算法提取挂科学生](https://gist.github.com/3037001)
2. [拼接字符串(空格分隔)](https://gist.github.com/3037042)
3. [交叉引用](https://gist.github.com/3037132)
4. [根据文法随机生成句子](https://gist.github.com/3038519)
5. [快速排序的简单实现](https://gist.github.com/3038528)

## QT实例讲解

date: 2012-07-04

### 知识点

1. Qmake的使用方法.
2. 讲解第二次作业.
3. `QFile`, `QTextstream`读写文件
4. `QObject::sender`信号发送者
5. `QDir`目录查询
6. 复习`QSignalMapper`
7. Layout `addWidget` `insertWidget`
8. 动态创建控件(`QPushButton`, `QDialog`)

## 编写泛型函数

date: 2012-07-05

### 知识点

1. 基本语法(类模板部分参见第11章)
2. 函数模板, 模板函数, 类模板, 模板类的区别
3. 隐式接口和编译期多态([Effective C++ Item 41](http://www.civilnet.cn/book/kernel/Effective%20C++%20(Third%20Edition)/ch07lev1sec1.html))
4. [迭代器的分类](http://cplusplus.com/reference/std/iterator/)
5. 模板实例化([简介](http://zh.wikipedia.org/wiki/%E6%A8%A1%E6%9D%BF_(C%2B%2B)#.E6.A8.A1.E6.9D.BF.E5.AF.A6.E4.BE.8B.E5.8C.96), [很好的文章但是链接挂了](http://blog.copton.net/articles/linker/index.html))
6. 模板参数推导和使用过程中的类型转换与歧义.
7. 数据结构独立性.
8. 二分搜索(`binary_search`, `lower_bound`, `upper_bound`)

## 管理内存和低级数据结构

date: 2012-07-06

### 知识点

1. 指针语法
2. 两种const指针
3. 函数指针及其[简便的声明方式](http://stackoverflow.com/questions/75538/hidden-features-of-c/1414869#1414869)
4. 函数对象(仿函数)
5. [简单的单元测试写法](https://gist.github.com/3054103)
6. 讲解第三次作业

### 代码

1. [作业三高阶要求样例]
2. [作业三基本要求样例]

# 作业

## 提交内容

* OJ上的题目: 源代码 + 提交号(写在一个txt文件里)
* 非OJ题目: 源代码

## 提交方式

上传到FTP对应目录下:

* 地址: ftp://10.11.131.101:27
* 用户名: dxq
* 密码: dxq
* 文件名: 学号\_姓名拼音.zip(其他压缩格式均可)

## 提交时间

~~课程结束后的一周之前.~~ 提交时间延长至七月底, 觉得做得不好的同学可以再次上传.

如果在校外无法上传到FTP, 可以把作业通过邮件发给我.

如果不能按时提交, 请发邮件跟我说明情况, 并尽早提交. 截止日期以教务处下达提交成绩的时间. 我会把这个时间更新到主页上(现在还不知道). **延时提交可能会酌情扣分**.

## 垃圾邮件的问题

有同学反映发到我的gmail邮箱被当成垃圾邮件了, 我看了绝大多数垃圾邮件都存在以下两个特征(中的一个):

* 邮件没有正文, 只有附件.
* 邮件正文中包含QQ表情(即包含图片).

解决办法:

* 邮件里写点东西, 不要空着.
* 尽量不要用QQ邮箱, 用了也请不要加表情.
* 实在不行就发到另一位助教的邮箱.

## 第一次作业

[Palindrom Numbers](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemId=78)

## 第二次作业

* 实现类似onenote组织方式的记事本界面程序一个
* 要求：
    * 默认加载已有的文本笔记；
    * 至少有一种笔记分类组织功能（类别或者页面）
* 备注
    * 不限制界面样式(界面自主设计，按钮或TAB等均可)
    * 不限制编程平台
    * 提交源代码及release版可执行程序(附带文档说明更佳)

![onenote](http://dl.answeror.com/u/3450602/cppcourse/onenote.png){: .border }

## 第三次作业

输入
  : 包含一行字符串的文件
输出
  : 包含(对字符)排序后的文件

### 要求

**以下百分号表示所能得的分数, 只要交一题**

基本要求(70%)

* 仿照vector设计文件的容器类, 容器元素为char, 包含begin和end方法
* 设计对应的随机访问迭代器
* 用sort对该容器排序

进阶要求(85%)

* 输入输出文件内容为二进制整数

高阶要求(100%)

* 输入输出文件内容可以为任意内建类型, 如字符, 二进制整数, 二进制浮点数等
* 容器及相关类写成类模板

### Tips

* [fstream](http://cplusplus.com/reference/iostream/fstream/): `read`, `write`, `seekg`, `tellg`, `seekp`, `tellp`
* [获取文件长度](http://bytes.com/topic/c/answers/139776-size-file)
* `sizeof`
* [读写二进制数据](http://stackoverflow.com/a/2478575/238472)
* 迭代器
    * 索引操作符: 12.3
    * 递增/递减操作符: A.3.1
    * 随机访问迭代器支持的操作: B.2.5
* 代理类
    * 赋值操作符: 11.3.2
    * 类型转换操作符: 12.5

### 如何检验结果的正确性

在进阶要求和高阶要求中, 需要进行二进制读写, 其输入和输出都是二进制数据, 无法直接用文本文件构造输入, 也不能用肉眼看出文件中结果的正确性.

解决办法是从控制台输入数字(整数, 实数等), 然后在程序里转换成二进制的字符数组再用流的`write`方法写入到文件里作为输入; 经过`sort`之后在从文件中用流的`read`方法读出字符数组, 转换成数字之后输出到控制台, 以检验结果的正确性.

## 第四次作业

[ZOJ 2727 List the Books](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemId=1727)

### 要求

1. 用`stable_partition`或者`partition`自己实现快速排序.
2. 快排写成模板则更好.

### Tips

* ZOJ不能使用lambda
* 每次输出之间要有一个空行
* `stable_partition`
* `partition`
* `min_element`
* `swap`
* 二元谓词
* 函数对象(仿函数)
* 函数指针

## 第五次作业

Accelerated C++ 习题8-2.

### 要求

**以下百分号表示所能得的分数, 只要交一题**

基本要求(90%)

* 完成习题并给出单元测试.

进阶要求(100%)

* 完成习题并使用作业三的容器做单元测试.

### Tips

1. [最简单的单元测试写法](https://gist.github.com/3054103)
2. `remove`函数(及其后缀版本)只需测试有效区间

## 作业样例

* [作业三高阶要求样例]
* [作业三基本要求样例]
* [第四次作业样例](https://gist.github.com/0983c81a38ff921d6c0f)
* [简单的单元测试写法]

# 联系方式

* C++: answeror (no spam please) at gmail dot com
* Qt: 21021021 (no spam please) at zju dot edu dot cn

[作业三高阶要求样例]: https://gist.github.com/ac3642565a27d229fc0d
[作业三基本要求样例]: https://gist.github.com/3065517
[简单的单元测试写法]: https://gist.github.com/3054103
