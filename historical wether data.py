#take weather data for march and april from every year possible 
from selenium import webdriver
# change the year to the desired one
year=2020

d=open(f"/home/roy/Documents/{year}.text","a")
names={
    1:"Jan",
    2:"Feb",
    3:"Mar",
    4:"Apr",
    5:"May",
    6:"Jun",
    7:"Jul",
    8:"Aug",
    9:"Sep",
    10:"Oct",
    11:"Nov",
    12:"Dec"
}
browser=webdriver.Firefox()
# link for the weather website
# browser.get("https://www.timeanddate.com/weather/jordan/amman/historic?month=2&year=2010")
def monthly():
    for i in range(1,32):
        try:
            # drop down menu for the day of the month
            browser.find_element_by_css_selector(f'#wt-his-select > option:nth-child({i})').click()
            # the hourly weather data
            search=browser.find_element_by_css_selector("#wt-his > tbody:nth-child(2)")
        
            t=search.text
            t=t.split("\n")
            for o in range (len(t)):
            # print("mar"+t)
                if o==0:
                    d.write(f"{i}-{names[mon]}-{year} {t[o]} ")
                elif o==1:
                    d.write(f"{t[o]}\n")
                else:
                    d.write(f"{i}-{names[mon]}-{year} {t[o]} \n")
                # print(f"mar-{i}-2011 {t[o]}")
            # d.write(f" {t} \n")
        except Exception:
            pass

for mon in range (1,13):
    browser.get(f"https://www.timeanddate.com/weather/jordan/amman/historic?month={mon}&year={year}")
    monthly()
    d.write("\n")
d.close()
# convert mon to month name and put the name of the month first line 
# put an empty line at the end of every month