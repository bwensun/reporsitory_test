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






