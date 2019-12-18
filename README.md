# 0x01 概述
* 使用Python3开发
* 结果导出为csv文件
* 使用在线平台（[http://whatweb.bugscaner.com](http://whatweb.bugscaner.com)）进行指纹识别
* 两个版本，一个版本直接导入url.txt使用，另外一个版本需要结合鬼麦子的子域名扫描工具使用

# 0x02 使用方法
```
git clone https://github.com/teamssix/Batch-identification-of-website-CMS-fingerprints.git
cd Batch-identification-of-website-CMS-fingerprints
pip3 install -r requirements.txt
python3 Batch_CMS_identification.py url.txt output_filename
python3 DB_Batch_CMS_identification.py db_name
```

上面命令后的 "db_name" 参数就是自己指定要收集的目标，比如用鬼麦子的get_domain工具收集了一波贝壳的子域，那么 mongo 数据库中的就会有一个 "_ke_com" 表，这个时候，"db_name" 参数就是"_ke_com"，最后结果同样以CSV保存。


![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/cmsshibie1.png)
导出后的CSV表格
![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/Batch_CMS_identification2.png)
![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/Batch_CMS_identification3.png)

# 0x03 注意事项
* url.txt文件中地址格式不能有```http://```或```https://```，正确的url.txt示例：```teamssix.com```或```www.teamssix.com```都是可以的。

* 如果执行过程中出现警告，一般是碰到有些网站使用的https的情况，可以不用理会，对结果没有影响。

* 如果想重新运行程序，请确认导出的CSV文件没有被打开，否则将因为不能导出文件而报错

* 程序中途想要退出，可以直接Ctrl+C退出，等待一段时间后便会退出，结果会保存

* 该平台每天有1500的使用限制。

* 如果程序出现```UnicodeEncodeError: gb2312 codec cant encode character \xb7 in position 52: illegal multibyte sequence```异常，需要修改results()子函数代码，比如这里提示 '\xb7' 编码存在问题，就需要将原来代码修改成下面的样子
```
	for i in req_json:
		i = i.replace('\xb7',' ') #原这行没有
		sub_i = req_json[i][0]
		result[i] = sub_i
	result['URL'] = url.replace('\xb7',' ') 原result['URL'] = url
	result['title'] = title.replace('\xb7',' ') 原result['title'] = title
```
也即是是修改上面存在注释的三行代码，其实这里就是把报错的 '\xb7' 给替换掉，如果程序继续报这个错，就继续在上一步修改的基础上添加replace，比如修改成```result['URL'] = url.replace('\xb7',' ').replace('\u2013',' ')```

* 因为有时程序可能会中途发生异常退出，所以如果想从url列表的某一行开始，可以在主函数的```for numbers in range(len(url_list)): ```下添加一个判断，比如```if numbers > 589:```，之后程序就会从 url列表的第590行开始。

![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
