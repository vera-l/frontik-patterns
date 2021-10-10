from frontik.handler import PageHandler
from frontik.futures import AsyncGroup


class Page(PageHandler):
    default_action = 'tornado_callbacks_parallel'

    def get_page(self):

        times = []

        def finish_cb():
            self.log.info(f'requests times: {times}')
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.1},
            )

        def cb(json, response):
            times.append(0 if response.code != 200 or json is None else json['time'])

        async_group = AsyncGroup(finish_cb)

        self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.1},
            callback=async_group.add(cb),
        )
        self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.2},
            callback=async_group.add(cb),
        )
        self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.3},
            callback=async_group.add(cb),
        )

        self.json.put({
            'status': 'ok',
        })
