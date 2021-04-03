from insta_constants.user_constants import USERNAME

LOGIN_USERNAME = "//span[contains(text(),\"Phone number\")]//following::input"
LOGIN_PASSWORD = "//span[contains(text(),\"Password\")]//following::input"
LOGIN_BTN = "//*[@id=\"loginForm\"]/div/div[3]/button/div"
FOLLOWER_HREF = '/' + USERNAME + '/followers/'
FOLLOWING_HREF = '/' + USERNAME + '/following/'
FOLLOWER_XPATH = f'//a[contains(@href,"{FOLLOWER_HREF}")]'
FOLLOWING_XPATH = f'//a[contains(@href,"{FOLLOWING_HREF}")]'
USER_MAIN_PAGE = "https://instagram.com/" + USERNAME
