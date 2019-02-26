# python-csv-handler-tkinter
a simple python program, used to process specific csv files. Use tkinter to implement GUI

这是一个用于处理特定格式csv文件的程序。代码完成时间比较早，逻辑简单，但优雅不足。使用tkinter来实现GUI。 会在WIKI页面说明工具的使用方法，工具实现的大体流程，以及一些需要注意的点（如错误处理部分）。

下面是在实现程序中记录的一些问题点：

（1）文件读取，如果使用with，要确保所写逻辑代码缩进正确，位于with语句块内。
    如果使用with无法满足要求，改成open & close的普通类型。
（2）csv文件写入，使用writerows与writerow是有差异的，注意传入参数类型的差别。
     如果使用writerows，需要构造list[list]参数。根据需要使用append或者extend。
     当前我使用穷举所需Item的方式，为每个Item定义了一个List变量，全部都使用了append。
（3）写csv文件的时候，根据需要定制自己的文件内容格式，如添加项目栏名称，将数据输出到一行或者一列，不同项目数据之间用空行隔开。
（4）实际项目过程中，发现csv文件类似纯文本格式文件，无法控制行宽，列宽。只有按照其他方式，
    将数据写入到excel文件中时，才能指定格式（如列宽）。
（5）float数据，按照指定位宽进行保存和输出。关于输出，可以继续看做字符串，类似"%.1f" % str
     的格式，就可以实现。关于保存，暂时没有很合适的方法。网上提到了三种方法：
	 （5-1）round(a,2) ： 不是完全的四舍五入，但类似。存在“保存的数据与预期不符”的问题。
	 （5-2）"%.2f" % a ： 属于字符串，不是按照数值保存，无法用来进行计算。
	 （5-3）Decimal    ： 未使用过，不知道。
	 （5-4）麻烦的办法 ： 自己写一个str2float的函数，实现格式控制，但不确定是否会受到float
	                      类型默认小数位数（如6位）的影响。
（6）使用page.tcl工具生成的tkinter gui的python代码，需要进行微小幅度的修改，才能编译通过，运行。
（7）运行page.tcl可视化GUI工具生成的代码，看到的GUI可能与page.tcl里面看到的略微不同，如组件大小，位置。
     可能需要根据需要进行调整。
（8）在page.tcl里面编辑text或者title时，可以使用中文。但是直接在python环境下运行程序，会看到乱码。需要
     使用utf-8做编解码处理：Labelframe01_Color.configure(text="色彩测试".encode('utf8').decode('utf8'))

