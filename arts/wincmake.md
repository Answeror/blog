title: Windows下的CMake碎碎念
date: 2013-06-15
json: true
lang: zh

<!--(」・ω・)」うー！(／・ω・)／にゃー！-->

CMake的官方文档乍看起来挺齐全, 实际上存在诸多死角. 许多零碎的知识需要从邮件列表和Stackoverflow里挖出来. 这里整理下我个人在Windows下使用CMake的经验. **注意**: 阅读本文需要CMake基础知识, 建议先阅读[CMake tutorial]的P1~84.

# 概述

\begin{tikzpicture}[
        sbase/.style={
                    % The shape:
            rectangle,
                    % The size:
            minimum size=2mm,
            minimum width=1.5cm,
                    % The border:
            thick,
            draw=black!50!black!50,
                    % 50% red and 50% black,
                    % and that mixed with 50% white
                    % The filling:
            top color=white,
            color=black,
                    % a shading that is white at the top...
            bottom color=red!80!black!20, % and something else at the bottom
                    % Font
        font=\itshape\scriptsize},
        scompiled/.style={sbase,
            node distance=1cm and 1cm,
            bottom color=green!70!black!20, % and something else at the bottom
        },
        sinterpreted/.style={sbase,
            node distance=1cm and 1cm,
            bottom color=orange!70!black!20, % and something else at the bottom
        },
        stools/.style={sbase,
            rectangle,
            minimum width=0cm,
            bottom color=blue!80!black!20,
            font=\slshape\scriptsize
        }
    ]
    \tikzstyle{boitearrondie} = [draw,
        dashed,
        opacity=.2,
        fill=blue!20,
        rounded corners
    ]
    \node [sinterpreted] (python)  {Python};
    \node [sinterpreted, below=0cm of python] (perl)    {Perl};
    \node [sinterpreted, below=0cm of perl] (ocaml)    {OCaml};
    \node [fit={(python) (perl) (ocaml)}] (interp) {};
    \node [scompiled, below=4.2mm of ocaml]    (cxx)     {C++};
    \node [scompiled, below=0cm of cxx]    (fortran) {Fortran};
    \node [scompiled, below=0cm of fortran]    (c) {C};
    \node [fit={(cxx) (fortran) (c)}] (lcompil) {};
    \node [fit={(interp) (lcompil)}] (dummy) {};
    \node at (dummy.west) [sbase, rotate=90, above, minimum width=3.5cm] (language) {Programming languages};
    \node[stools, above right=0cm and 3.5cm of interp.west] (interpreter) {interpreter};
    \node[stools, below right=0cm and 1.5cm of lcompil.south east, rotate=90] (object) {object code};
    \node[stools, below right=0cm and 1.5 cm of object.south west, rotate=90] (executable) {executable};
    \node[stools, minimum height=2cm, right=0 cm and 2 cm of executable.south east ] (running) {Running program};
    \draw [->,thick] (interp.east) -- (interpreter.west) node[above,midway,font=\tiny] {?byte-compile?};
    \draw [->,thick] (interpreter.east) -- (running.west) node[above,midway,font=\tiny] {interprets} ;
    \draw [->,thick] (lcompil.east) -- (object.north) node[above,midway,font=\tiny] {compiles};
    \draw [->,thick] (object.south) -- (executable.north) node[above,midway,font=\tiny] {links};
    \draw [->,thick] (executable.south) -- (running.west) node[above,midway,font=\tiny] {executes};
    \begin{pgfonlayer}{background}
        \draw [boitearrondie,top color=blue,bottom color=green,middle color=red] ([xshift=0.05cm]language.south) rectangle ([xshift=0.1cm,yshift=-0.7cm]running.south east);
        \node [color=accent, below=0cm of running.south] {CMake};
    \end{pgfonlayer}
\end{tikzpicture}

