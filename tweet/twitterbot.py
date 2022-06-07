from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class TwitterBot():
    def __init__(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print('pass')

    def login (self):
        driver=self.driver
        driver.get('https://twitter.com/i/flow/login')
        time.sleep(30)
        username=driver.find_element(By.XPATH,'//input')
        username.clear()
        username.send_keys('i_davidwonder')
        username.send_keys(Keys.ENTER)
        time.sleep(5)
        password=driver.find_element(By.XPATH,'//input[@name="password"]')
        password.send_keys('oyomw4rld')
        time.sleep(3)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

    def searchTrend(self):
        driver=self.driver
        ## hashtag Trend
        n_tweets=0
        n_retweets=0
        hashtags=["Rapture","jesus",'APCPresidentialPrimaries']
        for hashtag in hashtags:
            url=f'https://twitter.com/search?q=%23{hashtag}&src=typeahead_click&f=live'
            driver.get(url)
            time.sleep(4)
            for i in range(1,5):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(2)

            tweets=driver.find_elements(By.XPATH,'//div[@data-testid="like"]')

            for tweet in range(len(tweets)-1):
                try:
                    driver.execute_script('arguments[0].click();',tweets[tweet])
                    n_tweets +=1
                    time.sleep(2)
                    retweets=(driver.find_elements(By.XPATH,'//div[@data-testid="retweet"]'))[tweet]
                    driver.execute_script('arguments[0].click();',retweets)
                    retweet=driver.find_element(By.XPATH,'//div[@data-testid="retweetConfirm"]')
                    driver.execute_script('arguments[0].click();',retweet)
                    n_retweets+=1
                    time.sleep(2)   
                except Exception as e:
                    print(e)    
                print(f'{n_tweets} tweet was liked with #{hashtag} and {n_retweets} tweet was retweeted with #{hashtag}')

            driver.get('https://twitter.com')
            time.sleep(20)


