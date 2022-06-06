import  os
import booking.constant as const
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys



class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\webdriver",teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, *args):
        if self.teardown:
            self.quit()

    def landing_page(self):
        self.get(const.BASE_URL)

    def select_category(self,category=None):
        category_link = self.find_element_by_link_text(f'{category}')
        category_link.click()

    def search_brand(self,brand):
        search_field = self.find_element_by_id("fi-q")
        search_field.clear()
        search_field.send_keys(f'{brand}')
        search_field.send_keys(Keys.ENTER)

    

    def select_items(self):
        items=self.find_element_by_xpath('//*[@id="jm"]/main/div[2]/div[3]/section/div[1]')
        name=items.get_attribute('src')
        print(name)

       
   