from seleniumwire.webdriver import Remote
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverHandler:
    """
    Simple class-handler to work with requests to sites with or without js
    """
    def __init__(self, js_support=False, proxy_options=None):
        """
        Init method with optional options of js and proxy support
        :param js_support: default False
        :param proxy_options: default None, format: {"protocol": "protocol://user:pass@ip:port"}
        """
        self._driver = None

        if js_support:
            self._capabilities = DesiredCapabilities.HTMLUNITWITHJS.copy()
            # You can use one of the versions: https://clck.ru/W6mPK, default is 'firefox'
            # self._capabilities['version'] = 'chrome'
        else:
            self._capabilities = DesiredCapabilities.HTMLUNIT.copy()

        self._seleniumwire_opt = {
            'addr': '127.0.0.1'
        }

        if proxy_options:
            self._seleniumwire_opt.update({'proxy': proxy_options})

    def start_driver(self):
        """
        Method to start driver with described options and capabilities in init method
        :return:
        """
        try:
            self._driver = Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=self._capabilities,
                seleniumwire_options=self._seleniumwire_opt
            )
        except Exception as e:
            raise ConnectionError('Cannot connect to remote HtmlUnit driver')

        if self._driver:
            # self._driver.set_page_load_timeout(60)
            self._driver.implicitly_wait(60)
            self._driver.set_script_timeout(60)

    def get(self, url, params=None, xpath=None):
        """
        Method to make a request to the site
        :param url: url of the site
        :param params: query string, optional
        :param xpath: path to search, optional
        :return:
        """

        if not self._driver:
            return None

        final_url = url
        if params:
            params_string = '&'.join('{}={}'.format(key, value) for key, value in params.items())
            final_url = '{}?{}'.format(url, params_string)
        try:
            self._driver.get(final_url)
        except:
            return None

        if not xpath:
            return self._driver.page_source

        try:
            WebDriverWait(self._driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except:
            return None

        return self._driver.page_source

    def kill_driver(self):
        """
        Method to close session
        :return:
        """
        if self._driver:
            self._driver.quit()

    def update_driver(self):
        """
        Method to restart the driver for example to set another proxy
        :return:
        """
        self.kill_driver()
        self.start_driver()

    def __del__(self):
        """
        Method that calls kill_driver on object destruction
        :return:
        """
        self.kill_driver()
