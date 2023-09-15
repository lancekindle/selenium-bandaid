import sys
import os
import subprocess
from selenium_bandaid import RefetchStaleDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

class WebDriverSetup():
    ''' inherit from this base in your selenium tests. Will set up browser with working config
        just make sure to DELETE setup_method() in your test class!!
    '''

    @property
    def _ubuntu_version(self):
        try:
            with open('/etc/os-release', 'r') as os_release_file:
                for line in os_release_file:
                    if line.startswith('PRETTY_NAME='):
                        return line.split('=')[1].strip().strip('"')
        except Exception:
            pass
        return ''

    def setup_method(self, method):
        options = Options()
        # supply --headless=false when running pytest in order to see browser
        if '--headless=true' in sys.argv:
            options.add_argument('-headless')  # in chrome, you probably want -headless=new
        service = Service(log_output=os.path.devnull)  # log_output=devnull is just to silence a deprecation warning
        if self._ubuntu_version.startswith('Ubuntu 22.04'):
            # workaround for default install of firefox on ubuntu 22.04
            try:
                result = subprocess.check_output(["which", "geckodriver"], stderr=subprocess.STDOUT, text=True)
                geckodriver_path = result.strip()
                service = Service(executable_path=geckodriver_path, log_output=os.path.devnull)
            except subprocess.CalledProcessError as e:
                pass

        self.driver = RefetchStaleDriver(options=options, service=service)  # it's Firefox improved
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Enable headless mode
        # self.driver = webdriver.Chrome(options=options)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
