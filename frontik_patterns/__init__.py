from frontik.app import FrontikApplication
from lxml import etree

from frontik_patterns.pages import error_page
from frontik_patterns.urls import URLS
from frontik_patterns.version import version


class FrontikPatternsApplication(FrontikApplication):

    def __init__(self, **settings):
        super().__init__(**settings)

    async def init(self):
        await super().init()

    def application_urls(self):
        return URLS

    def application_version_xml(self):
        version_xml = etree.Element('version')
        version_xml.text = version
        return (
            version_xml,
        )

    def application_404_handler(self, _):
        return error_page.Page, {'status_code': 404}
