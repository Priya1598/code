import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
url = "https://catalys.portal.nttdataservices.com/report/progress/index.php?course=11571"
Epic = "https://catalys.portal.nttdataservices.com/report/progress/index.php?course=11559"
Epicmychart = "https://catalys.portal.nttdataservices.com/report/progress/index.php?course=16014"
UMMHC = "https://catalys.portal.nttdataservices.com/report/progress/index.php?course=11565"
UMMHCepic ="https://catalys.portal.nttdataservices.com/report/progress/index.php?course=16016"
Cedars="https://catalys.portal.nttdataservices.com/report/progress/index.php?course=11572"
HMH = "https://catalys.portal.nttdataservices.com/report/progress/index.php?course=11573"
NYULH = "https://catalys.portal.nttdataservices.com/report/progress/index.php?course=11561"
MSHS = "https://catalys.portal.nttdataservices.com/report/progress/index.php?course=11560"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

Loop_Count=1
wait = WebDriverWait(driver,100)

for i in range(Loop_Count):
        driver.get(url)
        time.sleep(5)
   
        Start_amount = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/span/input")
        Start_amount.send_keys("251623")
        time.sleep(5)
 
        Start_amount = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input")
        Start_amount.click()
        time.sleep(5)
       
        domain = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div[2]/span/input")))
        domain.send_keys("Gdh44kz2dg")
        time.sleep(5)
       
        Verify = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/form/div[2]/input")
        Verify.click()
        time.sleep(70)
       
                
        Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]/a')))
        Download.click()
        time.sleep(10)
        
driver.get(Epic)
for i in range(Loop_Count):
        driver.get(Epic)
        time.sleep(10)
        
        Epic_Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]/a')))
        Epic_Download.click()
        time.sleep(10)
        
driver.get(Epicmychart)
for i in range(Loop_Count):
        driver.get(Epicmychart)
        time.sleep(10)
        
        Epicmychart_Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]')))
        Epicmychart_Download.click()
        time.sleep(10)
        
driver.get(UMMHC)
for i in range(Loop_Count):
        driver.get(UMMHC)
        time.sleep(10)
        
        UMMHC_Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]')))
        UMMHC_Download.click()
        time.sleep(10)
        
driver.get(UMMHCepic)
for i in range(Loop_Count):
        driver.get(UMMHCepic)
        time.sleep(10)
        
        UMMHCepic_Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]')))
        UMMHCepic_Download.click()
        time.sleep(10)
        
driver.get(Cedars)
for i in range(Loop_Count):
        driver.get(Cedars)
        time.sleep(10)
        
        Cedars_Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]')))
        Cedars_Download.click()
        time.sleep(10)
        
driver.get(HMH)
for i in range(Loop_Count):
        driver.get(HMH)
        time.sleep(10)
        
        MHM_Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]')))
        MHM_Download.click()
        time.sleep(10)
        
driver.get(NYULH)
for i in range(Loop_Count):
        driver.get(NYULH)
        time.sleep(10)
        
        NYULH_Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]')))
        NYULH_Download.click()
        time.sleep(10)
        
driver.get(MSHS)
for i in range(Loop_Count):
        driver.get(MSHS)
        time.sleep(10)
        
        MSHS_Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]')))
        MSHS_Download.click()
        time.sleep(10)
        
           
        
print("Web ran Successfully")
driver.quit()
