import asyncio

from frontik.handler import AwaitablePageHandler


class Page(AwaitablePageHandler):
    default_action = 'async_coro_parallel'

    async def get_page(self):
        result1, result2, result3, result4 = await asyncio.gather(
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
            )
        )

        self.json.put({
            'status': 'ok',
            'time': max([
                result.data['time'] for result in (result1, result2, result3, result4)
            ]),
        })
