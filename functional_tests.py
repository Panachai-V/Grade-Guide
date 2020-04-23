from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # def test_page_layout(self):
    #     # เอิร์ธได้ยินมาว่ามีเว็บในการคำนวณเกรดและอยากจะใช้งาน
    #     # จึงเข้าเว็บไปที่หน้า Homepage
    #
    #     self.browser.get('http://localhost:8000')
    #
    #     # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า GRADEGUIDE
    #     self.assertIn('', self.browser.title)
    #     header_text = self.browser.find_element_by_tag_name('head_text').text
    #     self.assertIn('GRADEGUIDE', header_text)
    #
    #     # เขาสังเกตุเห็นว่าในหน้าจะมีลิงคหน้า grade guird
    #     homepage_link = self.browser.find_element_by_tag_name('gradguide_link').text
    #     self.assertIn('GRADEGUIDE', homepage_link)
    #
    #     # เขาสังเกตุเห็นว่าในหน้าจะมีลิงคหน้า sign up
    #     signup_link = self.browser.find_element_by_tag_name('signup_link').text
    #     self.assertEqual('SIGN UP', signup_link)
    #
    #     # เขาสังเกตุเห็นว่าในหน้าจะมีลิงคหน้า log in
    #     login_link = self.browser.find_element_by_tag_name('login_link').text
    #     self.assertIn('LOG IN', login_link)
    #
    #     # เขาสังเกตุเห็นว่าในหน้าจะมีลิงคหน้า flow
    #     flow_link = self.browser.find_element_by_tag_name('flow_link').text
    #     self.assertIn('FLOW', flow_link)
    #
    #     # เขาสังเกตุเห็นว่าในหน้าจะมีลิงคหน้า about
    #     about_link = self.browser.find_element_by_tag_name('about_link').text
    #     self.assertIn('ABOUT', about_link)
    #
    #     # เขาสังเกตุเห็นว่าในหน้าจะมีลิงคหน้า help
    #     help_link = self.browser.find_element_by_tag_name('help_link').text
    #     self.assertIn('HELP', help_link)
    #
    #     # ภายในหน้านั้นจะมีคำว่า Welcome to GradeGuide !
    #     welcome_text = self.browser.find_element_by_tag_name('h2').text
    #     self.assertIn('Welcome to GradeGuide !', welcome_text)
    #
    #     # จะมีจำนวนผู้สมัครเพื่อแสดงความนิยมของเว็บไซต์อีกด้วย
    #     totaluser_text = self.browser.find_element_by_tag_name('p').text
    #     self.assertIn('Total users registered:', totaluser_text)
    #
    #     # เขาลองคลิกปุ่ม log in
    #     login_click = self.browser.find_element_by_tag_name('login_link')
    #     login_click.click()
    #
    #     # เขายังเห็นว่ายังอยู่ภายในเว็บ grade guide อยุ่
    #     self.assertIn('', self.browser.title)
    #     header_text = self.browser.find_element_by_tag_name('head_text').text
    #     self.assertIn('GRADEGUIDE', header_text)
    #
    #     # มีช่องที่สำหรับใส่ username
    #     username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
    #     self.assertIn('Username:', username_label)
    #     username_box = self.browser.find_element_by_id("id_username")
    #     self.assertEqual(username_box.get_attribute('type'),'text')
    #
    #     # มีช่องที่สำหรับใส่ password
    #     password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
    #     self.assertIn('Password:', password_label)
    #     password_box = self.browser.find_element_by_id("id_password")
    #     self.assertEqual(password_box.get_attribute('type'),'password')
    #
    #     # และมีปุ่มสำหรับ log in อีกด้วย
    #     login_button = self.browser.find_element_by_tag_name("button")
    #     self.assertEqual(login_button.get_attribute('type'),'button')
    #
    #     self.fail('Finish the test!')
    #
    # def test_login_fail(self):
    #     # เขาเข้าไปที่หน้า login
    #     self.browser.get('http://127.0.0.1:8000/accounts/login/')
    #     header_text = self.browser.find_element_by_tag_name('h2').text
    #     self.assertIn('Log in', header_text)
    #
    #     # เขาใส่ id และ password ลงไป
    #     username_login_box = self.browser.find_element_by_id('id_username')
    #     password_login_box = self.browser.find_element_by_id('id_password')
    #     username_login_box.send_keys('dummy_username')
    #     password_login_box.send_keys('dummy_password')
    #
    #     # เขากดปุ่ม log in
    #     login_button = self.browser.find_element_by_tag_name('login_button')
    #     login_button.click()
    #
    #     # เขาไม่สามารถ log in ได้
    #     error_message = self.browser.find_element_by_tag_name('test_tag').text
    #     self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',error_message)
    #     self.fail('Finish the test!')
    #
    #
    # def test_user_can_signup_and_login(self):
    #     # เมื่อเขากดเข้าไปที่หน้า signup
    #     self.browser.get('http://localhost:8000/signup')
    #
    #     username_box = self.browser.find_element_by_id('id_username')
    #     password_box = self.browser.find_element_by_id('id_password1')
    #     password_box2 = self.browser.find_element_by_id('id_password2')
    #
    #     # เขาทำการสมัคร username jesselingard
    #     # password lingard123456789
    #     # password2 lingard123456789
    #     username_box.send_keys('jesselingard')
    #     password_box.send_keys('lingard123456789')
    #     password_box2.send_keys('lingard123456789')
    #     # เขาทำการกดปุ่ม signup
    #     signup_button = self.browser.find_element_by_tag_name('signup_button')
    #     signup_button.click()
    #
    #
    #     # เขาเข้าไปที่หน้า login
    #     self.browser.get('http://127.0.0.1:8000/accounts/login/')
    #     header_text = self.browser.find_element_by_tag_name('h2').text
    #     self.assertIn('Log in', header_text)
    #
    #     # เขาใส่ id password
    #     username_login_box = self.browser.find_element_by_id('id_username')
    #     password_login_box = self.browser.find_element_by_id('id_password')
    #     username_login_box.send_keys('jesselingard')
    #     password_login_box.send_keys('lingard123456789')
    #
    #     # เขากดปุ่ม login
    #     login_button = self.browser.find_element_by_tag_name('login_button')
    #     login_button.click()
    #
    #
    #     # เขาเข้าไปที่หน้า homepage
    #     self.browser.get('http://127.0.0.1:8000/home')
    #     id_user = self.browser.find_element_by_tag_name('id_text').text
    #     self.assertIn('jesselingard', id_user)
    #     self.fail('Finish the test!')
    #
    # def test_subjects_button_flow(self):
    #     # เธอคลิกเข้ามาที่ link flow
    #     self.browser.get('http://localhost:8000/flow.html')
    #
    #
    #     # test Flow H1 text
    #     # เธอเห็นคำว่า Flow ซึ่งเป็นหัวข้อใหญ่
    #     header_text = self.browser.find_element_by_tag_name('h1').text
    #     self.assertEqual('Flow', header_text)
    #
    #     # เธอเห็นประโยคที่อยู่ก่อนหน้าปุ่ม subjects
    #     defination = self.browser.find_element_by_tag_name('p1').text
    #     self.assertIn('If you can not remember a name of your subject , The Subjects button will help you. :)',defination)
    #
    #     # test subjects button
    #     # เธอจำชื่อวิชาไม่ได้
    #     # เธอจึงคลิกไปที่ปุ่ม subjects เพื่อที่เธอจะได้ดูชื่อวิชา
    #     subject_button = self.browser.find_element_by_id('subject_button')
    #     subject_button.click()
    #     self.fail('Finish the test!')
    #
    # def test_search_flow(self):
    #     # เธอคลิกเข้ามาที่ link flow
    #     self.browser.get('http://localhost:8000/flow.html')
    #
    #     self.assertIn('', self.browser.title)
    #
    #     # test search box
    #     # เธอเห็นช่องสำหรับใส่ชื่อวิชาเพื่อค้นหาวิชาที่เป็นตัวต่อกัน
    #     # เธอจึงพิมพ์วิชา Programming Fundamental ลงไป
    #     subject_placeholder = self.browser.find_element_by_id('search_placeholder')
    #     self.assertEqual(subject_placeholder.get_attribute('type'),'text')
    #     subject_placeholder.send_keys('Programming Fundamental')
    #
    #
    #     # test submit button
    #     # เธอจึงกดปุ่ม search เพื่อทำการหาตัวต่อของวิชา Programming Fundamental
    #     submit_button = self.browser.find_element_by_id('submit_button')
    #     self.assertEqual(submit_button.get_attribute('type'),'submit')
    #     submit_button.click()
    #
    #
    #     # test input Search text
    #     # เธอเห็นหัวข้อ subject
    #     # หลังจากที่เธอกด search แล้ว เธอพบว่าวิชาที่เธฮ search ไปปรากฏอยู่หลังหัวข้อ subject
    #     subject_head = self.browser.find_element_by_tag_name('h2').text
    #     self.assertEqual('subject : Programming Fundamental', subject_head)
    #
    #     # test search result
    #     # เธอเห็นผลของการ search ของเธอ หลังจากที่กดปุ่ม search ไป
    #     result_search = self.browser.find_element_by_tag_name('p2').text
    #     self.assertEqual('Semister2 : Algorithms and Data Structures\nSemister5 : Operating Systems',result_search)
    #
    #     # test Note
    #     # เธอเห็นประโยคด้านล่างเกี่ยวกับวิชาเลือก
    #     note = self.browser.find_element_by_tag_name('p3').text
    #     self.assertEqual('Note : Elective Subjects don\'t connect to each other but I want to show how many elective subjects are in this flow.', note)
    #     self.fail('Finish the test!')
    #
    # def test_flow_pic(self):
    #     # เธอคลิกเข้ามาที่ link flow
    #     self.browser.get('http://localhost:8000/flow.html')
    #
    #
    #     # test fullflow button
    #     # เธออยากดูภาพรวมของวิชาทั้งหมดที่เธอต้องเรียน
    #     # เธอจึงคลิกไปที่ปุ่ม Full Flow เพื่อไปยังรูป flow
    #     flow_button = self.browser.find_element_by_id('fullflow_button')
    #     flow_button.click()
    #
    #     # test can find the flow picture
    #     # เธอเห็นภาพวิชาตัวต่อทั้งหมด
    #     flow_image = self.browser.find_element_by_id('image')
    #     self.assertEqual(flow_image.get_attribute('id'),'image')
    #     self.fail('Finish the test!')


    def test_submit_grade(self):
        # เมื่อเขากดเข้าไปที่หน้า signup
        self.browser.get('http://localhost:8000/signup')
        username_box = self.browser.find_element_by_id('id_username')
        password_box = self.browser.find_element_by_id('id_password1')
        password_box2 = self.browser.find_element_by_id('id_password2')

        # เขาทำการสมัคร username jesselingard
        # password lingard123456789
        # password2 lingard123456789
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        password_box2.send_keys('lingard123456789')

        # เขาทำการกดปุ่ม signup
        signup_button = self.browser.find_element_by_tag_name('signup_button')
        signup_button.click()

        # เขาเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', header_text)

        # เขาใส่ id password
        username_login_box = self.browser.find_element_by_id('id_username')
        password_login_box = self.browser.find_element_by_id('id_password')
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')

        # เขากดปุ่ม login
        login_button = self.browser.find_element_by_tag_name('login_button')
        login_button.click()
        time.sleep(2)

        # เขาเข้าไปที่หน้า homepage
        self.browser.get('http://127.0.0.1:8000/home')
        id_user = self.browser.find_element_by_tag_name('id_text').text
        self.assertIn('jesselingard', id_user)

        # เขาใส่ unit
        select_unit_1 = Select(self.browser.find_element_by_id('subject1Unitid'))
        select_unit_1.select_by_visible_text('Unit: 2')
        select_unit_2 = Select(self.browser.find_element_by_id('subject2Unitid'))
        select_unit_2.select_by_visible_text('Unit: 3')
        select_unit_3 = Select(self.browser.find_element_by_id('subject3Unitid'))
        select_unit_3.select_by_visible_text('Unit: 4')
        select_unit_4 = Select(self.browser.find_element_by_id('subject4Unitid'))
        select_unit_4.select_by_visible_text('Unit: 1')
        time.sleep(5)

        # เขาใส่ Grade
        select_grade_1 = Select(self.browser.find_element_by_id('subject1Gradeid'))
        select_grade_1.select_by_value('4')
        select_grade_2 = Select(self.browser.find_element_by_id('subject2Gradeid'))
        select_grade_2.select_by_value('3.5')
        select_grade_3 = Select(self.browser.find_element_by_id('subject3Gradeid'))
        select_grade_3.select_by_value('0')
        select_grade_4 = Select(self.browser.find_element_by_id('subject4Gradeid'))
        select_grade_4.select_by_value('1.5')
        time.sleep(5)

        # เขาเห็นเกรดแสดงขึ้นมา
        submit_button = self.browser.find_element_by_tag_name('calculate_button')
        submit_button.click()
        grade_result = self.browser.find_element_by_tag_name('grade_result').text
        self.assertIn('2.00', grade_result)


        # เขาเห็นสาถานะนักศึกษาของเขา
        state_result = self.browser.find_element_by_tag_name('state_result').text
        self.assertIn('Normal State', state_result)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
