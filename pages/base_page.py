from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from data import DEFAULT_TIMEOUT
from locators import MODAL_LOADING

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open_url(self, url):
        self.driver.get(url)
        self.wait_page_loading()    

    def wait_page_loading(self):
        self.wait_invisibility(MODAL_LOADING)

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.wait_clickable(locator).click()

    def send_keys(self, locator, value):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def is_displayed(self, locator):
        return self.wait_visible(locator).is_displayed()
    
    def is_element_displayed(self, locator):
        elements = self.driver.find_elements(*locator)
        return any(element.is_displayed() for element in elements)

    def wait_url_contains(self, value):
        self.wait.until(
            EC.url_contains(value)
        )

    def wait_invisibility(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def get_element_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def refresh_page(self):
        self.driver.refresh()

    def find_all_visible_elements(self, locator):
        return self.wait.until(
        EC.visibility_of_all_elements_located(locator)
    )

    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(
            source, target
        ).perform()
    
    def find_child_elements(self, parent, locator):
        return parent.find_elements(*locator)  

    def click_element(self, element):
        self.wait_element_clickable(element).click()

    def wait_element_clickable(self, element):
        return self.wait.until(
            EC.element_to_be_clickable(element)
        )

    def html5_drag_and_drop(self, source_locator, target_locator):
        source = self.wait_visible(source_locator)
        target = self.wait_visible(target_locator)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
        """, source, target)