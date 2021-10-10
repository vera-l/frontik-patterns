from tornado import gen

from frontik.handler import PageHandler


@gen.coroutine
def get_result(handler, duration):
    result = yield handler.get_url(
        '0.0.0.0:8000',
        '/example_request',
        data={'duration': duration},
    )
    if result.failed:
        return 0
    return result.data['time']


class Page(PageHandler):
    default_action = 'tornado_coro_parallel_coro'

    def get_page(self):
        results = yield [
            get_result(self, 0.1),
            get_result(self, 0.2),
            get_result(self, 0.3),
            get_result(self, 0.4),
        ]

        self.json.put({
            'status': 'ok',
            'time': max(results),
        })
