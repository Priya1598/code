import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
url = "https://catalys.portal.nttdataservices.com/report/progress/index.php?course=11571"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

Loop_Count=1
wait = WebDriverWait(driver,10)

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
        time.sleep(60)
       
        # Reports = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/nav/ul/li[5]/a')))
        # Reports.click()
        # time.sleep(10)
        
        # Activity_Completion = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/div/div/ul/li[6]/a')))
        # Activity_Completion.click()
        # time.sleep(10)
        
        Download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/div/div[3]/div/section/div/ul/li[1]/a')))
        Download.click()
        time.sleep(10)
        
        # sla = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[2]/ul[1]/li[5]/a")))
        # sla.click()
        # time.sleep(5)
        
        # download = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/span")))
        # download.click()
        # time.sleep(5)
        
        # closed_month = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/ul/li[2]/span[2]")))
        # closed_month.click()
        # time.sleep(5)
        
        # download = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/span")))
        # download.click()                                                
        # time.sleep(5)
        
        # Custom_report = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/ul/li[11]/span[2]")))
        # Custom_report.click()
        # time.sleep(5)
    
        # download = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[11]/span")))
        # download.click()
        # time.sleep(5)
       
       
        # telecom = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/nav/a[2] ")))
        # telecom.click()
        # time.sleep(10)
        
        # telecom_1 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/ul/li[1]/span[2]")))
        # telecom_1.click()
        # time.sleep(5)
        
        # download = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]/span")))
        # download.click()
        # time.sleep(5)
        
        # telecom_2= wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/ul/li[2]/span[2]")))
        # telecom_2.click()
        # time.sleep(5)
        
        # download = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div[2]/span")))
        # download.click()
        # time.sleep(5)
        
print("Web ran Successfully")
driver.quit()
