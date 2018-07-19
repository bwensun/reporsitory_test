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