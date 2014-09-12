title: Clang Complete
date: 2013-01-29

最近因为VAssitX的补全与VS自带补全在include头文件的时候会冲突, 于是把VAssistX卸载了. 然后感觉VS各种不好用. 特别是切换tab的时候, 不能搜索. 于是想用vim开发C++了.

约定俗成的标准大概是OmniComplete和Ctags. 要补全第三方库就需要手动对第三方库做ctags. 据说Qt做ctags的结果有1个多G... 搜到两篇blog, 提到了[clang complete](https://github.com/Rip-Rip/clang_complete)这个插件. 原理就是用clang来做语法分析. 然后根据语法树来做补全. 据说gcc也有类似的插件, 不过貌似不太好用.

配置[这里](http://blog.misakamm.org/p/282)讲得比较详细. 其实就两步:

1. 下载`libclang.dll`.
2. 安装插件.

插件可以用`vundle`安装. 那个dll, 文章中给出的[下载链接](http://sourceforge.net/projects/tcgraphics/files/others/libclang.zip/download)是可以用的, 但是版本比较老, 不支持读取`compile_commands.json`文件. [这里](http://www.ishani.org/web/articles/code/clang-win32/)有最新的二进制包.

安装以后在工程根目录(vim的当前目录)定义`.clang_complete`文件, 里面包含形如`-IXXX`的行, `XXX`是一个头文件路径. 的确可用. 但是同时有多个工程就不好手工配了.

这个插件自带了一个`cc_args.py`文件, 可以用来配合make生成`.clang_complete`文件. 但是不知道要怎么跟cmake配合起来. [这里](http://stackoverflow.com/questions/13484622/clang-complete-cc-args-py-wont-generate-clang-complete-file)说了linux下的跟make配合的方法.

[这里](https://github.com/Rip-Rip/clang_complete/pull/148)有个pull request说是利用了cmake的`CMAKE_EXPORT_COMPILE_COMMANDS`选项导出`compile_commands.json`文件, 该文件里包含了每个源文件(cpp)对应的编译指令. 然后在vim插件里面用python解析这个json, 再设置`b:clang_auto_user_options`为对应的参数就可以针对每个文件做特定的补全了. 刚开始没试这个方法.

然后看了[这里](http://scitools.com/blog/2012/04/cmake-and-understand.html)说怎么使用`CMAKE_EXPORT_COMPILE_COMMANDS`选项的, 设置成`ON`即可.

然后在插件内置的帮助文档里发现设置`g:clang_auto_user_options`为`compile_commands.json`就可以读取json文件了. 并且这个特性已经被merge到主分支上了. 但是用了发现不行.

然后试用了上面的未被采纳的pull request, 报错说:

> module use of python32.dll conflicts with this version of python

在ctypes的地方出错了. 以为是Python3的问题, 于是把everything搜索到的所有相关的`python32.dll`都删掉了. `PATH`也清理并重启了. 还是不行. 然后查看vim的python文档, 没太看懂, 貌似是python2和python3混用的时候有啥问题. 于是把vimrc里所有python3写的代码全注释掉, 还是不行. 最后把everything搜索到的所有相关的`python27.dll`也删掉了, 报错说:

> vim could not load library python27.dll

在控制台用python2和python3手动加载ctypes, 没错. 然后在[善用佳软](http://xbeta.info/vim-voof.htm)介绍voom的文章里看到安装python环境的说法, 没说要拷贝`python27.dll`到vim目录里去. 于是重装了python27. 好了... 大概是注册表什么的缘故吧. 以前安装的python也许是EPD的? 很久远, 想不起来了. 顺便把python32也重装了.

这个错误消失后发现里面python调用的地方读取json出错了. 查看它的[源码](https://github.com/dave-h/clang_complete/blob/586dffb86ff5c6f25ff9b0324cd24f2fe489e431/autoload/getopts/compile_commands.vim), 依样画葫芦在python27里读取json, 依然不行, python32里也不行. 说是字符127非法. 搜了, 在stackoverflow上说是`\r`的问题. 然后打开json发现有些奇怪的字符`@<<`和`<<`被加到编译指令里了. 看了[clang](http://clang.llvm.org/docs/JSONCompilationDatabase.html)对这个json格式的说明, 发现只说了gcc和clang可用, 没有提到msvc. 于是把跟`libclang.dll`一起下载下来的`clang.exe`作为编译器重新nmake了. 生成的json还是不行. 仍然有这些奇怪的字符.

然后在[这里](http://lists.cs.uiuc.edu/pipermail/cfe-dev/2012-October/025169.html)发现有人提了相似的问题. 说是把说箭头去掉, 再把反斜杠改成顺斜杠就好了. 后面有回复说clang的这个特性现在还不支持windows...

于是手动改了插件源码, 好用了.

插件内置文档说, 如果配置文件更新了. 需要重新加载buffer才能更新补全. 但是发现[这里](http://vim.1045645.n5.nabble.com/Refresh-reload-an-opened-file-td1187419.html)说的用`:e!`命令重新加载不好用. 倒是用`SaveSession`然后`OpenSession`可以.
