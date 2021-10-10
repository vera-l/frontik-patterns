from frontik_patterns.pages import index, example_request
from frontik_patterns.pages.async_coro import (
    tasks as async_coro_tasks,
    serial as async_coro_serial,
    parallel as async_coro_parallel,
    parallel_dict as async_coro_parallel_dict,
    parallel_coro as async_coro_parallel_coro
)
from frontik_patterns.pages.tornado_coro import (
    tasks as tornado_coro_tasks,
    serial as tornado_coro_serial,
    parallel as tornado_coro_parallel,
    parallel_dict as tornado_coro_parallel_dict,
    parallel_coro as tornado_coro_parallel_coro
)
from frontik_patterns.pages.tornado_callbacks import (
    tasks as tornado_callbacks_tasks,
    serial as tornado_callbacks_serial,
    parallel as tornado_callbacks_parallel
)


def url(matcher):
    return r'^{}/?(?:\?.*)?$'.format(matcher)


URLS = [
    # Main
    (url(r'/'), index.Page),
    (url(r'/example_request'), example_request.Page),

    # Native coroutines
    (url(r'/async_coro/serial'), async_coro_serial.Page),
    (url(r'/async_coro/parallel'), async_coro_parallel.Page),
    (url(r'/async_coro/parallel_dict'), async_coro_parallel_dict.Page),
    (url(r'/async_coro/parallel_coro'), async_coro_parallel_coro.Page),
    (url(r'/async_coro/tasks'), async_coro_tasks.Page),

    # Tornado coroutines (deprecated)
    (url(r'/tornado_coro/serial'), tornado_coro_serial.Page),
    (url(r'/tornado_coro/parallel'), tornado_coro_parallel.Page),
    (url(r'/tornado_coro/parallel_dict'), tornado_coro_parallel_dict.Page),
    (url(r'/tornado_coro/parallel_coro'), tornado_coro_parallel_coro.Page),
    (url(r'/tornado_coro/tasks'), tornado_coro_tasks.Page),

    # Tornado callbacks (deprecated)
    (url(r'/tornado_callbacks/serial'), tornado_callbacks_serial.Page),
    (url(r'/tornado_callbacks/parallel'), tornado_callbacks_parallel.Page),
    (url(r'/tornado_callbacks/tasks'), tornado_callbacks_tasks.Page),

    # Default rule
    # (r'.*', error_page.Page)
]
