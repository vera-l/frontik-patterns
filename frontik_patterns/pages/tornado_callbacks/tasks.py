from frontik.handler import PageHandler
from frontik.futures import AsyncGroup


class Page(PageHandler):
    default_action = 'tornado_callbacks_tasks'

    def get_page(self):
        # task
        self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 1.1},
        )

        # the second parallel group

        def finish_cb2():
            pass

        def cb2(json, response):
            async_group2 = AsyncGroup(finish_cb2)

            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.1},
                callback=async_group2.add(cb),
            )
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.2},
                callback=async_group2.add(cb),
            )

        # single request between two parallel requests groups

        def finish_cb():
            self.get_url(
                '0.0.0.0:8000',
                '/example_request',
                data={'duration': 0.4},
                callback=cb2
            )

        # the first parallel group

        async_group1 = AsyncGroup(finish_cb)

        def cb(json, response):
            pass

        self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.1},
            callback=async_group1.add(cb),
        )
        self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.2},
            callback=async_group1.add(cb),
        )
        self.get_url(
            '0.0.0.0:8000',
            '/example_request',
            data={'duration': 0.3},
            callback=async_group1.add(cb),
        )

        self.json.put({
            'status': 'ok',
        })
