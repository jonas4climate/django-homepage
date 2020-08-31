from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

   def setUp(self):
      options = ChromeOptions()
      webdriver.get()
      self.browser = webdriver.

   def tearDown(self):
      self.browser.quit()

   def test_can_see_blogs_on_homepage(self):
      # Sarah has heard about a cool new online blog. She goes
      # to check out its homepage
      self.browser.get('http://localhost:8000')

      # She notices the owner's name in the blog's browser title
      self.assertIn('Jonas', self.browser.title)
      # as well as a large text mentioning blog on the website
      header_text = self.browser.find_element_by_tag_name('h1').text  
      self.assertIn('Blog', header_text)
      
      self.fail('Finish the test!')
      
      

if __name__ == '__main__':  
   unittest.main(warnings='ignore')