from requests-html import HTMLSession

session = HTMLSession()
r = session.get('https://ww.qiushibaike.com/text/')
// 查看页面内容
print(r.html.html)