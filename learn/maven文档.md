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
				2. 路径相同先声明者优先
			统一定义版本：
				先定义    
				<properties>  
	        		<springframework.version>1.5.6</springframework.version>  
	    		</properties>
	    		后引用
	    		<version>${springframework.version}</version>


5. 仓库
	在Maven世界中，任何一个依赖、插件或者项目构建的输出，都可以称为构件
	Maven可以在某个位置统一存储所有Maven项目共享的构件，这个统一的位置就是仓库
		1. gav和本地maven仓库映射：groupId/artifactId/version/artifactId-version.packaging
	    2. 本地仓库地址默认为：Default: ${user.home}/.m2/repository,可以自己修改<localRepository>/path/to/local/repo</localRepository>来修改
	    3. maven默认都有一个中央仓库，远程仓库，本地仓库为空时就需要从远程仓库下载，但是中央仓库的下载速度常常有限制，尤其是在国内，
	    	常常配置为上私服，开发先从私服中请求，没有则私服从外部缓存在给予提供
	    	<!-- 配置远程仓库 -->
			    <repositories>
			        <repository>
			            <id>jboss</id>
			            <name>JBoss Repository</name>
			            <url>http://repository.jboss.com/maven2/</url>
			            <releases>
			                <enabled>true</enabled>
			                <updatePolicy>daily</updatePolicy>
			            </releases>
			            <snapshots>
			                <enabled>false</enabled>
			                <checksumPolicy>warn</checksumPolicy>
			            </snapshots>
			            <layout>default</layout>
			        </repository>
			    </repositories>
			repository:在repositories元素下，可以使用repository子元素声明一个或者多个远程仓库
			id：仓库声明的唯一id，尤其需要注意的是，Maven自带的中央仓库使用的id为central，如果其他仓库声明也使用该id，就会覆盖中央仓库的配置
			name：仓库的名称，让我们直观方便的知道仓库是哪个，暂时没发现其他太大的含义
			url：指向了仓库的地址，一般来说，该地址都基于http协议，Maven用户都可以在浏览器中打开仓库地址浏览构件
			releases和snapshots：用来控制Maven对于发布版构件和快照版构件的下载权限。需要注意的是enabled子元素，该例中releases的enabled值为true，表示开启JBoss仓库的发布版本下载支持，而snapshots的enabled值为false，表示关闭JBoss仓库的快照版本的下载支持。根据该配置，Maven只会从JBoss仓库下载发布版的构件，而不会下载快照版的构件
			layout：元素值default表示仓库的布局是Maven2及Maven3的默认布局，而不是Maven1的布局。基本不会用到Maven1的布局
			其他：对于releases和snapshots来说，除了enabled，它们还包含另外两个子元素updatePolicy和checksumPolicy。
				1：元素updatePolicy用来配置Maven从远处仓库检查更新的频率，默认值是daily，表示Maven每天检查一次。其他可用的值包括：never-从不检查更新；always-每次构建都检查更新；interval：X-每隔X分钟检查一次更新（X为任意整数）。
				2：元素checksumPolicy用来配置Maven检查校验和文件的策略。当构建被部署到Maven仓库中时，会同时部署对应的检验和文件。在下载构件的时候，Maven会验证校验和文件，如果校验和验证失败，当checksumPolicy的值为默认的warn时，Maven会在执行构建时输出警告信息，其他可用的值包括：fail-Maven遇到校验和错误就让构建失败；ignore-使Maven完全忽略校验和错误
		4. 配置认证信息
		认证一般配置在settings.xml中，尽自己可见
		<settings>
      		...
     	 <!--配置远程仓库认证信息-->
		    <servers>
		         <server>
		              <id>releases</id>
		             <username>admin</username>
		             <password>admin123</password>
		         </server>
		    </servers>
    		...
		</settings>
		5. 部署到远程仓库
		编辑项目的pom.xml文件。配置distributionManagement元素
		<distributionManagement>
	        <repository>
	            <id>releases</id>
	            <name>public</name>
	            <url>http://59.50.95.66:8081/nexus/content/repositories/releases</url>
	        </repository>
	        <snapshotRepository>
	            <id>snapshots</id>
	            <name>Snapshots</name>
	            <url>http://59.50.95.66:8081/nexus/content/repositories/snapshots</url>
	        </snapshotRepository>
		</distributionManagement>
		配置好了就运行命令mvn clean deploy，Maven就会将项目构建输出的构件部署到配置对应的远程仓库
		6. 配置镜像
		国外仓库下载jar包太慢，可以配置国内镜像，需要在settings.xml文件中修改，阿里云镜像如下
		<mirrors>
		    <mirror>
		      <id>alimaven</id>
		      <name>aliyun maven</name>
		      <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
		      <mirrorOf>central</mirrorOf>        
		    </mirror>
  		</mirrors>
		镜像相关属性：
			<mirrorOf>*<mirrorOf>:匹配所有远程仓库
			<mirrorOf>external:*<mirrorOf>:匹配所有远程仓库，使用localhost的除外，使用file://协议的除外。也就是说，匹配所有不在本机上的远程仓库
			<mirrorOf>repo1,repo2<mirrorOf>:匹配仓库repo1h和repo2，使用逗号分隔多个远程仓库
			<mirrorOf>*,!repo1<mirrorOf>:匹配所有远程仓库，repo1除外，使用感叹号将仓库从匹配中排除
			需要注意的是，由于镜像仓库完全屏蔽了被镜像仓库，当镜像仓库不稳定或者停止服务的时候，Maven仍将无法访问被镜像仓库，因而将无法下载构件
		7. 仓库服务搜索地址
			1. Sonatype Nexus：https://repository.sonatype.org/
			2. MVNrepository：http://mvnrepository.com/
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
