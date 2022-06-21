import re
import os
import apify
import logging
from scrapy import Spider
from urllib.parse import urljoin
from apify_client import ApifyClient
from scrapy.http.request import Request


class ASINsExtractor(Spider):

    name = 'asins_extractor'

    headers = {'Host': 'www.amazon.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'en-GB,en;q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1',}

    logger = None

    first_page_only = False
    total_number_of_inputs_urls = 0
    #input_url = ['https://www.amazon.com/s?k=python']
    input_url = 'https://www.amazon.com/s?k=python'

    directory_path = os.getcwd()

    def start_requests(self):

        self.logger = logging.getLogger()

        if 'Dropbox' not in self.directory_path:

            # Initialize the main ApifyClient instance
            client = ApifyClient(os.environ['APIFY_TOKEN'], api_url=os.environ['APIFY_API_BASE_URL'])

            # Get the resource subclient for working with the default key-value store of the actor
            default_kv_store_client = client.key_value_store(os.environ['APIFY_DEFAULT_KEY_VALUE_STORE_ID'])

            # Get the value of the actor input and print it
            self.logger.info('Loading input...')
            actor_input = default_kv_store_client.get_record(os.environ['APIFY_INPUT_KEY'])['value']
            self.logger.info(actor_input)

            self.input_url = actor_input["inputs_urls"]
            self.first_page_only = actor_input["first_page_only"]

        #for input_url in self.inputs_urls:
        yield Request(url=self.input_url,
                      headers=self.headers,
                      callback=self.parse_overview_page)

    def parse_overview_page(self, response):

        results = response.xpath('.//div/@data-asin')
        if results and len(results) > 0:
            results = results.extract()
            for result in results:
                if result != '':
                    obj = {'ASIN': result,
                           'Overview Page URL': response.url}

                    if 'Dropbox' not in self.directory_path:
                        apify.pushData(obj)
                    else:
                        yield apify

        if not self.first_page_only:
            next_url = response.xpath('.//a[contains(@class, "s-pagination-item s-pagination-next")]/@href')
            if next_url and len(next_url) > 0:
                next_url = next_url.extract()[0]
                next_url = urljoin(self.base_url, next_url)
                yield Request(url=next_url,
                              meta=response.meta,
                              headers=self.headers,
                              callback=self.parse_overview_page)
