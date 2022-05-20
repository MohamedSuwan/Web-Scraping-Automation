from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
d=open(f"/home/roy/Documents/drugs.text","a")
names= ["Metformin","Levothyroxine","Atorvastatin","Lisinopril","Albuterol"]

browser=webdriver.Firefox()
browser.get("http://www.jfda.jo/Pages/viewpage.aspx?pageID=184") 
browser.switch_to_frame(0)
for name in names:

    scientific_name=browser.find_element_by_xpath("//*[@id='ing']").send_keys(name)
    browser.find_element_by_css_selector("#btnFreeSrch").click()
    time.sleep(4)
    search= browser.find_element_by_css_selector(".table-scrollable")
    browser.find_element_by_xpath("//*[@id='ing']").send_keys(Keys.CONTROL,"a")
    browser.find_element_by_xpath("//*[@id='ing']").send_keys(Keys.DELETE)

    text=search.text
    d.write(text)
