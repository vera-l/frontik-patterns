from frontik.handler import PageHandler


class Page(PageHandler):
    default_action = 'tornado_coro_parallel'

    def get_page(self):
        result1, result2, result3, result4 = yield [
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            ),
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            ),
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            ),
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            ),
        ]

        self.json.put({
            'status': 'ok',
            'time': max([
                result.data['time'] for result in (result1, result2, result3, result4)
            ]),
        })
