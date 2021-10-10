from frontik.handler import PageHandler

REQUESTS = 4


class Page(PageHandler):
    default_action = 'tornado_callbacks_serial'

    def get_page(self):
        i = 0

        def cb(data, response):
            nonlocal i
            i += 1

            if i < REQUESTS:
                self.get_url(
                    '0.0.0.0:8000',
                    '/example_request',
                    data={'duration': 0.5},
                    callback=cb,
                )

        self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.5},
            callback=cb,
        )

        self.json.put({
            'status': 'ok',
        })
