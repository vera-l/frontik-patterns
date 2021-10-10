from frontik.handler import PageHandler


class Page(PageHandler):

    page_name = 'error'

    def initialize(self, status_code):
        super().initialize()
        self.set_status(status_code)

    async def get_page(self):
        self.put_state({
            'pageError': {
                'code': self._status_code,
            },
        })
