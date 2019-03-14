# maven

### 安装maven

注意：安装Maven之前，先确认已经安装了JDK

1. 我们可以去maven官网下载，链接：[Maven官网](https://link.juejin.im/?target=http%3A%2F%2Fmaven.apache.org%2Fdownload.cgi)，下载完毕后解压即可

![image.png](https://user-gold-cdn.xitu.io/2018/1/2/160b27fca6e67627?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

2. 配置环境变量

   就和配置JDK一样，进入环境变量配置，新建系统变量**M2_HOME**以及修改**PATH**，**M2_HOME**变量值为maven的安装目录，**PATH**最后加上;%MA_HOME%\bin;

   如图

   ![image.png](https://user-gold-cdn.xitu.io/2018/1/2/160b27fca6d81655?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

3. 测试：进入cmd命令行，输入mvn -v，得到下面信息就说明配置成功![image.png](https://user-gold-cdn.xitu.io/2018/1/2/160b27fca9ef3782?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)



### IDEA集成Maven

ctrl+alt+s进入设置，搜索maven,配置上maven的安装目录，settings.xml的目录以及repository的目录，apply&OK

![image.png](https://user-gold-cdn.xitu.io/2018/1/2/160b27fceda7382f?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)



### GAVN

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.tengj</groupId>
    <artifactId>springBootDemo1</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springBootDemo1</name>
</project>
```

> groupId:定义了项目属于哪个组，一般为倒置的域名

> artifactId:定义了当前Maven项目在组中唯一的ID，一般为项目名

> version：指定了项目当前的版本

> name：非必需，描述项目



### 依赖的配置

#### 依赖范围

|   依赖范围   | 描述                                                         |
| :----------: | ------------------------------------------------------------ |
| **compile**  | 没有指定，就会默认使用该依赖范围，对于编译、测试、运行三种classpath都有效 |
|   **test**   | 只对测试有效，编译，运行是不会使用该依赖的                   |
| **provided** | 编译和测试classpath有效，但在运行时候无效，代表就是tomcat，springboot是自带tomcat的所以运行不需要配 |
| **runtime**  | 对于测试和运行classpath有效，但在编译主代码时无效，代表就是JDBC |



### nexus搭建私服

1. 下载nexus

   ​	下载地址：[nexus下载](https://www.sonatype.com/download-oss-sonatype?hsCtaTracking=920dd7b5-7ef3-47fe-9600-10fecad8aa32%7Cf59d5f10-099f-4c66-a622-0254373f4a92)，最新已经是3.x版本，下载速度有点慢

   ![1539794763254](C:\Users\郑建雄\AppData\Roaming\Typora\typora-user-images\1539794763254.png)

2. 安装并启动

   1. windows安装：

      1. 安装之前确认已经安装了JDK1.8以及maven

      2. 解压，获得两个文件目录，进入nexus-3.14.0-04/bin中，shift+右击打开cmd窗口，win10就打开powershell窗口，输入以下命令

         ```
         nexus.exe /run
         ```

         等待安装完毕

   2. linux安装：

      1. 将安装包放入linux中

      2. 解压到user/local下，最好自己新建一个目录

         ```shell
         #这是我安装的命令
         tar -zxvf /software -C /usr/local/nexus3.x
         ```

      3. 进入bin目录启动	

         ```shell
         ./nexus start
         ```

3. 访问测试

   ```
   注意：
   1.注意查看防火墙状态，一般需要关闭防火墙
   2.如果8081端口号已经被占用，可以在etc/nexus-default.properties配置中修改
   3.尤其注意文件解压目录不能包含中文，nexus无法识别GBK编码，楼主在这里卡了不少时间
   ```

   输入`http://localhost:8081`访问得到以下页面表示启动成功

   ![1539795896586](C:\Users\郑建雄\AppData\Roaming\Typora\typora-user-images\1539795896586.png)

4. 登陆

   账号：admin    密码：admin123

5. 创建私服仓库

   该仓库就是我们在项目的pom.xml中获取jar包的仓库，点击创建私服

   ![1540136256491](C:\Users\郑建雄\AppData\Roaming\Typora\typora-user-images\1540136256491.png)

   填写仓库id以及相关配置![](C:\Users\郑建雄\Desktop\maven文档图片\Snipaste_2018-10-21_23-40-09.png)

   ![](C:\Users\郑建雄\Desktop\maven文档图片\Snipaste_2018-10-21_23-43-50.png)

6. 导入索引：

   1. nexus3索引还没查到有相关资料

### 用户端配置

##### 配置本地仓库（settings.xml）

```xml
<settings>
	<localRepository>D:\java\repository\</localRepository>
</settings>
```

##### 配置远程仓库（pom.xml）	

```xml
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
```

##### 配置认证

```xml
   <!--配置远程仓库认证信息-->
     <servers>
         <server>
             <id>releases</id>
             <username>admin</username>
             <password>admin123</password>
          </server>
      </servers>
```

##### **配置镜像**

```xml
<mirrors>
    <mirror>
      <id>alimaven</id>
      <name>aliyun maven</name>
      <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
      <mirrorOf>central</mirrorOf>        
    </mirror>
  </mirrors>
```

##### **部署构件至远程仓库**

1. 配置项目pom.xml

```xml
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
```

2. 执行mvn deploy 打包部署

   1. 创建用户

   2. 仓库管理

      ```
      1.component name的一些说明： 
          1）maven-central：maven中央库，默认从https://repo1.maven.org/maven2/拉取jar 
          2）maven-releases：私库发行版jar 
          3）maven-snapshots：私库快照（调试版本）jar 
          4）maven-public：仓库分组，把上面三个仓库组合在一起对外提供服务，在本地maven基础配置		settings.xml中使用。
      2.Nexus默认的仓库类型有以下四种：
          1）group(仓库组类型)：又叫组仓库，用于方便开发人员自己设定的仓库；
          2）hosted(宿主类型)：内部项目的发布仓库（内部开发人员，发布上去存放的仓库）；
          3）proxy(代理类型)：从远程中央仓库中寻找数据的仓库（可以点击对应的仓库的Configuration页签下Remote Storage Location属性的值即被代理的远程仓库的路径）；
          4）virtual(虚拟类型)：虚拟仓库（这个基本用不到，重点关注上面三个仓库的使用）；
      3.Policy(策略):表示该仓库为发布(Release)版本仓库还是快照(Snapshot)版本仓库；
      4.Public Repositories下的仓库 
         1）3rd party: 无法从公共仓库获得的第三方发布版本的构件仓库，即第三方依赖的仓库，这个数据通常是由内部人员自行下载之后发布上去；
         2）Apache Snapshots: 用了代理ApacheMaven仓库快照版本的构件仓库 
         3）Central: 用来代理maven中央仓库中发布版本构件的仓库 
         4）Central M1 shadow: 用于提供中央仓库中M1格式的发布版本的构件镜像仓库 
         5）Codehaus Snapshots: 用来代理CodehausMaven 仓库的快照版本构件的仓库 
         6）Releases: 内部的模块中release模块的发布仓库，用来部署管理内部的发布版本构件的宿主类型仓库；release是发布版本；
         7）Snapshots:发布内部的SNAPSHOT模块的仓库，用来部署管理内部的快照版本构件的宿主类型仓库；snapshots是快照版本，也就是不稳定版本
      所以自定义构建的仓库组代理仓库的顺序为：Releases，Snapshots，3rd party，Central。也可以使用oschina放到Central前面，下载包会更快。
      ```

   3. 

   4. 

      ![1539796366296](C:\Users\郑建雄\AppData\Roaming\Typora\typora-user-images\1539796366296.png)



### 本地配置

##### 代理中央仓库

只要在PMO文件中配置即可

```xml
<repositories>
        <repository>
            <id>maven-central</id>
            <name>maven-central</name>
            <url>http://192.168.1.14:8081/repository/maven-central/</url>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
            <releases>
                <enabled>true</enabled>
            </releases>
        </repository>
    </repositories>
```

##### **Snapshot包的管理**

1. 修改Maven的settings.xml文件，加入认证机制

   ```xml
   <server>
         <id>nexus</id>
         <username>admin</username>
         <password>admin123</password>
   </server>
   ```

2. 修改工程的Pom文件(settings.xml文件中的名字一定要对应上)

   ```xml
   <distributionManagement>
           <snapshotRepository>
               <id>nexus</id>
               <name>Nexus Snapshot</name>
               <url>http://192.168.1.14:8081/repository/maven-snapshots/</url>
           </snapshotRepository>
           <site>
               <id>nexus</id>
               <name>Nexus Sites</name>
               <url>dav:http://192.168.1.14:8081/repository/maven-snapshots/</url>
           </site>
       </distributionManagement>
   ```

3. 传到Nexus上,使用mvn deploy命令运行

   ```xml
   <groupid>com.woasis</groupid>
   <artifactid>test-nexus</artifactid>
   <version>1.0.0-<span style="color: #ff0000;">SHAPSHOT</span></version>
   <packaging>jar</packaging>
   ```

##### Releases包的管理

与Snapshot配置不同的地方，就是工程的PMO文件，加入repository配置

```xml
<distributionManagement>
        <repository>
            <id>nexus</id>
            <name>Nexus Snapshot</name>
            <url>http://192.168.1.14:8081/repository/maven-releases/</url>
        </repository>
```

打包的时候需要把Snapshot去掉

```xml
<groupId>com.woasis</groupId>
    <artifactId>test-nexus</artifactId>
    <version>1.0.0</version>
<packaging>jar</packaging>
```

**第三方Jar上传到Nexus**

```shell
mvn deploy:deploy-file -DgroupId=org.jasig.cas.client -DartifactId=cas-client-core -Dversion=3.1.3 -Dpackag
```

