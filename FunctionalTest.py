# from selenium import webdriver
# import unittest
# from selenium.webdriver.common.keys import Keys
# import time
# from django.test import LiveServerTestCase

# """class PageTest(LiveServerTestCase.TestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()"""

# cWait = 2
# class PageTest(LiveServerTestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()
# 	#def tearDown(self):
# 	#	self.browser.quit()

# 	def check_rows_in_listtable(self, row_text):
# 		start_time = time.time()
# 		while time.time()-start_time<cWait:
# 		#	time.sleep(0.2)
# 			try:
# 				table = self.browser.find_element_by_id('scheduleTable')
# 				rows = table.find_elements_by_tag_name('tr')
# 				self.assertIn(row_text,[row.text for row in rows])
# 				return
# 			except (AssertionError,WebDriverException) as e:
# 				if time.time()-start_time>cWait:
# 					raise e
		
# 	def test_start_list_and_retrieve_it(self):
# 		"""self.browser.get('http://localhost:8000')"""
# 		self.browser.get(self.live_server_url)
# 		self.assertIn('PT Schedule', self.browser.title)
# 		headerText = self.browser.find_element_by_tag_name('h1').text
# 		self.assertIn('Schedule Form', headerText)
# 		inpName = self.browser.find_element_by_id('studentName')
# 		inpNameF = self.browser.find_element_by_id('FstudentName')
# 		inpNameL = self.browser.find_element_by_id('LstudentName')
# 		inpNameM = self.browser.find_element_by_id('MstudentName')
# 		btn_button = self.browser.find_element_by_id('btn')
# 		self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
# 		inpName.click()
# 		inpName.send_keys('Scathach')
# 		time.sleep(1)
# 		inpNameF.send_keys('Skadi')
# 		time.sleep(1)
# 		inpNameL.send_keys('Morgan')
# 		time.sleep(1)
# 		inpNameM.send_keys('Eresh')
# 		time.sleep(1)
# 		btn_button.click()
# 		time.sleep(1)

# 	def test_start_list_and_retrieve_it_test_ulit(self):
# 		"""self.browser.get('http://localhost:8000')"""
# 		self.browser.get(self.live_server_url)
# 		self.assertIn('PT Schedule', self.browser.title)
# 		headerText = self.browser.find_element_by_tag_name('h1').text
# 		self.assertIn('Schedule Form', headerText)
# 		inpName = self.browser.find_element_by_id('studentName')
# 		inpNameF = self.browser.find_element_by_id('FstudentName')
# 		inpNameL = self.browser.find_element_by_id('LstudentName')
# 		inpNameM = self.browser.find_element_by_id('MstudentName')
# 		btn_button = self.browser.find_element_by_id('btn')
# 		self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
# 		inpName.click()
# 		inpName.send_keys('Dale')
# 		time.sleep(1)
# 		inpNameF.send_keys('Jean')
# 		time.sleep(1)
# 		inpNameL.send_keys('Maliksi')
# 		time.sleep(1)
# 		inpNameM.send_keys('Carlet')
# 		time.sleep(1)
# 		btn_button.click()
# 		time.sleep(1)

# 		self.check_rows_table('1: Dale Jean Maliksi Carlet')

# 	def checking_if_in_table_list(self,row_test):
# 		save_time =time.time()
# 		while time.time()-save_time<CWAIT:
# 			time.sleep(0.5)
# 			try:
# 				table = self.browser.find_element_by_id('scheduleTable')
# 				rows = table.find_elements_by_tag_name('tr')
# 				self.assertIn(row_text,[row.text for row in rows])
# 				return
# 			except (AssertionError,no entry) as e:
# 				if time.time()-save_time>CWAIT:
# 					raise e
# 				time.sleep(1)


# 		"""table = self.browser.find_element_by_id('scheduleTable')
# 		rows = table.find_elements_by_tag_name('tr')
# 		self.assertIn('1: Scathach', [rows.text for rows in rows])"""

# """if __name__ == '__main__':
# 	unittest.main(warnings='ignore')"""


