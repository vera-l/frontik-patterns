import asyncio

from frontik.handler import AwaitablePageHandler


async def get_result(handler, duration):
    result = await handler.get_url(
        '0.0.0.0:8000',
        '/example_request',
        data={'duration': duration},
    )
    if result.failed:
        return 0
    return result.data['time']


class Page(AwaitablePageHandler):
    default_action = 'async_coro_parallel_coro'

    async def get_page(self):
        results = await asyncio.gather(
            *[
                get_result(self, 0.1),
                get_result(self, 0.2),
                get_result(self, 0.3),
                get_result(self, 0.4),
            ]
        )

        self.json.put({
            'status': 'ok',
            'time': max(results),
        })
