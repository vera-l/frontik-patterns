from frontik.handler import AwaitablePageHandler, PageHandler, HTTPErrorWithPostprocessors


class FrontikPatternsPageHandler(AwaitablePageHandler):
    page_name = None
    report_name = None

    preprocessors = []

    def get_debug_argument(self, argument_name):
        value = self.get_argument(argument_name, self.get_cookie(argument_name, None))
        if value is not None:
            self.require_debug_access()
            return value
