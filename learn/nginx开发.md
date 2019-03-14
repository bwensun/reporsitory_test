1. 简介：
nginx是一个HTTP服务器，也是一个反向代理服务器，它是一个基于事件的异步IO并发模型，轻量级

2. 命令：
	./nginx 启动nginx
	./nginx -s stop 停止nginx
	./nginx reload 重新载入配置文件


3. 配置文件解析：
linux中改变功能绝大多都是修改配置文件，linux中的配置文件在/etc/nginx/nginx.conf中,nginx为模块化系统，各模块完成不同的功能
http_gzip_static_module就是负责压缩的，http_ssl_module就是负责加密的，其配置文件基本由两个模块构成event,http，
而模块又是可以相互之间进行嵌套的，各个模块是有层级关系的，http和events还有mail是同级的，http就是跟web有关的,
	server,顾名思义就是一个服务，比如你现在有一个域名，要部署一个网站，那就得创建一个server块,listen为监听端口号，root为访问域名展示的index.html
	server_name:为域名,location为访问域名之下目录时对应的设置：

	server {
  		listen 80;
  		root /home/yinsigan/foo;
  		server_name foo.bar.com;
  		location / {

  		}
	}
	配置子配置文件读取：使用Include
	  include /etc/nginx/conf.d/*.conf;
  	  include /etc/nginx/sites-enabled/*;

	location配置详解：
	location [modifier] match {
    ...
	}
	匹配规则:
		啥都没： 和后面的match进行匹配
		= : 精确匹配
		~ : 大小写敏感的正则匹配
		~*:大小写不敏感的正则匹配
		^~:非正则匹配
	匹配顺序：
		(location =) > (location 完整路径) > (location ^~ 路径) 
		> (location ~,~* 正则顺序) > (location 部分起始路径) > (/)
	root指令：
		匹配替换ip+端口号,最终得到的路径为 root + match，注意match前最好要有斜杠，在linux中
	多斜杠视为单斜杠，保持前面一直有斜杠可以避免出错，root中第一个出现斜杠表示从根目录出发(linux目录)，比如
	root:/usr/local/nginx/  match为/static 这样比较好，访问安装目录下文件最好使用alias
	alias: static  match： static
	alias指令：
		其替换规则是连match一并替换，同样的路径alias需要多写点
	index指令：
	只处理以/结尾的uri，用于指定索引文件，文件名可以包含变量，
	按照文件做顺序查找，看文件是否存在，如存在则就把文件加到/后，发起redirect,重新访问
				index 用于设定我们只输入域名后访问的默认首页地址		

	rewrite指令：
		使用nginx提供的全局变量或自己设置的变量，结合正则表达式和标志位实现url重写以及重定向。rewrite只能放在server{},location{},if{}中，并且只能对域名后边的除去传递的参数外的字符串起作用
		举例：访问路径为http://oss.yogovi.com/user/findById?id=123,rewrite替换的内容即为/user/findById,除去域名和参数
		语法:rewrite regex replacement [flag]
		更改统一域名下获取资源的路径
		flag:
			last : 相当于Apache的[L]标记，表示完成rewrite
			break : 停止执行当前虚拟主机的后续rewrite指令集
			redirect : 返回302临时重定向，地址栏会显示跳转后的地址
			permanent : 返回301永久重定向，地址栏会显示跳转后的地址
		if:if(condition){...}
			concation:
				表达式只有一个变量时，值为空或者任何以0开头的字符串都会为false
				比较变量和内容使用=和！=
				~正则匹配，~*不区分大小写的匹配，！~区分大小写的不匹配
				-f和!-f用来判断是否存在文件
				-d和!-d用来判断是否存在目录
				-e和!-e用来判断是否存在文件或目录
				-x和!-x用来判断文件是否可执行
		全局变量：
				$args ： #这个变量等于请求行中的参数，同$query_string
				$content_length ： 请求头中的Content-length字段。
				$content_type ： 请求头中的Content-Type字段。
				$document_root ： 当前请求在root指令中指定的值。
				$host ： 请求主机头字段，否则为服务器名称。
	客户端分流	$http_user_agent ： 客户端agent信息
				$http_cookie ： 客户端cookie信息
				$limit_rate ： 这个变量可以限制连接速率。
				$request_method ： 客户端请求的动作，通常为GET或POST。
	限制访问		$remote_addr ： 客户端的IP地址。 
				$remote_port ： 客户端的端口。
				$remote_user ： 已经经过Auth Basic Module验证的用户名。
				$request_filename ： 当前请求的文件路径，由root或alias指令与URI请求生成。
				$scheme ： HTTP方法（如http，https）。
				$server_protocol ： 请求使用的协议，通常是HTTP/1.0或HTTP/1.1。
				$server_addr ： 服务器地址，在完成一次系统调用后可以确定这个值。
				$server_name ： 服务器名称。
				$server_port ： 请求到达服务器的端口号。
				$request_uri ： 包含请求参数的原始URI，不包含主机名，如：”/foo/bar.php?arg=baz”。
				$uri ： 不带请求参数的当前URI，$uri不包含主机名，如”/foo/bar.html”。
				$document_uri ： 与$uri相同

4. 反向代理：
	正向和反向代理
		正向代理：一般代理过程，A想获取服务器C的资源，但用于某些原因不直接访问服务器C，于是请求代理服务器B，服务器B去请求服务器C，将获得结果转发给A
		正向代理目的：
			1. 跨过限制：可能被拦截，或者网络出现问题
			2. 加速： A和C之间的交互速度 < A-B-C
			3. cache: 代理服务器被委托请求数据后，会将请求结果缓存，下一次请求相同资源可以直接给予
			4. 访问授权： 对内部的访问权限进行控制
			5. 隐藏访问者： 对于C来说，并不知道最后是A请求的资源
		反向代理：和正向代理相反，对于服务器A来说，反向代理服务器B就相当于资源服务器，就和正常请求一样去访问，A并不知道C的存在
		反向代理目的：
			1. 隐藏原始资源服务器：A不知道C有一个好处，Y原始资源服务器被换掉对A无影响的，正向代理做不到
			2. 负载均衡：反向代理服务器，可以对于来的请求进行策略优化，保证访问的资源速度
		注意：
			1. 正向代理是代理服务器代理请求者，反向代理服务器代理的是资源服务器
			2. 正向代理是是需要对代理服务器进行设置的，也就是说他知道这是代理的，反向代理增就是正常请求
	代理设置：
		在location模块使用proxy_pass指令，如proxy_pass:http://www.baidu.com, 需要注意的是localtion的匹配路径一定
		要在路径最前面带上斜杠，否则会出现访问404，

5. ngx_http_gzip_module:压缩静态资源，提升性能

6. 无缝升级：假设你有一个旧版本
	1. 先保证相关库是完全的：
		sudo yum -y install pcre-devel openssl openssl-devel
	2. 下载解压新版本nginx,congigure,make,make install
	3. 无缝启动：
		sudo make upgrade

7. 安装nginxtop
	sudo apt-get install python-pip: 安装pip
	sudo pip install ngxtop
	nginxtop

8. ngx_http_auth_basic_module:
	提供最基本的基于http协议的认证，它可以实现在访问页面时，
	提供最基本的用户名和密码的验证，验证匹配的信息是以文件的形式存储
	1. 先安装命令相关：sudo apt-get install apache2-utils
	2. 生成用户admin: sudo htpasswd -c /etc/nginx/.htpasswd admin   -c参数表示创建
	3. 再输入两遍密码即可
	4. 配置http basic auth认证:
			server {
	        ...
	        location /status {
	            auth_basic "Restricted";
	            auth_basic_user_file /etc/nginx/.htpasswd;
	            vhost_traffic_status_display;
	            vhost_traffic_status_display_format html;
	        	}
			}







https://nginx.rails365.net/chapters/2.html

https://docshome.gitbooks.io/nginx-docs/content/%E4%BB%8B%E7%BB%8D/%E5%88%9D%E5%AD%A6%E8%80%85%E6%8C%87%E5%8D%97.html

配置文件：
http://seanlook.com/2015/05/17/nginx-install-and-config/