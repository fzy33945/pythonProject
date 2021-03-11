from requests_html import HTMLSession

session = HTMLSession()
url = 'http://bbs.tianya.cn/post-culture-488321-1.shtml'
r = session.get(url)

author = r.html.find('div.atl-info span a', first=True).text
div = r.html.find('div.atl-pages', first=True)
links = div.find('a')
total_page = 1 if links == [] else int(links[-2].text)
title = r.html.find('span.s_title span', first=True).text 

with open(f'{title}.txt', 'x', encoding='utf-8') as f:
    for i in range(1, total_page + 1):
        s = url.rfind('-')
        r = session.get(url[:s + 1] + str(i) + '.shtml')
        items = r.html.find(f'div.atl-item[_host={author}]')
        for item in items:
            content: str = item.find('div.bbs-content', first=True).text
            if not content.startswith('@'):
                f.write(content + "\n")