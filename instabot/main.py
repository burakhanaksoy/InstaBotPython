from selenium import webdriver
from insta_constants.xpath_constants import *
from insta_constants.user_constants import *
from time import sleep


class Instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(10)
        self.driver.get('https://instagram.com')
        sleep(2)
        self.driver.find_element_by_xpath(
            LOGIN_USERNAME).send_keys(self.username)
        self.driver.find_element_by_xpath(
            LOGIN_PASSWORD).send_keys(self.password)
        self.driver.find_element_by_xpath(LOGIN_BTN).click()

        save_pwd_info_check = driver.find_element_by_xpath(
            "//*[contains(text(),'Not Now')]").text  # checks for save pwd info? pop up

        if not save_pwd_info_check is None:
            self.driver.find_element_by_xpath(
                "//*[contains(text(),'Not Now')]").click()

        receive_notifications_info_check = driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').text

        if not receive_notifications_info_check is None:
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[3]/button[2]').click()

        self.driver.get(USER_MAIN_PAGE)
        self.follower_number = int(driver.find_element_by_xpath(
            FOLLOWER_XPATH).text.split(' ')[0])
        self.following_number = int(driver.find_element_by_xpath(
            FOLLOWING_XPATH).text.split(' ')[0])

    def get_followers(self):
        # click on follower and start scrolling down
        self.driver.find_element_by_xpath(FOLLOWER_XPATH).click()

        # define WebElement you want to scroll down on
        scroller = driver.find_element_by_class_name('isgrP')
        last_ht, ht = 1, 0
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = driver.execute_script(""" 
            arguments[0].scrollBy(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight * 0.3;
            """, scroller)

        follower_path_dynamic = driver.find_elements_by_tag_name('a')
        followers = [
            name.text for name in follower_path_dynamic if name.text != '']

        # close tab
        driver.find_element_by_xpath('//*[@class=\"WaOAr\"]//button').click()
        return followers

    def get_following(self):
        # get following
        self.driver.find_element_by_xpath(FOLLOWING_XPATH).click()
        last_ht, ht = 1, 0
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = driver.execute_script(""" 
            arguments[0].scrollBy(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight * 0.3;
            """, scroller)
        following_path_dynamic = driver.find_elements_by_tag_name('a')
        following = [
            name.text for name in following_path_dynamic if name.text != '']

        return following

    def find_unfollowing(self):
        print(self.get_following() - self.get_followers())
        print(
            f'Not following you --> {self.get_following() - self.get_followers()}')


bot = Instabot(USERNAME, PASSWORD)
bot.find_unfollowing()
