1. 下载安装maven:
下载地址http://maven.apache.org/download.cgi
windows下：配置环境变量,我下载的3.5.3版本，
	1. 安装在windows环境，配置环境变量M2_HOME:安装目录（到文件），PATH中添加%M2_HOME%/bin
	2. 安装在linux环境，一样配置环境，生效后即可

2. 目录介绍：
	1. bin：该目录包含了mvn运行的脚本，这些脚本用来配置java命令，准备好classpath和相关的Java系统属性，然后执行Java命令
	2. boot:该目录只包含一个文件，该文件为plexus-classworlds-2.5.2.jar。plexus-classworlds是一个类加载器框架，相对于默认的java类加载器，它提供了更加丰富的语法以方便配置，Maven使用该框架加载自己的类库
	3. conf:该目录包含了一个非常重要的文件settings.xml。直接修改该文件，就能在机器上全局地定制Maven的行为，一般情况下，我们更偏向于复制该文件至~/.m2/目录下（~表示用户目录），然后修改该文件，在用户范围定制Maven的行为
	4. lib:该目录包含了所有Maven运行时需要的Java类库，Maven本身是分模块开发的，因此用户能看到诸如maven-core-3.0.jar、maven-model-3.0.jar之类的文件，此外这里还包含一些Maven用到的第三方依赖如commons-cli-1.2.jar、commons-lang-2.6.jar等等

3. maven命令：
	1. mvn clean：表示运行清理操作（会默认把target文件夹中的数据清理）
	2. mvn clean compile：表示先运行清理之后运行编译，会将代码编译到target文件夹中
	3. mvn clean test：运行清理和测试
	4. mvn clean package：运行清理和打包
	5. mvn clean install：运行清理和安装，会将打好的包安装到本地仓库中，以便其他的项目可以调用
	6. mvn clean deploy：运行清理和发布（发布到私服上面）

4. 关于pom.xml：
	1. 第一行：xml的头部，指定xml版本和编码格式
	2. project: pom的根元素，声明了一些POM相关的命名空间及xsd元素，紧随其下的modelVersion表示POM模型的版本号，
		maven3对应的都是4.0.0
	3. gav:联合三个可以确定jar包的唯一性
		groupId:代表组织和整个项目的唯一标志，一般为倒置的域名
		artifactId：具体的项目名
		version:版本号
		name:非必需，起个友好的名字
	4. dependencys:依赖，旗下可以包含多个依赖，依赖可以设置的标签除了gav外，还有
		1. type: jar/war/pom,大部分情况下不必生命默认为jar
		2. optional:标记依赖是否可选，true/false
		3. exclusions: 用来排除传递性依赖
		4. scope: 依赖范围
			1. compile:编译依赖范围，默认的依赖范围，对于编译、测试、运行环境都有效
			2. test： 测试依赖范围，只对测试环境有效，代表就是junit
			3. provided: 已提供依赖范围，只在编译和测试时有效，典型就是tomcat,eclipse是需要配这个的
			4. runtime：运行时依赖范围，对于测试和运行环境有效，编译无效，代表就是jdbc，
				一般都是代码里面没用到的，即没引入的，java时预编译的
			5. system: 系统依赖范围，和provided范围相同，但是必须指定systemPath属性指定该依赖的路径，
				由于此类依赖不是通过Maven仓库解析的，而且往往与本机系统绑定，可能构成构建的不可移植，
				因此应该谨慎使用。systemPath元素可以引用环境变量
			依赖传递：
				maven中存在依赖的传递，假设A依赖于B,B依赖于C，我们说A对于B是第一直接依赖，B对于C是第二直接依赖，A对于C是传递性依赖
			依赖调接规则：
				1. 路径最近者优先
				2. 路径相同先声明这优先

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<groupId>com.yogovi</groupId>
	<artifactId>order</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<packaging>war</packaging>

	<name>order</name>
	<description>订单</description>

	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>1.5.7.RELEASE</version>
		<relativePath /> <!-- lookup parent from repository -->
	</parent>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-redis</artifactId>
		</dependency>
		<dependency>
			<groupId>org.mybatis.spring.boot</groupId>
			<artifactId>mybatis-spring-boot-starter</artifactId>
			<version>1.3.0</version>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>com.fasterxml.jackson.core</groupId>
			<artifactId>jackson-annotations</artifactId>
		</dependency>
		<dependency>
			<groupId>com.fasterxml.jackson.core</groupId>
			<artifactId>jackson-core</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-configuration-processor</artifactId>
			<optional>true</optional>
		</dependency>

		<!-- Use MySQL Connector-J -->
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-tomcat</artifactId>
		</dependency>

		<!-- GENERAL UTILS -->
		<dependency>
			<groupId>org.apache.commons</groupId>
			<artifactId>commons-lang3</artifactId>
			<version>3.3.2</version>
		</dependency>
		<dependency>
			<groupId>com.google.guava</groupId>
			<artifactId>guava</artifactId>
			<version>18.0</version>
		</dependency>
		<dependency>
			<groupId>net.sf.dozer</groupId>
			<artifactId>dozer</artifactId>
			<version>5.4.0</version>
			<exclusions>
				<exclusion>
					<groupId>org.slf4j</groupId>
					<artifactId>slf4j-log4j12</artifactId>
				</exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.apache.poi</groupId>
			<artifactId>poi</artifactId>
			<version>3.9</version>
		</dependency>
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi-ooxml</artifactId>
            <version>3.9</version>
        </dependency>
    </dependencies>

	<profiles>
		<profile>
			<id>dev</id>
			<properties>
				<environment>dev</environment>
			</properties>
			<activation>
				<activeByDefault>true</activeByDefault>
			</activation>
		</profile>
		<profile>
			<id>test</id>
			<properties>
				<environment>test</environment>
			</properties>
		</profile>
		<profile>
			<id>prod</id>
			<properties>
				<environment>prod</environment>
			</properties>
		</profile>
	</profiles>

	<build>
		<!-- Turn on filtering by default for application properties -->
		<resources>
			<resource>
				<directory>${basedir}/src/main/resources/config/${environment}</directory>
				<filtering>true</filtering>
				<includes>
					<include>**/application*.yml</include>
					<include>**/logback*.xml</include>
				</includes>
			</resource>
			<resource>
				<directory>${basedir}/src/main/resources</directory>
				<excludes>
					<exclude>**/application*.yml</exclude>
					<exclude>**/logback*.xml</exclude>
				</excludes>
			</resource>
		</resources>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
				<configuration>
					<finalName>${project.artifactId}</finalName>
					<mainClass>${start-class}</mainClass>
				</configuration>
			</plugin>
		</plugins>
	</build>
</project>
```
