from selenium import webdriver
from  selenium.webdriver.common.by  import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest  # 需要引入 unittest、time、 等程式
from selenium.webdriver.common.keys import Keys
import random
import time
from .Keyword import *

class test_user(unittest.TestCase):  # 測試項目
    def setUp(self):
        self.url="http://127.0.0.1:3000/"  # 要執行自動測試的網站

    def test_create_user(self):
        test=webdriver.Chrome()
        test.get( self.url )
        test.maximize_window()
        login( test )
        sub_tab_go_to_page( test, 'users' )
        # precondition 
        get_web_element( test, '//button[contains(normalize-space(), "Create")]' ).click() 
        input_field( test, 'name.first', 'ChunPing' )
        input_field( test, 'name.last', 'Chu' )
        input_field( test, 'email', 'iamgp@ntut.org.tw' )
        input_field( test, 'password', 'james0000' )

        input_field( test, 'password', '12345678' )
        input_field( test, 'password_confirm', '12345678' )
        password = get_web_element( test, '//input[contains( @name , "password") ]' ).get_attribute('value')
        self.assertEqual( password, '12345678' )

        input_field( test, 'password', '!@#$%^&*' )
        input_field( test, 'password_confirm', '!@#$%^&*' )
        password = get_web_element( test, '//input[contains( @name , "password") ]' ).get_attribute('value')
        self.assertEqual( password, '!@#$%^&*' )
        
        input_field( test, 'password', 'james0000' )
        input_field( test, 'password_confirm', 'james0000' )
        password = get_web_element( test, '//input[contains( @name , "password") ]' ).get_attribute('value')
        self.assertEqual( password, 'james0000' )
        
        get_web_element( test, '//button[contains(@type, "submit") and contains(normalize-space(), "Create")]' ).click() 
        
        input_field( test, 'phone', "035824384" )
        input_field( test, 'phone', "0962010830" )
        get_web_element( test, '//*[contains( @data-button , "update") ]' ).click()
        top_tab_go_to_page( test, 'users' )

        exist = is_text_present( test, 'ChunPing Chu' )
        self.assertTrue( exist )
        exist = is_text_present( test, 'iamgp@ntut.org.tw' )
        self.assertTrue( exist )
        exist = is_text_present( test, '0962010830' )
        self.assertTrue( exist )
        time.sleep(2)
        test.close()


if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(test_user("test_create_user"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testsuite)