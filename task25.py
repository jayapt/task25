from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

class SubmitForm:
    def __init__(self, url="https://www.imdb.com/search/name/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 5)
        self.action = ActionChains(self.driver)
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        url = self.wait.until(EC.url_to_be(self.url))

    def quit(self):
        self.driver.quit()
    def findElementByclassname(self, className):
        return self.driver.find_element(by=By.ID, value=className)
    def findElementByTagname(self, name):
        return self.driver.find_element(by=By.TAG_NAME, value=name)
    def findElementByXpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)


    def submit(self):
        self.boot()
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button/span"))).click()
            self.wait.until(EC.presence_of_element_located((By.ID, "text-input__3"))).send_keys("virat kohli")
            self.wait.until(EC.presence_of_element_located((By.ID, "text-input__8"))).send_keys("05-11-1988")
            self.wait.until(EC.presence_of_element_located((By.ID, "text-input__9"))).send_keys("27-09-2024")
            self.wait.until(EC.presence_of_element_located((By.ID, "text-input__4"))).send_keys("11-05")
            self.wait.until(EC.presence_of_element_located((By.ID, "text-input__5"))).send_keys(("November fifth"))
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]'))).click()
            print("Successfully searched")
        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()
if __name__ == "__main__":
    obj = SubmitForm()
    obj.submit()

