常用的linux命令
##https://blog.csdn.net/ljianhui/article/details/11100625
前言：基本参照上面的博文，一些已经知道的就去掉了
1. ls命令
	-l ：列出长数据串，包含文件的属性与权限数据等  
	-a ：列出全部的文件，连同隐藏文件（开头为.的文件）一起列出来（常用）  
	-d ：仅列出目录本身，而不是列出目录的文件数据  
	-h ：将文件容量以较易读的方式（GB，kB等）列出来  
	-R ：连同子目录的内容一起列出（递归列出），等于该目录下的所有文件都会显示出来

2. 查看文件内容： 
	cat 从上至下查看文件内容 （-n/显示行号）
	tac 从下至上查看文件内容
	tail 查看文件尾部几行 （-f/循环读取，-n/显示行号）常用来查询日志

3. grep命令
	该命令常用于分析一行的信息，若当中有我们所需要的信息，就将该行显示出来，该命令通常与管道命令一起使用，用于对一些命令的输出进行筛选加工等等
	它的简单语法为grep [-acinv] [--color=auto] '查找字符串' filename 
	参数：	
		-a ：将binary文件以text文件的方式查找数据  
		-c ：计算找到‘查找字符串’的次数  
		-i ：忽略大小写的区别，即把大小写视为相同  
		-v ：反向选择，即显示出没有‘查找字符串’内容的那一行  
		# 例如：  
		# 取出文件/etc/man.config中包含MANPATH的行，并把找到的关键字加上颜色  
		grep --color=auto 'MANPATH' /etc/man.config  
		# 把ls -l的输出中包含字母file（不区分大小写）的内容输出  
		ls -l | grep -i file
4. find命令
	find是一个基于查找的功能非常强大的命令，相对而言，它的使用也相对较为复杂，参数也比较多，所以在这里将给把它们分类列出
	它的基本语法如下：
	find [PATH] [option] [action]  
		# 与时间有关的参数：  
		-mtime n : n为数字，意思为在n天之前的“一天内”被更改过的文件；  
		-mtime +n : 列出在n天之前（不含n天本身）被更改过的文件名；  
		-mtime -n : 列出在n天之内（含n天本身）被更改过的文件名；  
		-newer file : 列出比file还要新的文件名  
		# 例如：  
		find /root -mtime 0 # 在当前目录下查找今天之内有改动的文件    
		# 与用户或用户组名有关的参数：  
		-user name : 列出文件所有者为name的文件  
		-group name : 列出文件所属用户组为name的文件  
		-uid n : 列出文件所有者为用户ID为n的文件  
		-gid n : 列出文件所属用户组为用户组ID为n的文件  
		# 例如：  
		find /home/ljianhui -user ljianhui # 在目录/home/ljianhui中找出所有者为ljianhui的文件  
		# 与文件权限及名称有关的参数：  
		-name filename ：找出文件名为filename的文件  
		-size [+-]SIZE ：找出比SIZE还要大（+）或小（-）的文件  
		-tpye TYPE ：查找文件的类型为TYPE的文件，TYPE的值主要有：一般文件（f)、设备文件（b、c）、  
		             目录（d）、连接文件（l）、socket（s）、FIFO管道文件（p）；  
		-perm mode ：查找文件权限刚好等于mode的文件，mode用数字表示，如0755；  
		-perm -mode ：查找文件权限必须要全部包括mode权限的文件，mode用数字表示  
		-perm +mode ：查找文件权限包含任一mode的权限的文件，mode用数字表示  
		# 例如：  
		find / -name passwd # 查找文件名为passwd的文件  
		find . -perm 0755 # 查找当前目录中文件权限的0755的文件  
		find . -size +12k # 查找当前目录中大于12KB的文件，注意c表示byte  
5. cp命令
	-a ：将文件的特性一起复制  
	-p ：连同文件的属性一起复制，而非使用默认方式，与-a相似，常用于备份  
	-i ：若目标文件已经存在时，在覆盖时会先询问操作的进行  
	-r ：递归持续复制，用于目录的复制行为  
	-u ：目标文件与源文件有差异时才会复制  
	举例：
	cp -a file1 file2 #连同文件的所有特性把文件file1复制成文件file2  
	cp file1 file2 file3 dir #把文件file1、file2、file3复制到目录dir中 
6. mv命令
	该命令可以把一个文件或多个文件一次移动一个文件夹中，但是最后一个目标文件一定要是“目录”
	-f ：force强制的意思，如果目标文件已经存在，不会询问而直接覆盖  
	-i ：若目标文件已经存在，就会询问是否覆盖  
	-u ：若目标文件已经存在，且比目标文件新，才会更新
	举例：
	mv file1 file2 file3 dir # 把文件file1、file2、file3移动到目录dir中  
	mv file1 file2 # 把文件file1重命名为file2 
7. rm命令
	-f ：就是force的意思，忽略不存在的文件，不会出现警告消息  
	-i ：互动模式，在删除前会询问用户是否操作  
	-r ：递归删除，最常用于目录删除，它是一个非常危险的参数 
	举例：
	rm -i file # 删除文件file，在删除之前会询问是否进行该操作  
	rm -fr dir # 强制删除目录dir中的所有文件  
8. ps命令
	该命令用于将某个时间点的进程运行情况选取下来并输出，process之意
	-A ：所有的进程均显示出来  
	-a ：不与terminal有关的所有进程  
	-u ：有效用户的相关进程  
	-x ：一般与a参数一起使用，可列出较完整的信息  
	-l ：较长，较详细地将PID的信息列出  
	常用的：
	ps aux # 查看系统所有的进程数据  
	ps ax # 查看不与terminal有关的所有进程  
	ps -lA # 查看系统所有的进程数据  
	ps axjf # 查看连同一部分进程树状态  
9. time命令
	该命令用于测算一个命令（即程序）的执行时间。它的使用非常简单，就像平时输入命令一样，不过在命令的前面加入一个time即可

10. ./configure --prefix=/usr/local/目录 
	Configure是一个可执行脚本，它有很多选项，在待安装的源码路径下使用命令./configure –help输出详细的选项列表。
	其中--prefix选项是配置安装的路径，如果不配置该选项，安装后可执行文件默认放在/usr /local/bin，库文件默认放在/usr/local/lib，配置文件默认放在/usr/local/etc，其它的资源文件放在/usr /local/share，比较凌乱。
	如果配置--prefix可以把所有资源文件放在/usr/local/test的路径中，不会杂乱，用了—prefix选项的另一个好处是卸载软件或移植软件。当某个安装的软件不再需要时，只须简单的删除该安装目录，就可以把软件卸载得干干净净；移植软件只需拷贝整个目录到另外一个机器即可

11. service命令：
service命令是Redhat Linux兼容的发行版中用来控制系统服务的实用工具，它以启动、停止、重新启动和关闭系统服务，还可以显示所有系统服务的当前状态
	语法：service(选项)(参数)
	选项值：-h：显示帮助信息；--status-all：显示所服务的状态
	参数：
		服务名：自动要控制的服务名，即/etc/init.d目录下的脚本文件名；
		控制命令：系统服务脚本支持的控制命令
	https://www.cnblogs.com/wangtao_20/p/3645690.html
	https://www.cnblogs.com/web424/p/6761153.html