构建系统(build system)是一套用于生成软件的工具链, 我们通常使用的Visual Studio, make等都可以称为构建系统. 使用同一种编程语言, 在不同的操作系统上通常需要不同的构建系统来编译和链接. 解释型语言一般不关构建系统的事, 所以CMake一般用来做C/C++之类的项目, 反正我只用它弄过C++, 顶多再加个Python接口. 当然构建系统并不仅限于做编译和链接. CMake是个构建系统的**生成器**, 它本身并不参与构建(这样说并不准确, 因为构建系统还可以反过来调用CMake来实现一些功能, 比如后文提到的`add_custom_command`, 请自行`CTRL+F`). 我们可以根据操作系统以及目标平台(交叉编译)的需要来选择生成合适的构建系统的配置文件. 所谓配置文件, 对于make来说就是`makefile`, 对于VS来说就是`.sln`, `.vsproj`和`.vsxproj`.

使用CMake做构建, 一般包含CMake, build, install和CPack这4个阶段. 其中我一般只用到前3个. 另外单元测试(test)也可以算作一个阶段, 在build之后, install之前.

\begin{tikzpicture}[
        sbase/.style={      % The shape:
            rectangle,
                    % The size:
            minimum size=2mm,
            minimum width=2.0cm,
            minimum width=0.5cm,
                    % The border:
            thick,
            draw=black!50!black!50,
                    % 50% red and 50% black,
                    % and that mixed with 50% white
                    % The filling:
            top color=white,
            color=black,
                    % a shading that is white at the top...
            bottom color=red!80!black!20, % and something else at the bottom
                    % Font
            font=\itshape\scriptsize
        }
    ]
    \tikzstyle{edited} = [
        sbase,
        draw,
        bottom color=green!80!black!20,
                      %opacity=.5,
                      %fill=green!20,
        rounded corners
    ]
    \tikzstyle{generated} = [
        sbase,
        draw,
                      %dashed,
        bottom color=red!80!black!20,
                      %opacity=.5,
                      %fill=green!20,
        rounded corners
    ]
    \tikzstyle{installed} = [
        sbase,
        draw,
        bottom color=blue!80!black!20,
                      %opacity=.5,
                      %fill=green!20,
        rounded corners
    ]
    \tikzstyle{pkg} = [
        installed,
        dashed,
        general shadow={fill=blue!60!black!40,shadow scale=1.05,shadow xshift=+2pt,shadow yshift=-2pt}
    ]
    \node[edited] (cmakelists) {CMakeLists.txt};
    \node[edited,below=1cm and 0cm of cmakelists.south] (sourcefiles) {Source files};
    \node[generated,right=0cm and 1.5cm of cmakelists.east] (projectfiles) {Project file(s), Makefiles, \ldots};
    \node[generated,below right=2cm and 1.5cm of cmakelists.east] (gensourcefiles) {Generated Sources files};
    \node[generated,right=0cm and 1.5cm of projectfiles.east] (objectfiles)  {Object files};
    \node[pkg, below left=1.7cm and 0cm of sourcefiles.south] (spackage) {Source package};
    \node[above right=0.5cm and 2.0cm of spackage.east] (legendL){};
    \node[right=0cm and 2.3cm of legendL.east] (legendR){};
    \node[pkg, below right=-1.5cm and 7cm of spackage.east] (bpackage) {Binary package};
    \node[installed, below=0.7cm and 0cm of bpackage.south] (ipackage) {Installed package};
    \node[installed, above=0.7cm and 0cm of bpackage.north] (binstalled) {Installed files};
    \tikzstyle{cmaketime} = [-latex,thick,color=solarizedGreen]
    \tikzstyle{buildtime} = [-latex,thick,color=solarizedRed]
    \tikzstyle{installtime} = [-latex,thick,color=solarizedCyan]
    \tikzstyle{cpacktime} = [-latex,thick,color=solarizedBlue]
    \tikzstyle{packageinstalltime} = [-latex,thick,color=solarizedMagenta,dashed]
    \draw [cmaketime]           ([yshift=0.0cm]legendL.south) -- ([yshift=0.0cm]legendR.south)  node[above=-2pt,midway,font=\tiny] {CMake time};
    \draw [buildtime]          ([yshift=-0.5cm]legendL.south) -- ([yshift=-0.5cm]legendR.south) node[above=-2pt,midway,font=\tiny] {Build time};
    \draw [installtime]        ([yshift=-1.0cm]legendL.south) -- ([yshift=-1.0cm]legendR.south) node[above=-2pt,midway,font=\tiny] {Install time};
    \draw [cpacktime]          ([yshift=-1.5cm]legendL.south) -- ([yshift=-1.5cm]legendR.south) node[above=-2pt,midway,font=\tiny] {CPack time};
    \draw [packageinstalltime] ([yshift=-2.0cm]legendL.south) -- ([yshift=-2.0cm]legendR.south) node[above=-2pt,midway,font=\tiny] {Package Install time};
    \begin{pgfonlayer}{background}
        \draw [cmaketime] (cmakelists) -- (projectfiles);
        \draw [cmaketime] (cmakelists) -- (gensourcefiles);
        \draw [cmaketime] (sourcefiles) -- (gensourcefiles);
        \draw [cpacktime] (cmakelists) -- (spackage);
        \draw [cpacktime] (sourcefiles) -- (spackage);
        \draw [cpacktime] ([xshift=-0.2cm]binstalled.south) -- ([xshift=-0.2cm]bpackage.north);
        \draw [buildtime] (sourcefiles) -- (objectfiles);
        \draw [buildtime] (gensourcefiles) -- (objectfiles);
        \draw [buildtime] (projectfiles) -- (gensourcefiles);
        \draw [installtime] (objectfiles) -- (binstalled);
        \draw [installtime] (gensourcefiles) -- (binstalled);
        \draw [installtime] (sourcefiles) -- (binstalled);
        \draw [packageinstalltime] (bpackage.south) -- (ipackage.north);
    \end{pgfonlayer}
