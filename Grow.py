import csv
from selenium.webdriver.common.by import By
import time
import csv
from seleniumbase import Driver

driver = Driver(uc=True)

with open('URL.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        Region = row[0]
        driver.get(row[1])

        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True

        provider_links = []
        provider_elements = driver.find_elements(By.CSS_SELECTOR, 'div.pb-8>div>div:nth-child(4)>div:nth-child(3)>a:nth-child(odd)')
        for provider_element in provider_elements:
            provider_link = provider_element.get_attribute("href")
            provider_links.append(provider_link)
        for provider_link in provider_links:
            print("LINK >>> ", provider_link)
            driver.get(provider_link)
            
            city_USED = ""

            try:
                name = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/div/div').text
                print("name >>> ", name) 
            except:
                name = "Unknown"

            try:
                Bio = ""
                Bio_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[1]/p')
                for Bio_element in Bio_elements:
                    Bio = Bio + Bio_element.text
                print("Bio >>> ", Bio)
            except:
                Bio = "No data"
            
            try:
                Identifies = ""
                Identify_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[1]/div[1]/div/a/span/div')
                for Identify_element in Identify_elements:
                    Identifies = Identifies + Identify_element.text
                print("Identifies >>> ", Identifies)
            except:
                Identifies = "No data"
            
            try:
                Specialities = ""
                Bookmark_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[1]/div[2]/div/div/a/span/div')
                for Bookmark_element in Bookmark_elements:
                    Specialities = Specialities + Bookmark_element.text
                normal_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[1]/div[2]/div/a/span/div')
                for normal_element in normal_elements:
                    Specialities = Specialities + normal_element.text
                print("specialties >>> ", Specialities)
            except:
                Specialities = "No data"
            
            try:
                Seeves_ages = ""
                age_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[1]/div[3]/div/a/span/div')
                for age_element in age_elements:
                    Seeves_ages = Seeves_ages + age_element.text
                print("Seeves_ages >>> ", Seeves_ages)
            except:
                Seeves_ages = "No data"    
                
            try:
                Licensed_in = ""
                license_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[1]/div[4]/div/a/span/div')
                for license_element in license_elements:
                    Licensed_in = Licensed_in + license_element.text
                print("Licensed_in >>> ", Licensed_in)
            except:
                Licensed_in = "No data"

            try:
                Accepted_Insurances = ""
                Insurance_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[1]/div[5]/div/a/span/div')
                for Insurance_element in Insurance_elements:
                    Accepted_Insurances = Accepted_Insurances + Insurance_element.text
                print("Accepted_Insurances >>> ", Accepted_Insurances)
            except:
                Accepted_Insurances = "No data"    

            try:
                Appointments_Type = ""
                type_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[1]/div[6]')[0].text
                print("Appointments_Type >>> ", Appointments_Type)
            except:
                Appointments_Type = "No data"        
            
            try:
                driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div/div/div[2]/div/div[3]/div[2]/a').click()
                print("See more abilites clicked!!!!!!!!!!!!!")
                try:
                    available_buttons =[]
                    elements = driver.find_elements(By.CSS_SELECTOR, 'table  > tbody > tr > td')
                    for element in elements:
                        status = element.get_attribute("aria-disabled")
                        if status == "true":
                            print("")
                        else:
                            available_buttons.append(element)
                    count = len(available_buttons)
                    print("Count", count)
                except:
                    count = "Empty"
                try:
                    price = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/form/div/div[1]/div[1]/div[3]/div[2]/div/h2[1]').text
                    print("Price >>> ", price)
                except:
                    price = "Unknown"
            except:
                print("Button >>> ", "There is no button")

            results = [Region, city_USED,provider_link ,name, Bio, Identifies, Specialities, Seeves_ages, Licensed_in, Accepted_Insurances, Appointments_Type, count, price]
            with open('clients.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(results)
driver.close()    