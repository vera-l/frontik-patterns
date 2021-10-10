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
    time_ = result.data['time']
    handler.log.info(f'Task request time {time_}s')
    return time_


class Page(AwaitablePageHandler):
    default_action = 'async_coro_tasks'

    async def get_page(self):
        task = self.run_task(get_result(self, 1.1))

        await asyncio.gather(
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
        )
        await self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.4},
        )
        # await task
        await asyncio.gather(
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
        )

        self.json.put({
            'status': 'ok',
        })
