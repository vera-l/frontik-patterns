from frontik.handler import PageHandler


class Page(PageHandler):
    default_action = 'tornado_coro_parallel_dict'

    def get_page(self):
        coro_dict = {
            'result1': self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            ),
            'result2': self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            ),
            'result3': self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            ),
            'result4': self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            )
        }

        result = yield coro_dict

        self.json.put({
            'status': 'ok',
            'time': result['result1'].data['time'],
        })
