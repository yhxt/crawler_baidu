# crawler_baidu

此爬虫项目是利用python的urllib和urllib2来实现的。

爬取思路：
		1.百度贴吧搜索链接为：http://tieba.baidu.com/f?&kw=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A
			kw=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A实际上就是kw=中国联通
			第2页面的链接为：http://tieba.baidu.com/f?kw=%E8%81%94%E9%80%9A&pn=50
			分析得出：每一页的显示内容pn=(n-1)*50
		2.利用urllib.urlencode方法对用户输入的贴吧名称转换，并拼接出来用户搜索贴吧的完整路径
		3.根据用户输入的起始页和结束页进行爬取
		4.get_html函数用老爬取html内容
		5.save_html函数进行爬取数据的保存
		6.load_crawler函数进行完整带页码的url,并爬取保存