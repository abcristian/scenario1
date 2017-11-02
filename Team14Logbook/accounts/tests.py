from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/sonik/Downloads/chromedriver')
		super(LoginTest, self).setUp()
	def tearDown(self):
		self.driver.quit()
		super(LoginTest, self).tearDown()
	def test_login(self):
		driver = self.driver
		driver.get('http://127.0.0.1:8000/login/')
		driver.find_element_by_id("id_username").send_keys("admin")
		driver.find_element_by_id("id_password").send_keys("password123")
		driver.find_element_by_css_selector("input[type=submit]").click()
		time.sleep(1)


class AddPostTest(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/sonik/Downloads/chromedriver')
		super(AddPostTest, self).setUp()
	def tearDown(self):
		self.driver.quit()
		super(AddPostTest, self).tearDown()
	def test_addpost(self):
		driver = self.driver
		driver.get('http://127.0.0.1:8000/login/')
		driver.find_element_by_id("id_username").send_keys("admin")
		driver.find_element_by_id("id_password").send_keys("password123")

		time.sleep(1)