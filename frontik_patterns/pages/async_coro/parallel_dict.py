from frontik.handler import AwaitablePageHandler
from frontik.util import gather_dict


class Page(AwaitablePageHandler):
    default_action = 'async_coro_parallel_dict'

    async def get_page(self):
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

        result = await gather_dict(coro_dict=coro_dict)

        self.json.put({
            'status': 'ok',
            'time': result['result1'].data['time'],
        })
