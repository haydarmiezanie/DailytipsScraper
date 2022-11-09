from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re, timeit

# Call chromdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define Function
def main_function():
    """
    Function for start scraping.
    """
    print("Scraping start")
    # Get driver
    driver.get('https://www.dailytips.id/2020/03/553-daftar-perusahaan-di-kawasan.html')

    # Find element by xpath
    element_finder  = driver.find_element("xpath",'//*[@id="post-body-3992433005709954375"]/div[2]/ol')
    element_to_text = element_finder.text
    element_to_list = list(element_to_text.split("\n"))

    # Find company_name using Regex
    name_regex   = re.compile("PT")
    name_newlist = list(filter(name_regex.match, element_to_list))

    # Find company address using Regex
    address_regex = re.compile("Alamat")
    regex_newlist = list(filter(address_regex.match, element_to_list))

    # Find company phone using Regex
    phone_regex   = re.compile("Telp")
    phone_newlist = list(filter(phone_regex.match, element_to_list))

    # Make company_name and company_address in 1 excel
    df = pd.DataFrame(list(zip(name_newlist,regex_newlist)),columns=['Nama PT','Adress'])
    # Make phone_number in 1 excel
    df2 = pd.DataFrame(list(zip(phone_newlist)),columns=['HP'])

    df.to_excel("JABABEKA_1.xlsx") 
    df2.to_excel("JABABEKA_2.xlsx")

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d jam, %02d menit, %02d detik" % (hour, minutes, seconds)

if __name__ == "__main__":
    start = timeit.default_timer()
    main_function()
    stop = timeit.default_timer()
    print(f"Scraping is Done in {convert(stop-start)}")