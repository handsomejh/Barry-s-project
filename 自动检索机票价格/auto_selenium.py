from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
import smtplib
import ssl
from email.message import EmailMessage


class Auto_Selenium(object):
    def __init__(self):
        options = Options()
        options.add_argument('--headless')  # 使用无头模式
        self.driver = webdriver.Chrome(options=options)

    def open_website(self):
        self.driver.get("https://www.ctrip.com/")
        self.driver.maximize_window()
        # login = self.driver.find_element(By.XPATH, '//span[text()="请登录"]')
        # login.click()
        # username=self.driver.find_element(By.XPATH, '//input[@id="nloginname"]')
        # password=self.driver.find_element(By.XPATH, '//input[@id="npwd"]')
        # username.send_keys("15651790925")
        # password.send_keys("zhy98982")
        # label=self.driver.find_element(By.XPATH, '//*[@id="normalview"]/form/div[2]/div[2]/label')
        # label.click()
        # login=self.driver.find_element(By.XPATH, '//input[@id="nsubmit"]')
        # login.click()
        # time.sleep(10)

    def select_city(self, city):
        air_ticket = self.driver.find_element(By.XPATH, '//div[@class="pc_home-tabbtnIcon lsn_ico_9C9TD"]')
        air_ticket.click()
        air_ticket=self.driver.find_element(By.XPATH, '//span[text()="机票"]')
        air_ticket.click()
        air_ticket = self.driver.find_element(By.XPATH, '//a[text()="特价机票"]')
        air_ticket.click()
        air_ticket = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/i')
        air_ticket.click()
        air_ticket = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[1]/div[1]/div/div[1]/div[3]/div/div[2]/div[2]/div[1]/div/span/i')
        air_ticket.click()
        air_ticket = self.driver.find_element(By.XPATH, '//span[text()="从哪出发"]')
        air_ticket.click()
        time.sleep(2)
        air_ticket = self.driver.find_element(By.XPATH, '//div[text()="南京"]')
        air_ticket.click()
        time.sleep(5)
        # 查找所有的 <span> 元素
        span_elements = self.driver.find_elements(By.XPATH, "//div[@class='flight_list_item']//a[@class='flight_item_title_bd']/span")
        span_elements1 = self.driver.find_elements(By.XPATH, "//div[@class='flight_list_item']//div[@class='flight_item_price_bd']/a/span")
        # 遍历所有的 <span> 元素并获取它们的文本
        s = ''
        for span1, span2 in zip(span_elements, span_elements1):
            s = s+span1.text+span2.text
        s = s.replace("\r", " ").replace("\n", " ").replace("更多航班", "")

        new_text = re.sub(r'(?<=\d)([\u4e00-\u9fff]{2,})(?=\d)', r'\n\1\n', s)
        _, _, new_text = new_text.partition('\n')
        print(new_text)

    def send_mail(self,text):
        EMAIL_ADDRESS = "handsomejnn@163.com"
        EMAIL_PASSWORD = "LROQIPTHYDPWISLK"
        context = ssl.create_default_context()
        smtp = smtplib.SMTP_SSL('smtp.163.com', 465, context=context)
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = "特价机票信息"
        body = text
        msg=EmailMessage()
        msg['subject']=subject
        msg['From']=EMAIL_ADDRESS
        msg['To'] = "1378933213@qq.com"
        msg.set_content(body)
        smtp.send_message(msg)
        msg = EmailMessage()
        msg['subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = "875976418@qq.com"
        msg.set_content(body)
        smtp.send_message(msg)

        time.sleep(10)

    def close_browser(self):
        self.driver.close()