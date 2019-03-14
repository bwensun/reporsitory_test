1. 管道操作和重定向
|表示将前面的结果作为后面的输入继续处理
>表示覆盖 比如 zjx > q.txt 表示写入zjx到q.txt中
>>表示追加
2. 可以执行cmd命令，比如ipconfig查看ip，netstat查看端口，rount print查看路由
	输入字符串会默认直接输出该字符，若想执行该字符串命令，则直接以在前面加&即可，比如& "ls"
3. cmdlets是Powershell的内部命令，每个命令有一个动词和名词组成，格式为：动词-名词，
4. Alias是别名，方便使用，ls,dir就是get-ChildItem的别名
	get-Alias | where {$_.Definition.Startswith("add")}
	创建自己的别名
	Set-Alias -Name Edit -Value notepad
	获取别名
	$Alias:Edit
5. 