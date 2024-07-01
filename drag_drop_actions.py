"""""
Using python selenium automation and action chains visit the URL https://jqueryui.com/droppable/
and do a drag and drop operation of the white rectangular box into the yellow rectangular box into the yellow
rectangular box
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains


class Droppable:
    source_locator = "//*[@id='draggable']"
    target_locator = "//*[@id='droppable']"

    def __init__(self,url):
        self.url=url
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def get_url(self):
        try:
         self.driver.maximize_window()
         self.driver.get(self.url)
         sleep(3)
         return True

        except WebDriverException as e:
            print("Error : URL is not opened", e)
            return False


    def iframe(self):
        try:
         iframe_element=self.driver.find_element(by=By.TAG_NAME, value="iframe")
         self.driver.switch_to.frame(iframe_element)
         sleep(2)
         return True

        except StaleElementReferenceException as e:
            print("Error : element not found")
            return False

    def drag_drop(self):
        try:
         action = ActionChains(self.driver)
         source_element = self.driver.find_element(by=By.XPATH,value=self.source_locator)
         target_element = self.driver.find_element(by=By.XPATH, value=self.target_locator)
         if source_element.is_displayed() and target_element.is_displayed():
            if source_element.is_enabled() and target_element.is_enabled():

                action.drag_and_drop(source_element,target_element).perform()
                sleep(2)
                return True

        except (NoSuchElementException,ElementNotVisibleException) as e:
            print("Error :cant locate the element",e)
            return True

        finally:
            self.driver.quit()
            return None


"""
if __name__=="__main__":
    droppable = Droppable("https://jqueryui.com/droppable/")
    droppable.get_url()
    droppable.iframe()
    droppable.drag_drop()
"""