resourceUtil获取路径

1. 静态资源配置
两个属性：
	1. spring.mvc.static-path-pattern：/index/**
		标识服务器接受的静态资源访问模板，默认为无，也就是可以直接访问
	2. spring.resources.static-locations：/resource
		标识服务器的静态资源位置，多个以逗号分隔，按照顺序查找加载，默认为那四个
自定义静态资源配置
	新建配置类，继承WebMvcConfigurerAdapter类，重写addResourceHandlers方法，配置类需加注解@Configuration,@EnableWebMvc
	配置注解后默认的配置失效，包括yml中的自定义配置，WebMvcConfigurerAdapter抽象类中有很多方法，都是实现WebMvcConfigurer接口，
	包括拦截器配置

2. 拦截器配置
	1. 定义拦截器类，实现HandlerInterceptor接口，return true表是放行
	2. 在上文：新建配置类，继承WebMvcConfigurerAdapter类，重写addResourceHandlers方法，配置类需加注解@Configuration,@EnableWebMvc的类中
	重写addInterceptors并添加拦截器

3. mybatis配置
	关于spring中mybatis的执行原理：
	
	1. 添加mybatis依赖
```xml
        <!--mybatis-->
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>1.3.0</version>
        </dependency>
```	
	2. 在application.yml中配置实体类映射和mapper.xml文件路径
```yml
		mybatis:
	  type-aliases-package: com.example.demo.domain
	  mapper-locations: classpath:mapper/*.xml
```
	3. 在启动类在上加上注解@MapperScan("com.neo.mapper")，启动时自动搜索所有mapper文件，
	或者在dao上加上@mapper注解（@reporsitory也是要的）
	4. 书写mapper.xml和dao

4. 异步调用
	1. 在启动类加上注解@EnableAsync，开启异步调用
	2. 在需要异步调用的方法上加上@Async注解，这里需要注意的是异步调用的对象是方法，还有当该方法所在类开启事务时，
	在spring中是创建了一个代理类来执行事务的，这种情况需要建立一个异步任务类，将异步方法放于其中（加上@Async注解）
	通过注入的方式调用方法

5. 配置文件解析：
在springboot中，属性的配置要比ssm配置方便的多，约定优于配置的思想下，大部分的属性配置springboot均有默认值，少部分是必须要配置的，但当
我们自定义属性值时，默认的配置会自动失效
多环境配置：
	一般的属性配置是在application.properties中，但是也可以在applicaion.xml、application.yml中配置属性，个人觉得yml的格式更加清晰，在实际开发过程中
	我们可以配置多个环境配置文件，1.配置spring.profiles.active: dev 表示启用appliation-dev.yml配置
配置自定义属性值：
	我们可以在配置文件中定义属性，在代码里面获取，实现读取和配置分离（叫什么我忘了），一般系统配置写在yml中，常量一般定义在接口或者枚举中，配置方法如下：
	1. 在yml配置相关属性
	2. 编写bean类，就和实体类一样，加上@configuration注解
		1. 方法一： 定义属性值，属性值上加上注解@value（"${yml配置的全名}"）
		2. 方法二： 在实体类上额外加上注解@ConfigurationProperties(prefix = "前缀")
		评价：只有一层关系时，方法二更加简单，但涉及到多层复杂关系，方法一更加简便，方法二需要内部类来实现

6. 单元测试
	1. 新建测试：在对应类中->navigate->Test->选择相应的方法->自动创建测试用例
	2. serive层测试：注入dao执行测试即可
	3. controller测试： 需要MockMvc实现了对Http请求的模拟，能够直接使用网络的形式，转换到Controller的调用，得测试速度快、不依赖网络环境、无需启动项目
	4. 若@Transactional注解junit会自动回滚，若不想回滚加上@rollback(false)

7. 事务
	1. 在Spring Boot中，当我们使用了spring-boot-starter-jdbc或spring-boot-starter-data-jpa依赖的时候，
	框架会自动默认分别注入DataSourceTransactionManager或JpaTransactionManager，
	所以我们不需要任何额外配置就可以用@Transactional注解进行事务的使用，这里需要注意的是导的是spring下的包，不是javax下的。
	2. 关于事务注解的一些属性:
		1. @Transactional(value="事务管理器名称"):指定事务管理器，多数据源常用到
		2. @Transactional(isolation = Isolation.DEFAULT)：指定隔离级别，默认的就是与底层数据库级别一直
		另外都是事务的隔离级别，不赘述了
		3. @Transactional(propagation = Propagation.MANDATORY)：指定事务的传播行为
			1. REQUIRED：如果当前存在事务，则加入该事务；如果当前没有事务，则创建一个新的事务。
			2. SUPPORTS：如果当前存在事务，则加入该事务；如果当前没有事务，则以非事务的方式继续运行。
			3. MANDATORY：如果当前存在事务，则加入该事务；如果当前没有事务，则抛出异常。
			4. REQUIRES_NEW：创建一个新的事务，如果当前存在事务，则把当前事务挂起。
			5. NOT_SUPPORTED：以非事务方式运行，如果当前存在事务，则把当前事务挂起。
			6. NEVER：以非事务方式运行，如果当前存在事务，则抛出异常。
			7. NESTED：如果当前存在事务，则创建一个事务作为当前事务的嵌套事务来运行；如果当前没有事务，则该取值等价于REQUIRED
		4. @Transactional(rollbackFor = Throwable.class)，指定回滚的情况，这就是出先任何错误和异常都回滚事务

8. 文件的上传下载
	1. 前端上传指定格式为，我们以MultipartFile，对象来接受，在指定目录存储即可
	2. 将需要下载的文件以流的形式写如HttpServletResponse对象中，直接返回即可，需要注意的是需要设置响应体的格式

9. 发送邮件
	已完成

10. 集成mybatis插件
http://tengj.top/2017/12/20/springboot11/
https://blog.csdn.net/isea533/article/details/42102297
https://tonydeng.github.io/rfc6241-zh/
MockMvc
https://blog.csdn.net/xiao_xuwen/article/details/52890730
为什么不用jsp:
https://blog.csdn.net/piantoutongyang/article/details/65446892

11. 集成消息队列

12. 正向和反向代理
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

ngx_http_gzip_module:压缩静态资源，提升性能

无缝升级：假设你有一个旧版本
1. 先保证相关库是完全的：
	sudo yum -y install pcre-devel openssl openssl-devel
2. 下载解压新版本nginx,congigure,make,make install
3. 无缝启动：
	sudo make upgrade

安装nginxtop
sudo apt-get install python-pip: 安装pip
sudo pip install ngxtop
nginxtop

ngx_http_auth_basic_module:
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


