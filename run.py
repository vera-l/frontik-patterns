#!/usr/bin/env python3
import os

import tornado.options
from frontik.server import main

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
CONFIG = os.path.join(PROJECT_ROOT, 'config', 'frontik.cfg')

if __name__ == '__main__':
    tornado.options.define('serve_static', default=True, type=bool)
    main([CONFIG])
