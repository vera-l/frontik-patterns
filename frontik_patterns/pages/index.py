from frontik.handler import AwaitablePageHandler

STYLES = '''
<style>
    body {
        padding: 20px 30px 10px;
        font-family: 'PT Mono', monospace;
        color: #586E75;
        background-color: #FDF6E3;
        font-size: 1em;
    }
    a:link, a:visited {
        color: #2AA198;
        border-bottom: 1px solid #2AA198;
        text-decoration: none;
    }
    a:hover, a:active {
        color: #D33682;
        border-bottom: 1px solid #D33682;
    }
    h1 {
        margin: 0 0 30px;
    }
    ul {
        margin: 0;
        padding: 0;
    }
    .code {
        font-size: 10px;
        color: #AAA;
    }
    .code a:link, .code a:visited {
        color: #AAA;
        border-bottom-color: #AAA; 
    }
</style>
'''

PAGES = {
    'async_coro': [
        'serial',
        'parallel',
        'parallel_coro',
        'parallel_dict',
        'tasks',
    ],
    'tornado_coro': [
        'serial',
        'parallel',
        'parallel_coro',
        'parallel_dict',
        'tasks',
    ],
    'tornado_callbacks': [
        'serial',
        'parallel',
        'tasks',
    ],
}

LINKS = [page for page in PAGES]
CODE_BASE = 'https://github.com/vera-l/frontik_patterns/tree/master/frontik_patterns/pages'


def get_link(group, name):
    return f'''
<li><a href="/{group}/{name}?debug">{name}</a> 
<span class="code">(<a href="{CODE_BASE}/{group}/{name}.py">code</a>)</span>
</li>'''


def get_nav(pages):
    tags = ['<html>', '<body>', STYLES, '<ul>']
    for group in pages:
        tags.append('<li>')
        tags.append(f'<strong>{group.upper()}</strong>')
        tags.append('<ul>')
        for name in pages[group]:
            tags.append(get_link(group, name))
        tags.append('</ul>')
        tags.append('<br />')
        tags.append('</li>')
    tags.append('</ul>')
    tags.append('</body>')
    tags.append('</html>')
    return tags


class Page(AwaitablePageHandler):
    default_action = 'areas'

    async def get_page(self):
        self.text = ''.join(get_nav(PAGES))
