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
    time_ = result.data['time']
    yield gen.sleep(0.1)  # To send response before logging
    handler.log.info(f'Task request time {time_}s')
    return time_


class Page(PageHandler):
    default_action = 'tornado_coro_serial'

    def get_page(self):
        fut = get_result(self, 1.1)
        self.finish_group.add_future(fut)

        yield [
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.1},
            ),
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            ),
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.3},
            )
        ]
        yield self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.4},
        )
        # yield fut
        yield [
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.1},
            ),
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
            )
        ]

        self.json.put({
            'status': 'ok',
        })
