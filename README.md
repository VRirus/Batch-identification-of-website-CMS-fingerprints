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
python3 Batch_CMS_identification.py url.txt filename
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
* 如果程序经常提示连接异常，可能因为对方拒绝连接或者本地网速较慢，如果本地网速延时较高，可将程序中的两处timeout调高一些，为保证速度，默认timeout为1秒。
* 该平台每天有1500的使用限制。

![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
