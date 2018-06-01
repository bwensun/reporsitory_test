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
