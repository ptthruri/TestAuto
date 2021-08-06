import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Làm trắng thông tin
def clear(browser):
    username = browser.find_elements_by_xpath("//input[@id='user_login']")
    username = username[0]
    username.clear()

    password = browser.find_elements_by_xpath("//input[@id='user_pass']")
    password = password[0]
    password.clear()

# Tên đúng Pass sai
def validate_with_username_correct_and_password_incorrect(driver):
    try:
        # Tìm xpath username
        username = browser.find_elements_by_xpath("//input[@id='user_login']")
        if not username:
            print("Case 1 fail")
            return False
        username = username[0]
        username.clear()
        # Truyền dữ liệu username
        username.send_keys("demo.student.01")
        # Tìm xpath password
        password = browser.find_elements_by_xpath("//input[@id='user_pass']")
        if not password:
            print("Case 1 fail")
            password = password[0]
            password.clear()
        login_button_elm = browser.find_elements_by_xpath("//input[@id='wp-submit']")
        login_button_elm[0].click()
        # Nếu hiển thị thông báo error thì Case 1 Pass
        if browser.find_elements_by_xpath("//div[@id='login_error']"):
            print("Case 1 pass")
            return True
        else:
            print("Case 1 fail")
            return False
    except Exception as e:
        print(e)

def validate_with_username_incorrect_and_password_correct(driver):
    try:
        username = browser.find_elements_by_xpath("//input[@id='user_login']")
        if not username:
            print("Case 2 fail")
            return False
        username = username[0]
        username.clear()

        password = browser.find_elements_by_xpath("//input[@id='user_pass']")
        if not password:
            print("Case 2 fail")
            password = password[0]
            password.clear()
            password.send_keys("Password123")
        login_button_elm = browser.find_elements_by_xpath("//input[@id='wp-submit']")
        login_button_elm[0].click()
        if browser.find_elements_by_xpath("//div[@id='login_error']"):
            print("Case 2 pass")
            return True
        else:
            print("Case 2 fail")
            return False
    except Exception as e:
        print(e)


def validate_with_username_correct_and_password_correct(driver):
    try:
        username = browser.find_elements_by_xpath("//input[@id='user_login']")
        if not username:
            print("Case 3 fail")
        username = username[0]
        username.clear()
        username.send_keys("demo.student.01")
        password = browser.find_elements_by_xpath("//input[@id='user_pass']")
        if not password:
            print("Case 3 fail")
            return False
        password = password[0]
        password.clear()
        password.send_keys("Password123")

        login_button_elm = browser.find_elements_by_xpath("//input[@id='wp-submit']")
        login_button_elm[0].click()
        if browser.find_elements_by_xpath("//span[normalize-space()='Dashboard']"):
            print("Case 3 pass")
            return True
        else:
            print("Case 3 fail")
            return False
    except Exception as e:
        print(e)



if __name__ == '__main__':
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://qasystem.com.vn/school/wp-login.php?loggedout=true&wp_lang=en_US")
    time.sleep(5)

    case_1 = validate_with_username_correct_and_password_incorrect(browser)
    time.sleep(5)
    clearcase_1 = clear(browser)
    time.sleep(5)

    case_2 = validate_with_username_incorrect_and_password_correct(browser)
    time.sleep(5)
    clearcase_2 = clear(browser)
    time.sleep(5)

    case_3 = validate_with_username_correct_and_password_correct(browser)
    time.sleep(5)

browser.quit()


