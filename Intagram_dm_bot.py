from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time                                                        

class InstagramBot:
    def __init__(self, username, password, users, message):
        self.username = username
        self.password = password
        self.users = users
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = webdriver.Chrome()
        self.bot.maximize_window()
        self.login()
 
    def login(self):
        self.bot.get(self.base_url)
 
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
 
        # first pop-up
        self.bot.find_element(By.XPATH,
                              '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(5)
 
        # direct button
        self.bot.find_element(By.XPATH,
                              '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/span').click()
        time.sleep(3)
 
        # clicks on pencil icon
        self.bot.find_element(By.XPATH,
                              '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[1]/div[2]').click()
        time.sleep(2)
 
        for user in self.users:
            # enter the username
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/input').send_keys(user)
            time.sleep(3)
 
            # click on the username
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div/div/span[1]/span/div/span').click()
            time.sleep(4)
 
            # next button
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[4]/div').click()
            time.sleep(4)
 
            # click on message area
            send = self.bot.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
 
            # types message including the username
            send.send_keys(f"{self.message} {user}")
            time.sleep(1)
 
            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)
 
            # clicks on direct option or pencil icon
            self.bot.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[1]/div[2]').click()
            time.sleep(4)
 
    def close_browser(self):
        self.bot.close()

# Run the bot
if __name__ == "__main__":
    username = "ajah35961@gmail.com"
    password = "Feb662005"
    users = ['ana_d_armas', 'madisonbeer']
    message = "reaching"

    bot = InstagramBot(username, password, users, message)
    bot.close_browser()