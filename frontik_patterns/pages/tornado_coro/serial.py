from tornado import gen

from frontik.handler import PageHandler


class Page(PageHandler):
    default_action = 'tornado_coro_serial'

    def get_page(self):
        result1 = yield self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.2},
            fail_fast=True,
        )

        if not result1.failed:
            result2 = yield self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
                fail_fast=True,
            )

            if not result2.failed:
                result3 = yield self.get_url(
                    '0.0.0.0:8000',
                    '/example_request',
                    data={'duration': 0.2},
                    fail_fast=True,
                )

                if not result3.failed:
                    result4 = yield self.get_url(
                        '0.0.0.0:8000',
                        '/example_request',
                        data={'duration': 0.2},
                        fail_fast=True,
                    )

        self.json.put({
            'status': 'ok',
            'time': sum([
                result.data['time'] for result in (result1, result2, result3, result4)
            ]),
        })
