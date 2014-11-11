title: 基于个人经验的研究指南
date: 2013-03-04
json: true

# 引言

本文旨在为实验室新生提供一般性的, 基于个人经验的, 研究指南. 主要介绍一些开发方面的基本技术和工具. 以后可能会进一步扩充其它内容.

[这里](http://dl.answeror.com/u/3450602/re-search.pdf)是12年11月的一次演讲, 关于研究过程中的基本的搜索技术和工具.

# 搜索技术

## 一般性搜索

使用英文Google(<http://google.com/ncr>). 抽风的时候建议使用英文Bing. Chrome可以在

    Settings > Search > Manage search engines...

里添加`http://www.google.com/search?&q=%s`作为默认搜索引擎.

## 文件搜索

# 文件管理

## 文件命名

1. **不要**包含空格(原因参见[这里](http://blog.sina.com.cn/s/blog_469ca3460100c6m3.html))! 建议使用`-`或者`_`代替空格.
2. 尽量使用小写字母.

# 开发工具

编程语言和开发工具之间的区分并不那么明显, 比如CMake虽然是构建工具, 但是它也具有自己的一套语法. 所以把两者并为一节.

## C++

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | Accelerated C++
            td > a href='http://book.douban.com/subject/1456835/' | 豆瓣
            td | <em>个人</em>推荐的入门书籍. 很薄, 一周可以看完. 有中文版.
        tr
            td | Effective C++
            td > a href='http://book.douban.com/subject/1453373/' | 豆瓣
            td | 与其说是C++的精华, 不如说是C++语言本身的缺陷列表, 而且是严重的缺陷, 以至于需要单独列出条目来提醒使用者其中的陷阱. 不过正是因为这些缺陷太过严重, 所以你必须了解它. 中文版推荐<em>侯捷</em>的版本.
        tr
            td | STL源码剖析
            td > a href='http://book.douban.com/subject/1110934/' | 豆瓣
            td |
                这本书不仅仅具有字面上的功能, 它还是:
                ul
                    li | 我见过的最好的STL参考手册. 因为每个函数/类都有详尽的调用说明和性能分析.
                    li | 我见过的最现实的数据结构教材. 既有深度, 又有极高的代码质量.
                    li | C++语言细节的实用范例. 从自定义动态内存分配, 到模板元编程基础如tag dispatch和traits, 面面俱到. 其中部分技术是学习Boost库的基础.
        tr
            td > strong | The C++ Programming Language
            td > a href='http://book.douban.com/subject/1452107/' | 豆瓣
            td | 高屋建瓴. 本书在详述了语言细节的同时, 更加注重介绍如何使用C++做设计, 并且极力宣扬C++编程范式的多样性. 个人认为介绍标准库的部分可以跳过. 裘宗燕的中文版总体不错, 但是interface翻译成"界面"实在令人无法接受.
{% endshpaml %}

## Boost

至今看过的介绍Boost的书都不怎么样. 学习Boost的最好方法是看一下官方文档的quick start, 然后自己去用, 遇到问题Google一下, 实在不行了再去看书. 下面仅针对各个子库推荐相关教程和书籍.

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 子库
            th | 书籍/教程
    tbody
        tr
            td | ASIO
            td
                ul
                    li > a href='http://www.gamedev.net/blog/950/entry-2249317-a-guide-to-getting-started-with-boostasio/' | A guide to getting started with boost::asio
                    li
                        The Boost C++ Libraries
                        ul
                            li > a href='http://en.highscore.de/cpp/boost/index.html' | 英文版
                            li > a href='http://zh.highscore.de/cpp/boost/' | 中文版
        tr
            td | BGL(boost graph library)
            td > a href='http://book.douban.com/subject/1463103/' | The Boost Graph Library
{% endshpaml %}

## Git

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | Git使用指南
            td > a href='http://dl.answeror.com/u/3450602/git-tutor.pdf' | 下载
            td | 推荐它主要是因为它是中文的...
        tr
            td | Atlassian的Git教程
            td > a href='http://www.atlassian.com/git' | 详情
            td | 至今看过最简明最实用的Git教程.
{% endshpaml %}

## CMake

### 教程

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th | 备注
    tbody
        tr
            td > a href='http://dl.answeror.com/u/3450602/cmake-practice.pdf' | CMake指南
            td | 推荐它主要是因为它是中文的...
        tr
            td > a href='https://github.com/TheErk/CMake-tutorial' | CMake tutorial
            td | 一份CMake教学slides, 相当详细, 强烈推荐.
        tr
            td > a href='http://www.cmake.org/Wiki/CMake#Basic_Introductions' | 官方教程列表
            <td></td>
{% endshpaml %}

### 例子

学习CMake的最好方式是看例子和自己使用. 因为个人认为官方文档有很多地方没有覆盖到. 需要根据具体的应用采用各自的解决方案. 一般这些解决方案会分布在Stackoverflow和CMake的邮件刘表上. 总之是Google一下就能出来的东西. 还有一些解决方案会在某些开源项目的源码里出现, 比如debug和release同时做packaing的办法在OGRE里就有比较好的实现. 著名的使用CMake做构建的开源项目有OGRE, OpenCV, Blender等. 下面是一些具体的例子.

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th | 备注
    tbody
        tr
            td > a href='https://github.com/Answeror/yapimpl' | yapimpl
            td | 袖珍的PIMPL实现, 包含build, test和install步骤. 看不懂的地方邮件我.
{% endshpaml %}

## Python

### 学习资源

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th | 备注
    tbody
        tr
            td > a href='http://learnpythonthehardway.org/book/' | Learn Python the Hard Way
            td | 这是被广泛推荐的一本在线python教材, 官方没有提供免费的pdf, 英文. 对应的中文版有点过时. 除了书中"不建议初学者使用python3"的说法以外, 其它方面我认为都不错.
        tr
            td > a href='http://swaroopch.com/notes/python/' | A Byte of Python
            td | 该页面上有pdf下载地址和中文版. 我当时看这个入门的. 被很多大学作为Python教材.
        tr
            td > a href='http://pythonbooks.revolunet.com/' | Python Books
            td | 是个比较全面的Python免费教材/教程列表. 上述了两本书上面都有. 另外还有python版的数据结构与算法教材.
{% endshpaml %}

### 开发环境搭建

<del>我一般安装32位的Python `2.7.x`和`3.3.x`, `x`表示子版本号, (截至2013-09-09)最新版本是`2.7.5`和`3.3.2`, 在[官方网站](http://www.python.org/)有下载. **强烈建议**使用[npackd](https://code.google.com/p/windows-package-manager/)安装Python.</del>

<del>如果不需要大规模科学计算, 建议安装32位Python. 64位的需要了再装也不迟. 各版本和各地址空间(32/64)的Python可以共存.</del>

<del>Python的开发环境(IDE)建议使用[IPython notebook](http://ipython.org/). 如果使用过Python一段时间, 建议使用virtualenv和pip安装ipython. 如果是新手, 建议参考[这里](http://nbviewer.ipython.org/urls/raw.github.com/Answeror/python-course.2013/master/ex.0.ipynb)安装.</del>

<del>上述教程中用到的所有安装包均可在[这里](http://www.lfd.uci.edu/~gohlke/pythonlibs/)下载. GOW可以在[这里](https://github.com/bmatzelle/gow/downloads)下载.</del>

<del>如果使用Python3, ipython的命令行对应为ipython3, 而不是ipython. 如果嫌每次输入ipython/python的绝对路径麻烦, 可以参考[这里](http://nbviewer.ipython.org/urls/raw.github.com/Answeror/python-course.2013/master/devenv.ipynb)设置系统PATH环境变量.</del>

<del>上述链接里还包含了pip和virtualenv的安装和使用方法, 强烈建议用之.</del>

请无视上面的废话. 直接安装[Anaconda Python](http://continuum.io/downloads)即可. 你可以先安装Python2的Anaconda, 然后参考[这里](http://continuum.io/blog/anaconda-python-3)安装Python3环境. Anaconda的各个Python环境是相互隔离的, 相当于virtualenv. 其包管理机制类似于pip, 不同点是Anaconda从二进制安装.

IDE建议使用[PyCharm](https://www.jetbrains.com/pycharm/). 如果你熟悉Vim, 请无视这段话.

## OpenCV

### 推荐书籍

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | OpenCV 2 Computer Vision Application Programming Cookbook
            td > a href='http://book.douban.com/subject/6521022/' | 豆瓣
            td | 市面上唯一一本(截至2013-03-07)介绍OpenCV 2的书籍. OpenCV 1和2的API具有相当的差距. 个人<strong>不建议学习1的API</strong>.
        tr
            td | Mastering OpenCV with Practical Computer Vision Projects
            td > a href='http://book.douban.com/subject/20469441/' | 豆瓣
            td | 用一些比较前沿的视觉项目来介绍OpenCV的使用. 书中源代码参见<a href='https://github.com/MasteringOpenCV/code'>Github</a>.
{% endshpaml %}

## Qt

建议在Python里使用[PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/intro)或[PySide](http://qt-project.org/wiki/PySide)开发GUI程序. 熟悉Python的话一般两天可以上手. 如果有一点Qt基础则上手更快. 入门教程参见[这里](http://zetcode.com/tutorials/pyqt4/).

开发过程中可以使用Qt的API文档. 绝大多数接口与PyQt/PySide是一一对应的.

### 推荐书籍

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | C++ GUI Programming With Qt 4
            td > a href='http://book.douban.com/subject/2352059/' | 豆瓣
            td | 中文版名称: <em>C++ GUI Qt 4 编程</em>. 该书使用的Qt版本较老. 其中关于多线程的编程范式不推荐使用. 关于Qt多线程, 推荐阅读<a href='http://qt-project.org/wiki/Threads_Events_QObjects'>这里</a>.
{% endshpaml %}

## OpenGL

### 推荐教程

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | An Interactive Introduction to OpenGL Programming
            td > a href='http://dl.acm.org/citation.cfm?id=1281596' | dl.acm.org
            td | ACM SIGGRAPH 2007 course 10
        tr
            td | NeHe的OpenGL教程
            td > a href='http://nehe.gamedev.net/' | 作者主页
            td | 最有名的OpenGL教程. 中文版参见<a href='http://www.owlei.com/DancingWind/'>这里</a>.
{% endshpaml %}

## Latex

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th | 备注
    tbody
        tr
            td > a href='http://www.uncg.edu/cmp/reu/presentations/Charles%20Batts%20-%20Beamer%20Tutorial.pdf' | A Beamer Tutorial in Beamer
            td | 简明的Beamer教程
        tr
            td > a href='http://stackoverflow.com/questions/6188780/git-latex-workflow' | Git+Latex工作流程
            td | 核心内容: 论文写作的时候建议开一个advisor分支, 用于保存导师的意见. 并且维护一个自己的工作分支, 在必要的时候merge. 参考<a href='http://en.wikibooks.org/wiki/LaTeX/Basics#Big_Projects'>这里</a>, 将对论文的每个章节拆分到独立的文件里, 并使用独立的分支来撰写每个章节. 每次提交尽量保证逻辑上的完备, 方便回滚.
{% endshpaml %}

# 图形学

个人不建议自学. 可以考虑修研究生秋冬学期的"计算机图形学"课程(彭群生&冯结青), 以及冯结青老师的公选课"几何造型基础".

# 机器学习

## 推荐书籍

难度递增.

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | Pattern Classification
            td > a href='http://book.douban.com/subject/1788544/' | 豆瓣
            td | 中文版名为"模式分类", 翻译上乘, 价格便宜.
        tr
            td | Pattern Recognition And Machine Learning
            td > a href='http://book.douban.com/subject/2061116/' | 豆瓣
            td | 比Pattern Classification更前沿, 作者公开了<a href='http://research.microsoft.com/en-us/um/people/cmbishop/prml/'>电子版</a>.
{% endshpaml %}

# 计算机视觉

推荐书籍:

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | Computer Vision: Algorithms and Applications
            td > a href='http://szeliski.org/Book/' | 书籍主页
            td | 基本理论和前沿研究兼备.
        tr
            td | OpenCV相关书籍
            <td></td>
            td | 参见<a href='#opencv'>OpenCV</a>小节.
{% endshpaml %}

# 数值计算和优化方法

## 推荐手册/教程

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | The Matrix Cookbook
            td > a href='http://orion.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf' | 下载
            td | 囊括了绝大部分用得到的线性代数知识.
{% endshpaml %}

## 推荐书籍

{% shpaml %}
table class='top wide'
    thead
        tr
            th style='min-width:20em' | 名称
            th style='min-width:5em' | 详情
            th | 备注
    tbody
        tr
            td | Numerical Recipes: The Art of Scientific Computing
            td > a href='http://www.nr.com/' | 书籍主页
            td | 主要讲矩阵计算和优化方法的代码实现.
        tr
            td | Convex Optimization
            td > a href='http://book.douban.com/subject/1888111/' | 豆瓣
            <td></td>
{% endshpaml %}

# 数据库

建议快速开发时使用Sqlite. 小巧轻便.

## Sqlite

### 管理工具

[SQLite Administrator](http://sqliteadmin.orbmu2k.de).

### Python

建议快速开发时使用SQLAlchemy, 教程参见[这里](http://www.blog.pythonlibrary.org/2012/07/01/a-simple-sqlalchemy-0-7-0-8-tutorial/).

# 学术资源

## 重要期刊和会议

[中国计算机学会推荐国际刊物会议列表2012](http://dl.answeror.com/u/3450602/%E4%B8%AD%E5%9B%BD%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%AD%A6%E4%BC%9A%E6%8E%A8%E8%8D%90%E5%9B%BD%E9%99%85%E5%88%8A%E7%89%A9%E4%BC%9A%E8%AE%AE%E5%88%97%E8%A1%A82012.pdf)
