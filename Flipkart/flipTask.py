from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class Flipkart(object):
    def __init__(self):
        self.url = "https://www.flipkart.com"
        self.xpaths = {
            'submitButton'      :   "//button[@type='submit']",
            'searchBox'         :   "//input[@type='text']",
            'sort_Popularity'   :   "//li[text()='Popularity']",
            'sort_Price_HtoL'   :   "//li[text()='Price -- Low to High']",
            'sort_Price_LtoH'   :   "//li[text()='Price -- High to Low']",
            'sort_NewestFirst'  :   "//li[text()='Newest First']",
            'sort_Relevance'    :   "//li[text()='Relevance']",
            'laptop_name'       :   "//*[@id='container']/div/div[2]/div[2]/div/div[2]/div[3]/div[{index}]/a/div[2]/div[1]/div[1]",
            'processor'         :   "//*[@id='container']/div/div[2]/div[2]/div/div[2]/div[3]/div[{index}]/a/div[2]/div[1]/div[4]/ul/li[1]",
            'ram'               :   "//*[@id='container']/div/div[2]/div[2]/div/div[2]/div[3]/div[{index}]/a/div[2]/div[1]/div[4]/ul/li[2]",
            'os'                :   "//*[@id='container']/div/div[2]/div[2]/div/div[2]/div[3]/div[{index}]/a/div[2]/div[1]/div[4]/ul/li[3]",
            'hdd'               :   "//*[@id='container']/div/div[2]/div[2]/div/div[2]/div[3]/div[{index}]/a/div[2]/div[1]/div[4]/ul/li[4]",
            'display'           :   "//*[@id='container']/div/div[2]/div[2]/div/div[2]/div[3]/div[{index}]/a/div[2]/div[1]/div[4]/ul/li[5]",
            'warranty'          :   "//*[@id='container']/div/div[2]/div[2]/div/div[2]/div[3]/div[{index}]/a/div[2]/div[1]/div[4]/ul/li[6]",}
    
    def Launch(self):
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(5)

    def searchItem(self, searchFor='laptops'):
        driver.find_element_by_xpath(self.xpaths['searchBox']).clear()
        driver.find_element_by_xpath(self.xpaths['searchBox']).send_keys(searchFor)
        driver.find_element_by_xpath(self.xpaths['submitButton']).click()
        time.sleep(5)

    def sort(self, Type='popularity'):
        driver.find_element_by_xpath(self.xpaths['sort_Popularity']).click()
        time.sleep(3)

    def getDetails(self):
        laptop_details = {}
        for items in range(1,50):
            laptop_name = driver.find_element_by_xpath(self.xpaths['laptop_name'].format(index=items)).text
            laptop_details[laptop_name] = {}
            try:
                laptop_details[laptop_name]['1'] = driver.find_element_by_xpath(self.xpaths['processor'].format(index=items)).text
                laptop_details[laptop_name]['2'] = driver.find_element_by_xpath(self.xpaths['ram'].format(index=items)).text
                laptop_details[laptop_name]['3'] = driver.find_element_by_xpath(self.xpaths['os'].format(index=items)).text
                laptop_details[laptop_name]['4'] = driver.find_element_by_xpath(self.xpaths['hdd'].format(index=items)).text
                laptop_details[laptop_name]['5'] = driver.find_element_by_xpath(self.xpaths['display'].format(index=items)).text
                laptop_details[laptop_name]['6'] = driver.find_element_by_xpath(self.xpaths['warranty'].format(index=items)).text
            except NoSuchElementException:
                pass
            
        return laptop_details
        	
if __name__ == '__main__':
    driver = webdriver.Chrome()
    flip = Flipkart()
    flip.Launch()
    flip.searchItem()
    flip.sort()
    di = flip.getDetails()
    for k, v in di.iteritems():
        print 
        print k
        for key, value in v.iteritems():
            print value
    driver.quit()
