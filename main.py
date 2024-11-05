import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver=r"C:\developer\chromedriver.exe"
driver=webdriver.Chrome(service=Service(chrome_driver))
driver.get('your 99acres location link')
time.sleep(4)
ok_understand=driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[4]/div[1]/div/div/div/div[5]/div')
ok_understand.click()
names=driver.find_elements(By.CLASS_NAME, 'tupleNew__locationName')
n=[name.text for name in names]

addr=driver.find_elements(By.CLASS_NAME, 'tupleNew__propType')
address=[add.text for add in addr]


ren=driver.find_elements(By.CSS_SELECTOR, '.tupleNew__priceValWrap span')
rent=[re.text for re in ren if re.text!='/month']


sq=driver.find_elements(By.CSS_SELECTOR, '.tupleNew__area1Type')
square_feet=[s.text for s in sq if 'BHK' not in s.text]


lin=driver.find_elements(By.CLASS_NAME, 'tupleNew__propertyHeading')
link=[li.get_attribute('href') for li in lin]

driver.get('https://forms.gle/hzSyeFjqd6bKgrZSA')
for i in range (0, len(n), 1):
    time.sleep(3)

    name_field= driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field.send_keys(n[i])


    bhkandaddress_field = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    bhkandaddress_field.send_keys(address[i])


    rent_field = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent_field.send_keys(rent[i])


    sqf_field = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    sqf_field.send_keys(square_feet[i])


    link_field = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(link[i])


    submit=driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()

    another_form=driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_form.click()





driver.quit()