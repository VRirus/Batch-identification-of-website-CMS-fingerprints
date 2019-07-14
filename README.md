# Batch-identification-of-website-CMS-fingerprints
> 批量识别网站CMS指纹

- 本程序利用在线CMS识别网站对目标进行识别，其利用平台为[http://whatweb.bugscaner.com/](http://whatweb.bugscaner.com/ "http://whatweb.bugscaner.com/")
- 该平台每天有1500次的使用限制，基本够用

# 使用方法
1. 在终端中输入`python Batch_CMS_identification.py url.txt`即可，url.txt为待识别的地址文件
2. 在当前目录下可以就看到刚才导出的Output_Result.csv文件

![](https://images-cdn.shimo.im/cEwEWzhuVBIA8l6C__thumbnail)

![](https://images-cdn.shimo.im/CNcLkR1G4nk1iGaQ/2.png__thumbnail)

# 注意
- url.txt文件中地址格式需要http开头，如http://www.teamssix.com
- 如果执行过程中出现警告，一般是碰到有些网站使用的https的情况，可以不用理会，对结果没有影响
- 如果想重新运行程序，请确认导出的CSV文件没有被打开，否则将因为不能导出文件而报错
