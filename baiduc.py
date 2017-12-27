# -*- coding:utf-8 -*-

import urllib
import urllib2
import codecs

"""
联通贴吧搜索链接为：http://tieba.baidu.com/f?&kw=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A
第2页面的链接为：http://tieba.baidu.com/f?kw=%E8%81%94%E9%80%9A&pn=50
分析得出：每一页的显示内容pn=(n-1)*50
"""


def get_html(url,filename):
    """
     1.get_html根据url地址进行网页内容抓取
     2.url即为爬取的链接完整地址
    """
    print '正在下载' + filename
    headers={'User-Agent-':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    return response.read()


def save_html(html,filename):
    """
    1.save_html是将get_html爬取的内容保存起来
    2.
    """
    print '正在保存'+filename
    with codecs.open(filename,'w') as f:
        f.write(html)
    print '-'*30

def load_crawler(url,StartPage,EndPage):
    """
    1.load_crawler拼接爬取的url地址
    2.url为用户输入的url完全地址
    """
    for page in range(StartPage,EndPage):
        pn=(page-1)*50
        filename='第'+str(page)+'页.html'
        fullurl=url+'&pn='+str(pn)
        print fullurl
        html=get_html(fullurl,filename)
        save_html(html,filename)
        print "谢谢使用"

if __name__ == '__main__':
    kw=raw_input('请输入需要爬取的贴吧名称：')
    StartPage=int(raw_input('请输入爬取内容的起始页码：'))
    EndPage=int(raw_input('请输入爬取内容的结束页码：'))

    url='http://tieba.baidu.com/f?'
    kw=urllib.urlencode({'kw':kw})
    fullurl=url+'&'+str(kw)
    print fullurl
    load_crawler(fullurl,StartPage,EndPage)
