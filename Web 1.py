import datetime
import time
import pyautogui
import shutil
import pyodbc
import pandas as pd
import os
from email.message import EmailMessage
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options


print("Code is working")

# sender = "319063@nttdata.com"
# recipient = "317848@nttdata.com"
# cc_email = '319063@nttdata.com'

#chrome_options = Options()
#chrome_options.add_argument('--headless')  # Enable headless mode
 
#driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()
driver.maximize_window()
Loop_Count = 1


try:

    url = 'https://ftb.dsoportal.com/Home'

    driver.get(url)
    time.sleep(5)
    
    pyautogui.click(x=400,y=300)
    pyautogui.typewrite("319063")
    pyautogui.press("tab")
        
    pyautogui.typewrite("Lakshmi_0702")
    pyautogui.press("enter")


    for i in range(Loop_Count):
        driver.get(url)
        time.sleep(5)
    
        pyautogui.click(x=400,y=300)
        pyautogui.typewrite("319063")
        pyautogui.press("tab")
        
        pyautogui.typewrite("Lakshmi_0702")
        pyautogui.press("enter")
        
        wait = WebDriverWait(driver,20)
        
        portal = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='txtUserName']")))
        portal.send_keys("Gokulakrishnan.Anand")
        
        password = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtPassword']")))
        password.send_keys("Lakshmi_0702")
        
        domain = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='txtDomain']")))
        domain.send_keys("NTTDSO")
        
        login = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='btnlogin']")))
        login.click()
        
        Menu = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='kt_header_menu']/ul/li[2]/a")))
        Menu.click()
        time.sleep(10)
        
        Main_Content = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='pca-main-content']/div/div[1]/ul/li[5]/a")))
        Main_Content.click()
        time.sleep(10)
        
        download = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='grid-reports']/table/tbody/tr/td[2]/a")))
        download.click()
        time.sleep(100)
        print("Web ran Successfully")

    driver.quit()

    print("File is downloaded moving to directory folder")
    download_dir = r'C:\Users\317078\Downloads'   

    src_file = os.path.join(download_dir, 'PCARequests.xlsx')
    dst_dir = os.path.expanduser(r'C:\Users\317078\Desktop\Asset Automation')
    dst_file = os.path.join(dst_dir, 'PCARequests.xlsx')

    shutil.move(src_file, dst_dir)

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = "Code execution successful"
    body = "The code ran successfully."         
    message.attach(MIMEText(body, 'plain'))
    
    smtp = smtplib.SMTP("155.16.123.161", port=25)
    smtp.sendmail(sender,recipient, message.as_string())
    smtp.quit()
    print("Success mail sent")

except Exception as e:
    print(f"Code Having error: {e}")
   
    message1 = MIMEMultipart()
    message1['From'] = sender
    message1['To'] = recipient
    message1['Cc'] = cc_email
    message1['Subject'] = "Error Alert"
    body1 = "Error occured in bot."
    message1.attach(MIMEText(body1, 'plain'))

    smtp1 = smtplib.SMTP("155.16.123.161", port=25)
    smtp1.sendmail(sender,recipient, message1.as_string())
    smtp1.quit()
    print("Failure mail sent")
