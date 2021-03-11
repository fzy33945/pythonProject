from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.qiushibaike.com/')  
print(r.html.html)

print(r.html.links)
print(r.html.absolute_links)

print(r.html.xpath("//div[@id='menu-hover']", first=True).text)



# print(r.html.find('div#menu-hover', first=True).text)
# print(r.html.find('div#menu-hover a'))
# print(list(map(lambda x: x.text, r.html.find('div.content span'))))