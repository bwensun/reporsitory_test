redis:
http://www.importnew.com/27031.html
redis:是一个key-value数据库
	redis特点;
		1. 性能极高：读的速度110000次/s,写入81000次/s
		2. 支持数据持久化，可以将数据写如入磁盘，重新启动时会自动加载使用
		3. 支持多种数据结构，有string、list、set、zset、hset、hash
		4. 支持分布式,事务，发布订阅模型

	数据结构：
		1. string: 使用最多，他是二进制安全的，不但可以存储字符串，任意对象，图片序列化都可以放入存储，
			最多可以存储512m
			方法：
				set key value
				set key expiredTime value
				get key
				setrange key offset value 从指定下标开始覆盖原value为新value
				strlen key 获取key对应value的长度
				mset key1 value1 key2 value2 批量设置
				mget key1 key2 key3
				msetnx key1 value1 key2 value2 批量新增，只要一个key已存在，都不执行
				getset key value 设置新值，返回旧值
				getrange key start end 截取key对应value的字符串，下标起始为0
				incr key 对key对应value累加1
				incrby key int(累加值) 类似incr,但value不存在会将value设为0
				desr key
				desrby key int(累减值)
		2. hash:hash的value是一个键值对，可以类比为一个键值对的map中的value还是一个map，适合存储对象
			每个hash可以存储2^32 -1个键值对
			方法：
				hset key field value
				hget key field
				hsetnx key field value 设置value值，不存在创建
				hmset key field1 value1 field2 value2
				hmget key field1 field2 field3
				hincrby key field int(累加值)
				hgetall key 获取hash所有的field和value 
				hvals key 获取hash的所有value
				hkeys key 返回hash所有field
				hlen key 返回hash的field数
				hstrlen key 返回value的字符串长度
		3. list:有序的字符串列表，可以制定添加到头尾（左右），一个列表最多可以包含2^32 -1个元素
			方法：
				rpush key value 尾部插入，r->right
				lrange key start stop 展示列表
				lpop key 获取头元素
				ltrim key start stop 截取list,获取topn值
		4. set:	去重的集合，set集合的可以求交集，并集，差集
			方法：
				sadd key value1 (value2)
				scard key 求集合元素数
				sdiff key1 key2 返回集合1减去集合2
		5. sorted set:有序集合，类似于list,但无重复，每个元素都关联一个double类型分数作为排序依据，
			key是唯一的，但是score是可以重复的
			方法：
				zadd key score1 value1 (score2 value2)
				zrange key max min withscores 返回score在min和max之间的zset
				zcount key min max 返回zset中score在min和max之间的value
				zincrby key int(累加值) value
	订阅发布模型：
		redis同样支持发布订阅模型
		命令：
			订阅：subscribe channel(频道名)
			发布：publish channel(频道名) message
			即使关闭后重新订阅，丢失的信息即丢失无法获取
		java实现：

	事务：
		开启事务： multi
		事务提交： exec

	数据备份与恢复:
		save: 备份当前redis数据库,该命令将会在redis安装目录中创建dump.rdb,恢复数据则需要将备份文件移动到
		redis安装目录并启动服务，获取redis目录可以使用config
		ngsave:
		后台执行save
		持久化：
			实际使用之中，由于redis中的数据是存储在内存中，重启之后就全部丢失，redis支持的持久化可以
			将数据写到磁盘上，重启后都读取恢复数据
			RDB:
				默认的存储方式，快照存储
				dbfilename dump.rdb
				# save <seconds> <changes>
				save 900 1    #当有一条Keys数据被改变时，900秒刷新到Disk一次
				save 300 10   #当有10条Keys数据被改变时，300秒刷新到Disk一次
				save 60 10000 #当有10000条Keys数据被改变时，60秒刷新到Disk一次
				redis中的RDB任意时刻都是可用的，因为其写操作是在一个新进程中进行的。 当生成一个新的RDB文件时，Redis生成的子进程会先将数据写到一个临时文件中，然后通过原子性rename系统调用将临时文件重命名为RDB文件
				同时，Redis的RDB文件也是Redis主从同步内部实现中的一环。
					第一次Slave向Master同步的实现是： Slave向Master发出同步请求，Master先dump出rdb文件，然后将rdb文件全量传输给slave，然后Master把缓存的命令转发给Slave，初次同步完成。
					第二次以及以后的同步实现是： Master将变量的快照直接实时依次发送给各个Slave。 但不管什么原因导致Slave和Master断开重连都会重复以上两个步骤的过程。
				事实上RDB有点像定时调度，实际之中发生问题自最后一次同步之后的内容都会丢失
			AOF（Append-only file）
				更加安全的方式，已追加的方式来写入文件之中，恢复数据时只需要将步骤再走一遍即可，
				开启aof需要将redis.conf中的ppendonly参数开启:
				 appendonly yes         #启用aof持久化方式
				 # appendfsync always   #每次收到写命令就立即强制写入磁盘，最慢的，但是保证完全的持久化，不推荐使用
				 appendfsync everysec     #每秒钟强制写入磁盘一次，在性能和持久化方面做了很好的折中，推荐
				 # appendfsync no #完全依赖OS的写入，一般为30秒左右一次，性能最好但是持久化最没有保证，不被推荐。
				 








