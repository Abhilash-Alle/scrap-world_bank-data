from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup


s=Service("C:/Windows/chromedriver.exe")
driver=webdriver.Chrome(service=s)
#return driver

url="https://data360.worldbank.org/en/search?tab=all"
body_url="https://data360.worldbank.org/"
driver.get(url)
#time.sleep(2)
wait=WebDriverWait(driver,10)

data_name=[]
update_details=[]
dissagregrations=[]
database=[]
pdf_link=[]
body_link=[]

page=1
while page <= 100:
    print("page:",page)
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    box = soup.find_all("div", class_="search-item")

    for item in box:
        name = item.find("a", class_="search-item-link")
        if name:
            names = name.text.strip()
            data_name.append(names)
        else:
            print("no data")

        details = item.find("p", class_="tui__sm_title")
        if details:
            details_text = details.text.strip()
        else:
            details_text = "no details"
        update_details.append(details_text)

        dis = item.find("div", class_="tui_badge_group")
        if dis:
            dis_text = dis.text.strip()
        else:
            dis_text = "no dissagregrations"
        dissagregrations.append(dis_text)

        dataset = item.select_one('a[href*="/en/dataset/"]')
        if dataset:
            database_text1 = dataset.text.strip()
        else:
            database_text1 = "no database"
        database.append(database_text1)

        pdf_tag = item.find("a", class_="download-pdf")
        if pdf_tag:
            pdf_link.append(pdf_tag.get("href"))
        else:
            pdf_link.append("no pdf")

        body_l = item.select_one('a[href*="/en/dataset/"]')
        if body_l and body_l.get("href"):
            body_link.append(body_url + body_l.get("href"))
        else:
            body_link.append("no link")


    try:
        next_button=wait.until(EC.element_to_be_clickable((By.XPATH, """//a[@aria-label='Goto next Page']""")))
        driver.execute_script("arguments[0].click();", next_button)
        #next_button.click()
        time.sleep(2)

        page+=1

    except:
        print("no page")
        break

df=pd.DataFrame({"DATA_NAME":data_name,"UPDATE_DETAILS":update_details,"DISSAGREGATIONS":dissagregrations,"DATABASE":database,"PDF_LINK":pdf_link,"BODY_LINK":body_link})
print(df)
df.to_csv("world_bank_data.csv",index=False)
driver.quit()