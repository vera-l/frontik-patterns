import asyncio

from frontik.handler import AwaitablePageHandler


class Page(AwaitablePageHandler):
    default_action = 'example_request'

    async def get_page(self):
        duration = float(self.get_argument('duration'))
        await asyncio.sleep(duration)

        self.json.put({
            'status': 'ok',
            'time': duration,
        })