\end{tikzpicture}

# 学习资料

## 资源列表

参见[研究指南].

## 官方文档

使用`--help-command`和`--help-variable`参数可以获取针对特定命令和变量的帮助文档.

```bash
cmake --help-command add_executable
cmake --help-variable CMAKE_INSTALL_PREFIX
```

![](http://dl.answeror.com/u/3450602/cmake-help-command.console.png)

Vim里可以使用[cmakecomplete](https://github.com/Answeror/cmakecomplete)插件.

![](http://dl.answeror.com/u/3450602/cmake-help-command.vim.png)

# 外部依赖

C/C++项目的外部依赖我一般按照规模分为两种. 其处理方式截然不同. 所谓规模大小指其构建所需的时间.

## 小型库

第一类小型库即纯文本. 例如只包含头文件的库[p-stade]和[CML], 以及CMake模块[acmake]等. 这种库最容易处理. 按照其版本控制工具, 有两种处理方式:

* 对于有Git版本库的, 作为submodule, 放在`/3rd`目录下.
* 否则直接拷贝到`/3rd`并纳入版本控制.

第二类小型库是需要编译的. 例如[ALGLIB]和[levmar]. 根据其版本控制工具和构建工具, 有如下处理方式:

* 具有版本控制, 并且可以自动(比如使用了CMake, qmake, make等)构建的, 可以使用ExternalProject模块自动下载和构建.
* 对于无法自动构建的:
    * 可以参照纯文本库作为submodule或者拷贝过来, 然后自己写个`CMakeLists.txt`来构建.
    * 对于十份稳定且库文件较小的, 可以直接拷贝其头文件和编译好的库文件, 一起纳入版本库.

## 大型库

这种库一般动辄需要编译几十分钟甚至几个小时, 比如我常用的[Boost], [Qt], [OGRE]等. 无论它是不是能自动构建, 我都不喜欢把它直接纳入版本控制. 当然这对于CI是很不友好的. 一种可能的方案是在工程内部, 根据是否提供了编译好的大型库来决定是否使用ExternalProject.

大型库我一般统一放在一个目录下, 使用平坦的文件结构, 即不同版本和参数配置的同一个库放在统一目录下, 以后缀区分.

![](http://dl.answeror.com/u/3450602/sdk.png)

注意:

* 后缀尽可能包含完整的信息.

    以`ogre.1-8-1.msvc11.boost.1-51-0`为例, 其中包含了:

    1. 版本号: `1.8.1`.
    2. 编译器: msvc11.
    3. 依赖的[Boost]版本号: `1.51.0`.

    当然[Boost]本身还有很多编译参数, 比如库本身动态/静态, 依赖的C运行时库动态/静态, 多线程/单线程. 因为我的[Boost]统一使用动态库, 动态多线程C运行时, 所以没这个问题.

* 区分源码目录和安装目录.
    
    安装目录通常是`make install`, `nmake install`或者VS的INSTALL工程生成的. 一般具有固定的目录结构(`include`, `lib`, `bin`).

在项目里引用这些库的时候建议采用统一的, 系统环境变量无关的方式. 某些库的find模块(例如[Qt]), (可选地)依赖某些特定的系统环境变量(`QTDIR`); 此外采用config模块进行查找的库(例如OpenCV), 可以通过设置系统环境变量(`OpenCV_DIR`)来定位config模块. 这些环境变量对于合作开发是非常不利的. 甚至对于单人开发, 如果没有合适的系统环境变量管理和备份软件(例如[RapidEE](http://www.rapidee.com/en/about)), 想要重现历史版本都会很困难. 建议对于非依赖环境变量不可的情况, 应将环境变量导出成`reg`文件纳入版本控制.

建议的方法是统一采用形如`XXX_HOME`的CMake变量保存大型库的根目录, 然后将其从命令行传给`cmake`, 并将`cmake`命令写入`bat`文件纳入版本控制. 一个典型的`conf.bat`如下:

```batch
@echo off
pushd %~dp0
set ROOT=%cd%
popd
@echo on
cmake %ROOT% ^
    -DQT_HOME=C:\sdk\qt.4-8-3.msvc11 ^
    -DBOOST_HOME=C:\sdk\boost.1-51-0.msvc11 ^
    -DOGRE_HOME=C:\sdk\ogre.1-8-1.msvc11.boost.1-51-0 ^
    -DOgreProcedural_HOME=C:\sdk\ogre-procedural.0-2.ogre.1-8-1.boost.1-51-0 ^
    -DROC_HOME=C:\sdk\roc.msvc11.boost.1-51-0.bullet.2-80 ^
    -DBULLET_HOME=C:\sdk\bullet.2-80-r2531.msvc11 ^
    -DCML_HOME=C:\sdk\cml.1-0-3 ^
    -DGRAPHVIZ_HOME="C:\Program Files (x86)\Graphviz" ^
    %*
```

其使用方法如下:

```batch
mkdir build.debug
cd build.debug
..\conf -G"NMake Makefiles" -DCMAKE_BUILD_TYPE=Debug
nmake
```

在工程的CMake配置里, 通过将`XXX_HOME`的内容加入到`CMAKE_PREFIX_PATH`里, 并且赋值给`XXX_DIR`(其中`XXX`的大小写需要注意)就可以让大多数find或config模块工作起来. 另外某些库可以通过特定的CMake变量进行查找, 例如[Boost]就可以使用`BOOST_ROOT`, 同样赋以该值即可. 如果使用了[acmake], 可以用下述命令简化该过程:

```cmake
include(acmake_use_home) # include only once
acmake_use_home(XXX)
```

对于满足find模块[约定写法](http://www.vtk.org/Wiki/CMake:How_To_Find_Libraries#Writing_find_modules)(具有`XXX_LIBRARIES`, `XXX_INCLUDE_DIRS`)的库, 可以用[acmake]简化引用过程:

```cmake
include(acmake_simple_support) # include only once
acmake_simple_support(${TARGET})
```

其中变量`TARGET`内保存了目标名.

某些配置较为复杂的库(例如[Boost]和[Qt]), 需要在`find_package`之前定义额外的变量来控制`find_package`的行为, 或者需要库提供的代码生成器动态生成源码. 在[acmake]里我针对几个经常用到的库写了额外的`acmake_xxx_support`宏. 其定义均有如下结构:

```text
acmake_xxx_support(TARGET [COPY_SHARED] [COMPONENTS <comp1> <comp2> ...])
```

其中`acmake_qt_support`在内部

1. 递归查找`CMAKE_CURRENT_SOURCE_DIR`目录下的所有头文件, UI文件, 资源文件;
2. 调用[Qt]的代码生成器生成对应的moc文件;
3. 创建`${TARGET}_moc`目标(静态库)并连接至`${TARGET}`.

更加详细的配置参见[acmake]的文档(虽然现在根本就没有文档... bgm38).

# 构建类型

构建类型(build type)翻译过来感觉怪怪的, 叫做"配置"的话又感觉太笼统. 在CMake里有个`CMAKE_BUILD_TYPE`变量, 而在VS里这个叫做"configuration", 指的都是一套预定义的编译和链接参数. 我们通常用到的就是`Debug`和`Release`两种(注意大小写). 其它的预定义配置有`RelWithDebInfo`和`MinSizeRel`. 其中`Release`, `RelWithDebInfo`以及`MinSizeRel`是一类. 在这3种配置下, `target_link_libraries`链接进去的库会使用`optimized`版本, 否则就使用`debug`版本. 即:

```cmake
target_link_libraries(${TARGET} debug foo optimized foo_d bar)
```

在`Debug`配置下会链接`foo`和`bar`; 而在另外3种配置下则会链接`foo_d`和`bar`. 注意这里`debug`和`optimized`关键字只对后面紧跟的一个名字有效.

但是`CMAKE_BUILD_TYPE`在使用基于make的构建系统的生成器时才有定义, nmake当然也包含在内. 也就是说, 在使用这类构建系统时:

1. 在CMake阶段, 就可以确定构建类型.
2. 一个build tree只能构建一种构建类型下的工程.

而其它构建系统(也就是具有IDE的构建系统, 例如Visual Studio和Eclipse), 则正好相反:

1. 在CMake阶段, `CMAKE_BUILD_TYPE`没有定义, 相应的, 任何具有`_DEBUG`, `_RELEASE`等后缀的CMake变量也没有定义.
2. 一个build tree可以构建多种构建类型下的工程. 生成文件通常位于`debug`和`release`(首字母可能是大写)子目录下.

基于make的构建系统在CMake阶段就能根据构建类型链接合适的库, 拷贝对应的dll, 配置文件和资源文件到可执行程序目录(用于运行程序或单元测试); 其代价是在程序打包时会遇到麻烦, 可能需要创建多个build tree, 各自构建, 再一起打包. 而具有IDE的构建系统在打包时则轻松许多, 但在需要根据构建类型来动态配置的场合就会特别麻烦. 一种解决方案是使用`add_custom_target`, `add_custom_command`和`add_test`自带的"generator expression"让依赖于构建类型行为延迟到build阶段. 如果这些依赖于构建类型行为较为复杂, 就可以将其放进独立的`.cmake`文件中, 然后通过`cmake -P`来在build阶段调用. 那些依赖CMake阶段的CMake变量的`.cmake`文件, 可以通过`configure_file`命令来生成. 具体的例子参见`acmake_copy_dependencies`的[实现](https://github.com/Answeror/ACMake/blob/master/acmake_copy_dependencies.cmake).

一般来说, 在Windows下开发, 使用Visual Studio Generator就足够了. 但是nmake有个巨大的好处是可以显示构建进度, 这在构建大型项目时是个很好的心理安慰.

![](http://dl.answeror.com/u/3450602/progress.png)

所以我通常的开发模式是建立3棵build tree:

1. `/build.debug`
2. `/build.release`
3. `/build.vs`

其中1用来运行单元测试, 2用来运行算法测试(即跑实验), 3用来调试和打包.

为了缓解build阶段不同构建系统调用方式的差异(make, nmake, msbuild, devenv...), CMake提供了一个统一的方式来build:

```text
cmake --build . --target <target name> --config <build type>
```

这样一来上述的所有阶段(cmake, build, test, install, pack)都可以在命令行中完成. 换句话说就是可以自动化. 当然, `--config`参数对于基于make的构建系统来说是没用的, 因为它们在CMake阶段就已经确定构建类型了.

在支持多种构建系统时, 需要特别注意尽可能不要在CMake阶段依赖构建类型, 而应当将所有依赖放到build阶段中去. 对于不得不在CMake阶段做的事... 暂时还没发现这样的事情...

# 单元测试

单元测试遵循下述原则:

* 测试数据纳入版本库.
* 测试数据与测试代码处于同一, 或相邻的目录.
* 不同目录中的单元测试, 用到的同一份测试数据需分别拷贝到各自的源码目录[^storage].
* 单元测试的工作目录应与源码目录分离. 即中间文件不应写入源码目录.

[^storage]: Git会自动处理相同文件, 不会在版本库中占用额外存储.

C++端单元测试采用[Boost.Test]和[CTest]. 其目录结构为:

```text
/root-path/
    CMakeLists.txt
    some-module/
        CMakeLists.txt
        include/
        src/
        test/
            CMakeLists.txt
            config.hpp
            config.cpp.in
            config.info.in
            some-test-data.dat
            test_foo.cpp
    another-module/
        CMakeLists.txt
        include/
        src/
        test/
            CMakeLists.txt
            some-test-data.dat
            test_bar.cpp
```

其中`config.cpp.in`包含配置文件(例如`config.info`)的绝对路径等信息的占位符, 由CMake的`configure_file`命令生成`config.cpp`到`CMAKE_CURRENT_BINARY_DIR`. `config.info.in`包含数据/模型文件(例如`some-test-data.dat`)的绝对路径等信息的占位符, 同样由`configure_file`生成`config.info`到`CMAKE_CURRENT_BINARY_DIR`.

## 调试

> Debugging is evil. <!--我说的 :P-->

我发现很多时候, 拥有一个好用的调试工具是写单元测试最大的阻碍. 所以在不是万不得已的情况下, 我会避免去碰`/build.vs`目录. 但是有些原子性的单元测试也挂掉的时候, 调试器就变成"必要之恶"了. 尤其是遇到没有stack trace的断言错误(建议在`/build.debug`下做单元测试就是这个原因, 否则可能连断言错误都不会触发, 默不作声<!--I thought what I'd do was, I'd pretend I was one of those deaf-mutes.-->才是最糟糕的)或异常, 特别是第三方库中的断言, 例如OpenCV的矩阵操作中的断言(因为做了类型擦除, 元素类型和通道个数的检查都推迟到了运行时, 很容易出错). 这种时候与其不停地插桩调试输出, 不如直接祭出VS. 在使用Boost.Test时, 通常诸如断言失败, 内存访问禁止等严重错误会导致单元测试直接停止. 加入`--catch_system_errors=0`(注意不是给`ctest`, 而是给单个的测试程序)之后就会像普通程序一样崩溃掉. 然后等一会在弹出窗口中点"Retry", 就可以调用VS的调试工具了.

## 其它

本文中两幅SVG图片修改<!--移植到markdown里好辛苦-->自[CMake tutorial].

[CML]: http://cmldev.net/
[acmake]: https://github.com/Answeror/ACMake
[p-stade]: https://github.com/himura/p-stade
[ALGLIB]: http://www.alglib.net/
[levmar]: http://users.ics.forth.gr/~lourakis/levmar/
[Boost]: http://www.boost.org/
[Qt]: http://qt-project.org/
[OGRE]: http://www.ogre3d.org/
[Boost.Test]: http://www.boost.org/libs/test/
[CTest]: http://cmake.org/Wiki/CMake/Testing_With_CTest
[研究指南]: http://answeror.com/research-guide.html#cmake
[CMake tutorial]: https://github.com/TheErk/CMake-tutorial
