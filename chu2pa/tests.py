from django.test import TestCase, LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from django.core.urlresolvers import reverse
# Create your tests here.
from chu2pa.models import UserStatus
from time import sleep

class SeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_login_page(self):
        UserStatus.objects.create_user(
            username='abc',
            password='1234')

        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('login')))
        # let's fill out the form with our superuser's username and password
        self.selenium.find_element_by_name('username').send_keys('abc')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('1234')

        # Submit the form
        password_input.send_keys(Keys.RETURN)
        # sleep for half a second to let the page load
        sleep(.5)

        body = self.selenium.find_element_by_tag_name('body')
        print body.text
        self.assertIn(', good to see you again!', body.text)