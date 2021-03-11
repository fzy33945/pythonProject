from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.cnfeat.com/')
for html in r.html:
    print(html)
# r.html.next()
