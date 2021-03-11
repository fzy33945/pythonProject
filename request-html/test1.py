from requests_html import HTML
doc = """<a href='https://www.qiushibaike.com/'>"""

html = HTML(html=doc)
html.links
print(html.html)