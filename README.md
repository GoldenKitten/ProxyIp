# ProxyIp
获取代理ip
## 项目简介
该项目用scrapy+mysql实现代理ip的获取
## 使用教程
1. 下载该项目并解压
2. 安装scrapy、pymysql、sqlalchemy模块
3. 在mysql里创建数据库proxyip
4. 打开settings.py文件，配置mysql用户名和密码
5. 在proxyip目录下运行命令scrapy crawl xici
